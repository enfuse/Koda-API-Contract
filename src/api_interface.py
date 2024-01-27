from abc import ABC, abstractmethod
from submit_request_body import SubmitRequestBody
from submit_response_body import SubmitResponseBody

class ApiInterface(ABC):
    @abstractmethod
    def submit(self, data: SubmitRequestBody) -> SubmitResponseBody:
        
        SubmitRequestBody()
        pass