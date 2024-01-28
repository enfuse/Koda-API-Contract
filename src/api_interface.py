from abc import ABC, abstractmethod
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional, List

class Message(BaseModel):

    """
    User Input

    Example:
    "Recommend me a good beer"
    """
    content: str

    """
    Random or hardcoded ID
    
    Example:
    1616221
    """
    sessionID: Optional[str] = None

    """
    Doesn't actually get passed in - defaults to "user"
    """
    role: str = "user"


class ChatHistory(BaseModel):
    messages: List[Message]
    """
    Random or hardcoded ID
    
    Example:
    1616221
    """
    sessionID: str

class Beer(BaseModel):
    """
    Name of a beer that may or may not match any IDs or beers mentioned in 'content'.
    Used as a fallback in case there are no valid recommendations in recs.

    Example:
    "A Good Beer"
    """
    name: str

class InputData(BaseModel):
    beers: List[Beer]

"""Defines the response body for the /submit endpoint"""
class SubmitResponseBody(BaseModel):
    """
    Text for Koda to speak out loud

    Example:
    "Here is my recommendation"
    """
    content: str

    inputData: InputData

    """
    Beer Recommendations
    
    Multiple beer IDs can be returned. 
    They may or may not match any of the beers mentioned in 'content'.
    
    Navigate to the first one that matches a beer name mentioned in 'content', if any.
    If not, navigate to the first one.
    
    Example:
    "beer_id_1", 
    "beer_id_2",
    "beer_id_2"
    """
    rec: List[str]

class ApiInterface(ABC):
    
    """Handler method for the POST /submit endpoint, formerly known as /koda
    
    This method will respond to a prompt from the LLM client
    """
    @abstractmethod
    def submit(self, message: Message) -> SubmitResponseBody:
        pass
    
    """Handler method for the GET /reset/{session_id} endpoint
    
    This method will deactivate the session-id that the client sends as a path parameter, 
    and respond with a newly generated and activated session-id
    """
    @abstractmethod
    def reset_session(self, session_id: str) -> str:
        pass
    
    """Handler method for the GET /loadconvo/{convo_id} endpoint
    
    This method will lookup a conversation in the database and load it into the LLM
    """
    @abstractmethod
    def load_conversation(self, conversation_id: str) -> bool:
        pass
    
    """Handler method for the POST /edit endpoint
    
    This method will edit the provided chat history for a given session-id
    """
    @abstractmethod
    def edit(self, chat_history: ChatHistory) -> StreamingResponse:
        pass