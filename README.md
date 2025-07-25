Here's a professional and comprehensive `README.md` for your GitHub repository that covers:

* Overview of the API test suite
* Setup instructions
* Running tests with Allure
* Directory structure
* Sample commands
* Troubleshooting tips

---

### ✅ `README.md`

```markdown
# UAE API Automation Test Suite

This repository contains automated tests for validating various UAE government APIs, including:

- OAuth2 Token Authentication
- Trade License Extraction (Ajman, UAQ, Ras Al Khaimah)
- TRN (Tax Registration Number) Lookup

The test suite is built using `pytest` and supports HTML and Allure reports for detailed insights.

---

## 📁 Project Structure

```

rak\_wbg\_api\_tests/
│
├── tests/                         # Test cases organized by API
│   ├── test\_token\_endpoint.py    # OAuth2 token tests
│   ├── test\_trade\_license.py     # Trade license extraction tests
│   ├── test\_trn\_search\_api.py    # TRN search test
│
├── utils/
│   └── api\_client.py             # Custom API client for requests
│
├── allure-results/               # Auto-generated Allure result files
├── report.html                   # HTML report generated by pytest-html
├── requirements.txt              # Python dependencies
└── README.md

````

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-org/uae-api-tests.git
cd uae-api-tests
````

### 2. Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ✅ Running the Tests

### Basic run with HTML report:

```bash
pytest --html=report.html --self-contained-html
```

### With Allure reporting:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

> Make sure Allure CLI is installed and available in your system path.
> [Download Allure CLI from GitHub](https://github.com/allure-framework/allure2/releases)

---

## ⏱️ Specific Tests with Delay

Some tests (e.g., Trade License) include a wait time of 1 minute for API readiness:

```bash
pytest tests/test_trade_license.py
```

---

## 🧪 Sample Tests Included

* ✅ `POST /api/oauth2/token` — Token validation with positive & negative scenarios
* ✅ `POST /api/trade-license/extract` — Trade license extraction for Ajman, UAQ, and RAK
* ✅ `POST /api/trn/search` — Lookup by TRN with expected company name

---

## 📊 Reports

### HTML (pytest-html)

Located at: `report.html`
Open in any browser.

### Allure Report

Launch in browser using:

```bash
allure serve allure-results
```

---

## ❗ Troubleshooting

| Issue                    | Fix                                             |
| ------------------------ | ----------------------------------------------- |
| `0 test cases` in Allure | Run pytest with `--alluredir=allure-results`    |
| `allure` not found       | Ensure Allure CLI is installed & in system PATH |
| HTML report not styled   | Use `--self-contained-html` flag                |

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Contributors

* Ajeet K Singh

---

```

Let me know if you'd like to include badges (e.g., build passing, license) or CI/CD instructions for GitHub Actions or Jenkins integration.
```
