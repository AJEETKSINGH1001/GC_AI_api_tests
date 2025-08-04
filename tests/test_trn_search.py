import requests

def test_valid_trn_lookup():
    url = "https://online-validation-demo-uae.gamechange.dev/api/trn/search"
    payload = {"trn": "100056880600003"}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "PostmanRuntime/7.35.0",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6InRTam50NVVzYTVkbkpFRXVHLUhpN1EiLCJ0eXAiOiJhdCtKV1QifQ.eyJjbGllbnRfaWQiOiJnYy1pbnRlcm5hbCIsImlzcyI6Imh0dHBzOi8vbmJvYXJkLWF1dGgtcWEuZ2FtZWNoYW5nZS5kZXYiLCJhdWQiOiJodHRwczovL25ib2FyZC1hdXRoLXFhLmdhbWVjaGFuZ2UuZGV2IiwianRpIjoiZGVkMTY0ZjItYTRkYy00MDhmLTgyNDEtYWU1MTY4MWQzM2MyIiwic3ViIjoiY2xpZW50OmdjLWludGVybmFsIiwiZXhwIjoxNzU0MzY1MDg0LCJpYXQiOjE3NTQyNzg2ODR9.QXx-3qKYyv9TSDbcwuHYPyJNsUoGIEiklvD2KFCqFxoIO__OPiVrtdleHPlX8fCDf1WtSQ3U841I324KLlEu53wH6VIQZrH_Lvp7eocHhZgZP1XzSR2KJxS1Y02SSXhOVZn3Vexx8JDg6dvf4v17CePQD-j1_enmDCtAqCwYcQUeYwLl8b83uP2JhJ--1uA5bbOZ8JLlaWz0VhECNz2gQ6gbJJQ47Jwklt90ldS9Lyr5j4lYBK8PimbvFh79jkE33orTd6JER8MmSPS6e9qUsIzeUY79W2rIz6Ym1OOnTH9MuEX-T9LZOg_lZtxMyzvD5Kguf0aRiXZ_URmdjmK4lg"  # <-- Replace this
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
    except requests.exceptions.RequestException as e:
        assert False, f"❌ Request failed: {e}"

    assert response.status_code == 200, f"❌ Status code not 200: {response.status_code}, {response.text}"

    try:
        data = response.json()
    except ValueError:
        assert False, f"❌ Response not JSON: {response.text}"

    assert data.get("trn") == "100056880600003", f"❌ TRN mismatch: {data}"
    assert data.get("name") == "GLOBUS SOLUTIONS DMCC", f"❌ Name mismatch: {data}"
