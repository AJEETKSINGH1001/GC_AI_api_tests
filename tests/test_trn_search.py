import requests

def test_valid_trn_lookup():
    url = "https://online-validation-demo-uae.gamechange.dev/api/trn/search"
    payload = {"trn": "100056880600003"}
    headers = {"Content-Type": "application/json"}

    # Send request with 60 seconds timeout
    response = requests.post(url, json=payload, headers=headers, timeout=60)

    # Check HTTP status
    assert response.status_code == 200, f"❌ Status code is not 200: {response.status_code}"

    # Parse and validate response JSON
    data = response.json()
    assert "trn" in data and data["trn"] == "100056880600003", "❌ TRN mismatch or missing"
    assert "name" in data and data["name"] == "GLOBUS SOLUTIONS DMCC", "❌ Name mismatch or missing"
