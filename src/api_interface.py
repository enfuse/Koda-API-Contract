from abc import ABC, abstractmethod
from submit_request_body import SubmitRequestBody
from submit_response_body import SubmitResponseBody

class ApiInterface(ABC):
    
    """Handler method for the /submit endpoint, formerly known as /koda
    
    This method will respond to a prompt from the LLM client
    """
    @abstractmethod
    def submitPrompt(self, data: SubmitRequestBody) -> SubmitResponseBody:
        pass
    
    """Handler method for the /reset endpoint
    
    This method will deactivate the given session-id, 
    and respond with a newly generated and activated session-id
    """
    @abstractmethod
    def resetSession():
        pass