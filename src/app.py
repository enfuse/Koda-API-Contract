import uuid

from api_implementation import ApiImplementation
from submit_prompt_request_body import SubmitPromptRequestBody

print('\nDemo implementations of the LLM API handler methods')

if __name__ == "__main__":
    api = ApiImplementation()
    
    print("\nDemo the POST /submit handler method")
    submitPromptRequestBody = SubmitPromptRequestBody(
        content="Recommend me a good beer",
        sessionId=9238457
    )
    print(f"Submit Request Body: {submitPromptRequestBody}")
    submitPromptResponseBody = api.submitPrompt(submitPromptRequestBody)
    print(f"Submit Response Body: {submitPromptResponseBody}")
    
    print("\nDemo the /reset/{sessionId} handler method")
    sessionIdToReset = uuid.uuid4().hex;
    print(f"Session Id to Reset: {sessionIdToReset}")
    newSessionId = api.resetSession(sessionIdToReset)
    print(f"New Session ID: {newSessionId}")
