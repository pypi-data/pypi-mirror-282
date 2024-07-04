import requests

class EllmentalError(Exception):
    """Custom exception for eLLMental errors."""
    pass

class Ellmental:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.test_suite_id = None
        self.test_execution_id = None
        self.token = token

    def set_evaluation_context(self, test_suite_id):
        self.test_suite_id = test_suite_id

    def search_pipeline_query(self, pipeline_id, context_id, query):
        url = f"{self.base_url}/api/search_pipelines/{pipeline_id}"
        params = {
            "query": query,
            "context_id": context_id
        }
        headers = self._get_headers()
        response = requests.get(url, headers=headers, params=params)
        return self._handle_response(response)

    def llm_evaluation(self, pipeline_id, query):
        return self.search_pipeline_query(pipeline_id, None, query)
    
    def list_search_pipelines(self):
        url = f"{self.base_url}/api/search_pipelines/"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def start_evaluation_execution(self):
        if not self.test_suite_id:
            raise ValueError("You need to set the evaluation context before starting a test execution")
        
        url = f"{self.base_url}/api/test_suites/{self.test_suite_id}/test_executions"
        headers = self._get_headers()
        response = requests.post(url, headers=headers)
        execution = self._handle_response(response)
        self.test_execution_id = execution["id"]

    def push_evaluation_result(self, test_case_id, test_result, status, metadata=None):
        if not self.test_suite_id or not self.test_execution_id:
            raise ValueError("You need to start a test execution before creating a test result")
        
        url = f"{self.base_url}/api/test_suites/{self.test_suite_id}/test_executions/{self.test_execution_id}/test_results"
        data = {
            "test_suite_id": self.test_suite_id,
            "test_case_id": test_case_id,
            "test_result": str(test_result),
            "user_metadata": metadata or {},
            "status": status
        }
        headers = self._get_headers()
        response = requests.post(url, json=data, headers=headers)
        return self._handle_response(response)

    def finish_evaluation_execution(self):
        if not self.test_suite_id or not self.test_execution_id:
            raise ValueError("You need to start a test execution before creating a test result")
        
        url = f"{self.base_url}/api/test_suites/{self.test_suite_id}/test_executions/{self.test_execution_id}/finish"
        headers = self._get_headers()
        response = requests.post(url, headers=headers)
        return self._handle_response(response)

    def list_evaluation_cases(self):
        if not self.test_suite_id:
            raise ValueError("You need to set the evaluation context before starting a test execution")
        url = f"{self.base_url}/api/test_suites/{self.test_suite_id}/test_cases"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        return self._handle_response(response)
    
    def _get_headers(self):
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers

    def _handle_response(self, response):
        if response.status_code != 200 and response.status_code != 201:
            raise EllmentalError(f"Error {response.status_code}: {response.text}")
        return response.json()
