from typing import TypedDict, List

"""
Defines the response body for the /submit endpoint
"""

class Beer(TypedDict):
    """
    Name of a beer that may or may not match any IDs or beers mentioned in 'content'.
    Used as a fallback in case there are no valid recommendations in recs.
    
    Example:
    "A Good Beer"
    """
    name: str
    
class InputData(TypedDict):
    beers: List[Beer]

class SubmitResponseBody(TypedDict):
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
    
