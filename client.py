import requests


class MakeCall:
    def __init__(self, endpoint, auth=None, headers=None):
        self.endpoint = endpoint
        self.auth = auth
        self.headers = headers

    def make_get(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        return response.json()


call = MakeCall(endpoint='http://127.0.0.1:8000/api/products/')
print(call.make_get())