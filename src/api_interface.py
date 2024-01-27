from abc import ABC, abstractmethod
from submit_prompt_request_body import SubmitPromptRequestBody
from submit_prompt_response_body import SubmitPromptResponseBody

class ApiInterface(ABC):
    
    """Handler method for the POST /submit endpoint, formerly known as /koda
    
    This method will respond to a prompt from the LLM client
    """
    @abstractmethod
    def submitPrompt(self, submitPromptRequestBody: SubmitPromptRequestBody) -> SubmitPromptResponseBody:
        pass
    
    """Handler method for the GET /reset/{sessionId} endpoint
    
    This method will deactivate the session-id that the client sends as a path parameter, 
    and respond with a newly generated and activated session-id
    """
    @abstractmethod
    def resetSession(self, sessionId: str) -> str:
        pass