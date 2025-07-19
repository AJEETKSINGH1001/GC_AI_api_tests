import os

import requests
from config import config

class APIClient:
    def __init__(self):
        self.base_url = config.BASE_URL
        self.parser_url = config.PARSER_BASE_URL
        self.token = self.get_token()

    def get_token(self):
        url = f"{self.base_url}/api/oauth2/token"
        headers = {'Content-Type': 'application/json'}
        payload = {
            'grant_type': 'client_credentials',
            'client_id': config.CLIENT_ID,
            'client_secret': config.CLIENT_SECRET
        }

        response = requests.post(url, headers=headers, json=payload)
        print(f"Token response status: {response.status_code}")
        print(f"Token response body: {response.text}")
        response.raise_for_status()
        return response.json()["access_token"]
    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.get_headers(), params=params)

    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, headers=self.get_headers(), json=json)

    def post_file(self, endpoint, file_path, field_name="file", extra_fields=None, timeout=90):
        """
        Upload a file with optional form-data and custom timeout.
        """
        url = f"{self.parser_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}

        with open(file_path, "rb") as f:
            files = {
                field_name: (os.path.basename(file_path), f, "application/pdf")
            }

            if extra_fields:
                for key, value in extra_fields.items():
                    files[key] = (None, value)

            response = requests.post(url, headers=headers, files=files, timeout=timeout)

        return response

