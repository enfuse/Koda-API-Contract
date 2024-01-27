from src.contract.api_implementation import ApiImplementation

print('running app')

if __name__ == "__main__":
    implementation = ApiImplementation()
    implementation.submit("Example Data")
