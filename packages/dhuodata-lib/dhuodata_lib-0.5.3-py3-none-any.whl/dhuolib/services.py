import json
import requests
from abc import ABC, abstractmethod


class APIError(Exception):
    pass


class ServiceML(ABC):

    def __init__(self, service_endpoint: str = 'http://localhost:8000'):
        self.service_endpoint = f"{service_endpoint}/api"

    @abstractmethod
    def create(self, params, **kwargs):
        pass

    @abstractmethod
    def search(self, filter_string: str = "", max_results: int = 10, page_token: str = None, **kwargs):
        pass

    def _handle_response(self, response):
        if not response.ok:
            raise APIError(
                f"API request failed with status {response.status_code}: {response.text}")
        return response.json()


class ExperimentMLAPI(ServiceML):
    def __init__(self, service_endpoint):
        super().__init__(service_endpoint)
        self.service_endpoint = f"{self.service_endpoint}/experiment"
        self.headers = {"Content-Type": "application/json"}

    def create(self, experiment_params: dict):
        response = requests.post(
            f"{self.service_endpoint}",
            data=json.dumps(experiment_params),
            headers=self.headers,
        )
        return self._handle_response(response)

    def search(self, filter_string: str = "", max_results: int = 10, page_token: str = '', view_type: int = 1):
        response = requests.get(
            f"{self.service_endpoint}/search?filter_string={filter_string}&max_results={max_results}&page_token={page_token}&view_type={view_type}"
        )
        return self._handle_response(response)

    def predict_online(self, params={}, files=None):
        if params is None and not isinstance(params, dict):
            raise ValueError("json_data must be a dict")
        response = requests.post(
            f"{self.service_endpoint}/predict_online",
            data=params,
            files=files,
        )
        return self._handle_response(response)

    def download_pickle(
        self,
        experiment_name: str,
        type_model: str,
        model_name: str,
        model_stage: str = "",
        run_id: str = "",
        local_filename: str = "model.pickle",
    ):
        url = f"{self.service_endpoint}/dowload/batch/{experiment_name}/{model_name}?model_stage={model_stage}&run_id={run_id}&type_model={type_model}"
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename


class ModelMLAPI(ServiceML):

    def __init__(self, service_endpoint):
        super().__init__(service_endpoint)
        self.service_endpoint = f"{self.service_endpoint}/models"
        self.headers = {"Content-Type": "application/json"}

    def create(self, model_params):
        if model_params is None and not isinstance(model_params, dict):
            raise ValueError("json_data must be a dict")
        response = requests.post(
            f"{self.service_endpoint}",
            data=json.dumps(model_params),
            headers=self.headers,
        )
        return self._handle_response(response)

    def transition_model(self, model_name: str, version: str, stage: str):
        response = requests.get(
            f"{self.service_endpoint}/transition-model/{model_name}?version={version}&stage={stage}",
        )
        return self._handle_response(response)

    def search(self, filter_string: str = "", max_results: int = 10, page_token: str = ""):
        response = requests.get(
            f"{self.service_endpoint}/search?filter_string={filter_string}&max_results={max_results}&page_token={page_token}"
        )
        return self._handle_response(response)


class RunsMLAPI(ServiceML):

    def __init__(self, service_endpoint):
        super().__init__(service_endpoint)
        self.service_endpoint = f"{self.service_endpoint}/runs"

    def create(self, run_params, files):
        response = requests.post(
            f"{self.service_endpoint}", data=run_params, files=files
        )
        return self._handle_response(response)

    def search(self, filter_string: str = "", max_results: int = 10, page_token: str = "", experiment_name: str = ""):
        response = requests.get(
            f"{self.service_endpoint}/{experiment_name}?filter_string={filter_string}&max_results={max_results}&page_token={page_token}",
        )
        if response.status_code == 204:
            raise ValueError("Experiment not found")
        return self._handle_response(response)


class ProjectMLAPI:
    def __init__(self, service_endpoint):

        if not isinstance(service_endpoint, str):
            raise ValueError("service_endpoint must be a string")

        self.service_endpoint = f"{service_endpoint}/api"
        self.headers = {"Content-Type": "application/json"}

    def create_project(self, project_name):
        body = {"project_name": project_name}
        return requests.post(f"{self.service_endpoint}/project", json=body)

    def deploy_script(
        self, project_name: str, script_file_encode: str, requirements_file_enconde: str
    ):
        body = {
            "project_name": project_name,
            "requirements_content": requirements_file_enconde.decode("utf-8"),
            "run_script_content": script_file_encode.decode("utf-8"),
        }
        response = requests.post(f"{self.service_endpoint}/deploy",
                                 json=body, headers=self.headers)

        return response.json()

    def get_pipeline_status(self, project_name: str):
        route = "deploy/{}".format(project_name)
        response = requests.get(f"{self.service_endpoint}/{route}")

        return response.json()

    def create_cluster(self, project_name: str, cluster_size: int):
        body = {"project_name": project_name, "cluster_size": cluster_size}
        response = requests.post(f"{self.service_endpoint}/cluster",
                                 json=body, headers=self.headers)

        return response.json()

    def run_pipeline(self, project_name: str):
        body = {"project_name": project_name}
        response = requests.post(
            f"{self.service_endpoint}/cluster/run", json=body, headers=self.headers)

        return response.json()


class ServiceAPIMLFacade:
    def __init__(self, service_endpoint):
        self.experiment_api = ExperimentMLAPI(service_endpoint)
        self.model_api = ModelMLAPI(service_endpoint)
        self.runs_api = RunsMLAPI(service_endpoint)
        self.project_api = ProjectMLAPI(service_endpoint)
