import requests

def test_valid_trn_lookup():
    url = "https://online-validation-demo-uae.gamechange.dev/api/trn/search"
    payload = {"trn": "100056880600003"}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "PostmanRuntime/7.35.0",
        "Authorization": "Bearer test"  # <-- Replace this
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
