from utils.api_client import APIClient

def test_get_status():
    client = APIClient()
    response = client.get("/api/oauth2/token")  # Adjust endpoint to your API
    assert response.status_code == 200
    assert "status" in response.json()
