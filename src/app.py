from api_implementation import ApiImplementation
from submit_request_body import SubmitRequestBody

print('running app')

if __name__ == "__main__":
    api = ApiImplementation()
    
    submitRequestBody = SubmitRequestBody(
        content="Recommend me a good beer",
        sessionId=9238457
    )
    
    print(f"Submit Request Body: {submitRequestBody}")

    submitResponseBody = api.submitPrompt(submitRequestBody)
    
    print(f"Submit Response Body: {submitResponseBody}")
