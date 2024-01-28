
import uuid

from fastapi.responses import StreamingResponse

from api_interface import (
    ApiInterface,
    SubmitResponseBody,
    InputData,
    Beer,
    ChatHistory,
    Message)

class ApiImplementation(ApiInterface):
    
    def submit(self, message: Message) -> SubmitResponseBody:
        return SubmitResponseBody(
            content="Here is my recommendation",
            inputData=InputData(
                beers=[
                    Beer(name="A Good Beer"), 
                    Beer(name="Another Good Beer")
                    ]
            ),
            rec=["beer_id_1", "beer_id_2", "beer_id_3"]
        )
        
    def reset_session(self, session_id: str) -> str:
        return uuid.uuid4().hex
    
    def load_conversation(self, conversation_id: str) -> bool:
        return True
    
    def edit(self, chat_history: ChatHistory) -> StreamingResponse:
        data = "{}"
        return StreamingResponse(content=data, media_type="application/json")