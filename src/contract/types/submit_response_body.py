from typing import TypedDict, List

"""
Defines the response body for the /submit endpoint
"""

class Beer(TypedDict):
    """
    Name of a beer that may or may not match any IDs or beers mentioned in 'content'.
    
    Example:
    "A Good Beer"
    """
    name: str
    
class InputData(TypedDict):
    """
    Used as a fallback in case there are no valid recommendations in recs.
    """
    beers: List[Beer]

class SubmitResponseBody(TypedDict):
    """
    Text for Koda to speak out loud
    
    Example:
    "Here is my recommendation"
    """
    content: str
    
    inputData: InputData
    
