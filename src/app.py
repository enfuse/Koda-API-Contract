import uuid

from api_implementation import ApiImplementation
from submit_prompt_request_body import SubmitPromptRequestBody


if __name__ == "__main__":
    api = ApiImplementation()
    
    print("\nPOST /submit")
    submitPromptRequestBody = SubmitPromptRequestBody(
        content="Recommend me a good beer",
        sessionId=9238457
    )
    print(f"Submit Request Body: {submitPromptRequestBody}")
    submitPromptResponseBody = api.submitPrompt(submitPromptRequestBody)
    print(f"Submit Response Body: {submitPromptResponseBody}")
    
    print("\nGET /reset/{sessionId}")
    sessionIdToReset = uuid.uuid4().hex
    print(f"Session Id to Reset: {sessionIdToReset}")
    newSessionId = api.resetSession(sessionIdToReset)
    print(f"New Session ID: {newSessionId}")
    
    print ("\nGET /load_convo/{convo_id}")
    conversationId = uuid.uuid4().hex
    print(f"Conversation ID: {conversationId}")
    loadConversationReturn = api.loadConversation(conversationId)
    print(f"Load Conversation returned: {loadConversationReturn}")
