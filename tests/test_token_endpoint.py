import pytest
import requests
import time
from config import config

BASE_URL = config.BASE_URL + "/api/oauth2/token"
HEADERS = {"Content-Type": "application/json"}

# 👇 Fixture to add delay between test cases
@pytest.fixture(autouse=True)
def wait_between_tests():
    time.sleep(5)  # wait 1 second before each test

# ✅ Positive case
def test_valid_credentials():
    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data.get("token_type") == "Bearer"
    assert isinstance(data.get("expires_in"), int)

# ❌ Missing fields
def test_missing_client_id():
    payload = {
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code in [400, 401]

def test_missing_client_secret():
    payload = {
        "client_id": config.CLIENT_ID,
        "grant_type": "client_credentials"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code in [400, 401]

def test_missing_grant_type():
    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 400

# ❌ Invalid credentials
def test_invalid_client_id():
    payload = {
        "client_id": "wrong-id",
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 401

def test_invalid_client_secret():
    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": "wrong-secret",
        "grant_type": "client_credentials"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 401

# ❌ Invalid grant type
def test_invalid_grant_type():
    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "password"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 400

# ❌ Empty body
def test_empty_body():
    response = requests.post(BASE_URL, headers=HEADERS, json={})
    assert response.status_code == 400

# ❌ Wrong content-type
def test_wrong_content_type():
    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    wrong_headers = {"Content-Type": "text/plain"}
    response = requests.post(BASE_URL, headers=wrong_headers, json=payload)
    assert response.status_code in [400, 415]

# ❌ Wrong method
def test_get_method_not_allowed():
    response = requests.get(BASE_URL)
    assert response.status_code == 405
