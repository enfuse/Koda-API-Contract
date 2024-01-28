
import uuid

from api_interface import ApiInterface
from submit_prompt_request_body import SubmitPromptRequestBody
from submit_prompt_response_body import SubmitPromptResponseBody, InputData, Beer

class ApiImplementation(ApiInterface):
    
    def submitPrompt(self, submitPromptRequestBody: SubmitPromptRequestBody) -> SubmitPromptResponseBody:
        return SubmitPromptResponseBody(            
            content="Here is my recommendation",
            input_data=InputData(
                beers=[
                    Beer(name="A Good Beer"), 
                    Beer(name="Another Good Beer")
                    ]
            ),
            rec=["beer_id_1", "beer_id_2", "beer_id_3"]
        )
        
    def resetSession(self, sessionId: str) -> str:
        return uuid.uuid4().hex;
    
    def loadConversation(self, conversationId: str) -> bool: 
        return True