import os
import requests
from utils.api_client import APIClient

def test_trade_license_extract_Ras_Al_Khaimah():
    client = APIClient()
    file_path = os.path.join(os.path.dirname(__file__), "TL-Rak-EZ.pdf")

    # Additional form-data fields
    extra_fields = {
        "issuingAuthority": "Ras Al Khaimah Economic Zone (RAKEZ)",
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
