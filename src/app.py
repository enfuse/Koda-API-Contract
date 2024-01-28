import uuid
from api_implementation import ApiImplementation
from api_interface import (ChatHistory, Message)

if __name__ == "__main__":
    api: ApiImplementation = ApiImplementation()
    
    print("\nPOST /submit")
    message = Message(
        content="Recommend me a good beer",
        sessionId="9238457"
    )
    print(f"Message: {message}")
    submitPromptResponseBody = api.submit(message)
    print(f"Submit Response Body: {submitPromptResponseBody}")
    
    print("\nGET /reset/{sessionId}")
    sessionIdToReset = uuid.uuid4().hex
    print(f"Session Id to Reset: {sessionIdToReset}")
    newSessionId = api.reset_session(sessionIdToReset)
    print(f"New Session ID: {newSessionId}")
    
    print ("\nGET /load_convo/{convo_id}")
    conversationId = uuid.uuid4().hex
    print(f"Conversation ID: {conversationId}")
    loadConversationReturn = api.load_conversation(conversationId)
    print(f"Load Conversation returned: {loadConversationReturn}")
    
    print ("\nPOST /edit")
    sessionToEdit = uuid.uuid4().hex;
    print(f"Session to edit: {sessionToEdit}")
    chatHistory = ChatHistory(
        sessionID = uuid.uuid4().hex,
        messages = [
            Message(
                content="Recommend me a good beer",
                sessionId=sessionToEdit
            ),
            Message(
                content="This drink is good. Another!",
                sessionId=sessionToEdit
            ),
            Message(
                content="Message from a different session",
                sessionId=uuid.uuid4().hex
            )
        ]
    )
    print(f"Chat history: {chatHistory}")
    response = api.edit(chatHistory)
    print(f"response: {response}")

    
    
