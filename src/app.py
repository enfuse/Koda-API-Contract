from api_implementation import ApiImplementation
from submit_request_body import SubmitRequestBody

print('running app')

if __name__ == "__main__":
    api = ApiImplementation()
    
    submitRequestBody = SubmitRequestBody(
        content="Here is my recommendation",
        input_data={"beers": [{"name": "A Good Beer"}]},
        rec=["beer_id_1", "beer_id_2", "beer_id_3"]
    )

    api.submit('{"content", "my rec"}')
