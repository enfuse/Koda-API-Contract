from api_implementation import ApiImplementation
from submit_prompt_request_body import SubmitPromptRequestBody

print('running app')

if __name__ == "__main__":
    api = ApiImplementation()
    
    submitPromptRequestBody = SubmitPromptRequestBody(
        content="Recommend me a good beer",
        sessionId=9238457
    )
    
    print(f"Submit Request Body: {submitPromptRequestBody}")

    submitPromptResponseBody = api.submitPrompt(submitPromptRequestBody)
    
    print(f"Submit Response Body: {submitPromptResponseBody}")
