from utils.api_client import APIClient

def test_token_generation():
    client = APIClient()
    token = client.token
    assert token is not None
    assert isinstance(token, str)
