import os
import requests
from utils.api_client import APIClient

def test_trade_license_extract_Abu_Dhabi():
    client = APIClient()
    file_path = os.path.join(os.path.dirname(__file__), "Abudhabi-Business-Center.pdf")

    # Additional form-data fields
    extra_fields = {
        "issuingAuthority": "Abu Dhabi Department of Economic Development",
        "validateWithApi": "true"
    }

    try:
        # Call API with extended timeout
        response = client.post_file(
            endpoint="/api/trade-license/extract",
            file_path=file_path,
            extra_fields=extra_fields,
            timeout=90  # seconds
        )
    except requests.exceptions.Timeout:
        assert False, "❌ API request timed out after 90 seconds"

    # Assertions
    assert response.status_code == 200, f"❌ Failed: {response.status_code}, {response.text}"

    data = response.json()
    assert "apiStatus" in data, "❌ 'apiStatus' key missing in response"
    assert data["apiStatus"] == "VERIFIED", f"❌ Expected 'VERIFIED', got: {data['apiStatus']}"
