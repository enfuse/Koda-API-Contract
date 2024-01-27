
from api_interface import ApiInterface
from submit_request_body import SubmitRequestBody
from submit_response_body import SubmitResponseBody

class ApiImplementation(ApiInterface):
    def submit(self, data: SubmitRequestBody) -> SubmitResponseBody:
        print("SubmitRequestBody: ", data)
        response_body = SubmitResponseBody(content="Response Content", beers=[])
        print("SubmitResponseBody: ", response_body)
        return response_body    