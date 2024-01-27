from typing import TypedDict

"""Defines the request body for the /submit endpoint"""
class SubmitPromptRequestBody(TypedDict):
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
    sessionId: int
    
    """
    Doesn't actually get passed in - defaults to "user"
    """
    role: str = "user"
