
from api_interface import ApiInterface
from submit_request_body import SubmitRequestBody
from submit_response_body import SubmitResponseBody, InputData, Beer

class ApiImplementation(ApiInterface):
    def submit(self, data: SubmitRequestBody) -> SubmitResponseBody:
        return SubmitResponseBody(            
            content="Here is my recommendation",
            input_data=InputData(
                beers=[
                    Beer(name="A Good Beer"), 
                    Beer(name="Another Good Beer")
                    ]
            ),
            rec=["beer_id_1", "beer_id_2", "beer_id_3"]
        )