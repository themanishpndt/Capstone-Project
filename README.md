# Capstone Project — AutomationExercise Test Automation Framework

A robust, end-to-end **Selenium WebDriver + Pytest** automation framework that exercises the public demo site
[AutomationExercise.com](https://automationexercise.com) using the **Page Object Model (POM)** design pattern.

The framework automates the official 26-test-case "capstone" suite (register, login, search, cart, checkout,
payment, subscription, categories, brands, reviews, scroll, invoice download, etc.) and produces rich
**Allure** and **HTML** reports with automatic screenshots and browser logs on failure.

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [Tech Stack](#-tech-stack)
4. [Project Structure](#-project-structure)
5. [Test Coverage (TC01 – TC26)](#-test-coverage-tc01--tc26)
6. [Prerequisites](#-prerequisites)
7. [Installation & Setup](#-installation--setup)
8. [Configuration](#-configuration)
9. [Running the Tests](#-running-the-tests)
10. [Reports & Artifacts](#-reports--artifacts)
11. [Page Object Model (POM)](#-page-object-model-pom)
12. [Markers / Test Categorization](#-markers--test-categorization)
13. [Custom Fixtures](#-custom-fixtures)
14. [Test Data](#-test-data)
15. [Troubleshooting](#-troubleshooting)
16. [Author](#-author)

---

## 🚀 Project Overview

| Item | Value |
|---|---|
| **Application under test** | [https://automationexercise.com](https://automationexercise.com) |
| **Framework** | Selenium 4 + Pytest 7 |
| **Design Pattern** | Page Object Model (POM) |
| **Languages / Versions** | Python 3.12 |
| **Supported Browsers** | Chrome, Brave, Firefox, Edge (headless optional) |
| **Reporting** | Allure + pytest-html |
| **Repository** | [Capstone-Project](https://github.com/themanishpndt/Capstone-Project) |

---

## ✨ Features

- **Page Object Model** — clean separation of locators, page actions, and tests.
- **Multi-browser support** — Chrome, Brave, Firefox, Edge via `webdriver-manager`.
- **Data-driven testing** — CSV / JSON fixtures under `test_data/`.
- **Robust waits** — implicit + explicit waits (Selenium `WebDriverWait`).
- **Auto screenshots** on test failure (saved + attached to Allure).
- **Browser console logs** captured and attached to Allure on every test.
- **Allure environment** auto-generated (`environment.properties`).
- **HTML report** with `--self-contained-html`.
- **Parallel execution** ready via `pytest-xdist` (`-n auto`).
- **Action-delay fixture** for human-friendly playback during demos.
- **Hardened click helper** that falls back from native click to JavaScript click when intercepted.
- **Ad-frame hiding** logic to keep Google ad iframes from blocking test clicks.

---

## 🧰 Tech Stack

| Layer | Tool |
|---|---|
| Browser Automation | Selenium WebDriver 4.15 |
| Driver Management | webdriver-manager 4.0 |
| Test Runner | Pytest 7.4 |
| Parallelization | pytest-xdist 3.5 |
| HTML Report | pytest-html 4.1 |
| Coverage | pytest-cov 4.1 |
| Timeout | pytest-timeout 2.2 |
| Reporting | allure-pytest 2.13 |
| Fake Data | Faker 21 |
| HTTP / API | requests 2.31 |
| Env Mgmt | python-dotenv 1.0 |
| Logging | colorlog 6.8 |
| Code Quality | black 23, flake8 6, pylint 3 |

---

## 🗂 Project Structure

```text
Capstone-Project/
│
├── conftest.py                 # Global pytest fixtures & hooks
├── pytest.ini                  # Pytest config, markers, addopts
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── .env                        # Local environment variables (NOT committed)
│
├── config/
│   ├── __init__.py
│   └── config.py               # Config + URLs class (loads from .env)
│
├── src/                        # Application-under-test code (framework code)
│   ├── __init__.py
│   ├── pages/                  # Page Object Model classes
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   ├── login_page.py
│   │   ├── product_page.py
│   │   ├── cart_page.py
│   │   ├── checkout_page.py
│   │   ├── contact_page.py
│   │   ├── category_page.py
│   │   ├── brand_page.py
│   │   ├── review_page.py
│   │   ├── scroll_page.py
│   │   ├── subscription_page.py
│   │   ├── invoice_page.py
│   │   └── automation_exercise_page.py   # High-level unified page object
│   │
│   ├── locators/               # Centralized XPath / CSS locators
│   │   ├── common_locators.py
│   │   ├── home_locators.py
│   │   ├── login_locators.py
│   │   ├── cart_locators.py
│   │   ├── checkout_locators.py
│   │   ├── product_locators.py
│   │   ├── contact_locators.py
│   │   ├── category_locators.py
│   │   ├── brand_locators.py
│   │   ├── review_locators.py
│   │   ├── scroll_locators.py
│   │   ├── subscription_locators.py
│   │   └── invoice_locators.py
│   │
│   ├── drivers/
│   │   └── __init__.py         # (Reserved for future driver factory)
│   │
│   └── utils/                  # Helpers: logging, waits, screenshots
│       ├── logger_utils.py
│       ├── wait_utils.py
│       └── screenshot_utils.py
│
├── tests/                      # Test suite (official TC01–TC26)
│   ├── __init__.py
│   ├── helpers.py              # Shared helpers (user builder, login flow)
│   ├── DEMO_framework_demo.py  # Sanity tests to verify framework
│   ├── tc01_register_user.py
│   ├── tc02_login_correct.py
│   ├── tc03_login_incorrect.py
│   ├── tc04_logout.py
│   ├── tc05_register_existing_email.py
│   ├── tc06_contact_us.py
│   ├── tc07_test_cases_page.py
│   ├── tc08_product_browse.py
│   ├── tc09_product_search.py
│   ├── tc10_home_subscription.py
│   ├── tc11_cart_subscription.py
│   ├── tc12_shopping_cart.py
│   ├── tc13_product_quantity.py
│   ├── tc14_place_order_register_checkout.py
│   ├── tc15_place_order_register_before_checkout.py
│   ├── tc16_place_order_login_before_checkout.py
│   ├── tc17_remove_products_from_cart.py
│   ├── tc18_view_category_products.py
│   ├── tc19_view_cart_brand_products.py
│   ├── tc20_search_products_verify_cart_after_login.py
│   ├── tc21_add_review_on_product.py
│   ├── tc22_add_to_cart_from_recommended_items.py
│   ├── tc23_verify_address_details_in_checkout_page.py
│   ├── tc24_download_invoice_after_purchase_order.py
│   ├── tc25_verify_scroll_up_using_arrow_button.py
│   └── tc26_verify_scroll_up_without_arrow_button.py
│
├── test_data/                  # Data-driven test inputs
│   ├── valid_users.csv
│   ├── invalid_credentials.csv
│   ├── products.json
│   └── contact_upload.txt
│
├── reports/                    # Auto-generated outputs (gitignored)
│   ├── logs/                   # test.log
│   ├── screenshots/            # On-failure screenshots
│   ├── allure-results/         # Allure raw data
│   └── test-report.html        # HTML report
│
└── .venv/                      # Local virtual environment
```

---

## ✅ Test Coverage (TC01 – TC26)

The framework implements the **official AutomationExercise 26-step capstone suite**:

| # | Test Case | File |
|---|---|---|
| 1 | Register User | `tc01_register_user.py` |
| 2 | Login User with correct email and password | `tc02_login_correct.py` |
| 3 | Login User with incorrect email and password | `tc03_login_incorrect.py` |
| 4 | Logout User | `tc04_logout.py` |
| 5 | Register User with existing email | `tc05_register_existing_email.py` |
| 6 | Contact Us Form | `tc06_contact_us.py` |
| 7 | Verify Test Cases Page | `tc07_test_cases_page.py` |
| 8 | Verify All Products and Product Detail Page | `tc08_product_browse.py` |
| 9 | Search Product | `tc09_product_search.py` |
| 10 | Verify Subscription in Home Page | `tc10_home_subscription.py` |
| 11 | Verify Subscription in Cart Page | `tc11_cart_subscription.py` |
| 12 | Add Products in Cart | `tc12_shopping_cart.py` |
| 13 | Verify Product Quantity in Cart | `tc13_product_quantity.py` |
| 14 | Place Order: Register while Checkout | `tc14_place_order_register_checkout.py` |
| 15 | Place Order: Register before Checkout | `tc15_place_order_register_before_checkout.py` |
| 16 | Place Order: Login before Checkout | `tc16_place_order_login_before_checkout.py` |
| 17 | Remove Products From Cart | `tc17_remove_products_from_cart.py` |
| 18 | View Category Products | `tc18_view_category_products.py` |
| 19 | View & Cart Brand Products | `tc19_view_cart_brand_products.py` |
| 20 | Search Products and Verify Cart After Login | `tc20_search_products_verify_cart_after_login.py` |
| 21 | Add Review on Product | `tc21_add_review_on_product.py` |
| 22 | Add to Cart from Recommended Items | `tc22_add_to_cart_from_recommended_items.py` |
| 23 | Verify Address Details in Checkout Page | `tc23_verify_address_details_in_checkout_page.py` |
| 24 | Download Invoice after Purchase Order | `tc24_download_invoice_after_purchase_order.py` |
| 25 | Verify Scroll Up using 'Arrow' Button | `tc25_verify_scroll_up_using_arrow_button.py` |
| 26 | Verify Scroll Up without 'Arrow' Button | `tc26_verify_scroll_up_without_arrow_button.py` |

---

## ⚙ Prerequisites

- **Python 3.10+** (developed on Python 3.12)
- **Git**
- One or more of the following browsers installed:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - Brave (optional, path configurable in `.env`)
- **Allure Command-Line** (optional, for serving reports):
  ```bash
  # Windows (Scoop)
  scoop install allure
  # Or via npm
  npm install -g allure-commandline
  ```

---

## 🛠 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/themanishpndt/Capstone-Project.git
cd Capstone-Project
```

### 2. Create & activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. (Optional) Configure environment variables
Create a `.env` file in the project root (already gitignored):
```ini
# Browser
BROWSER=chrome
HEADLESS=False

# Target site
BASE_URL=https://automationexercise.com

# Waits (seconds)
IMPLICIT_WAIT=15
EXPLICIT_WAIT=25
PAGE_LOAD_TIMEOUT=40
ACTION_DELAY=0

# Download directory (for invoice test)
DOWNLOAD_DIR=reports/downloads

# Brave (optional)
BRAVE_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe

# Page load strategy
PAGE_LOAD_STRATEGY=eager
```

---

## ▶ Running the Tests

### Run the full suite (Chrome by default)
```bash
pytest
```

### Run a specific test
```bash
pytest tests/tc01_register_user.py
```

### Run a single test method
```bash
pytest tests/tc18_view_category_products.py::TestViewCategoryProductsTC18::test_view_category_products
```

### Run with a different browser
```bash
pytest --browser=firefox
pytest --browser=edge
pytest --browser=brave
```

### Run in headless mode
```bash
pytest --headless
```

### Run only smoke tests
```bash
pytest -m smoke
```

### Run only critical tests
```bash
pytest -m critical
```

### Run in parallel (auto-detect CPU cores)
```bash
pytest -n auto
```

### Run smoke + critical only in parallel
```bash
pytest -m "smoke or critical" -n auto
```

### Run against a different base URL
```bash
pytest --base_url=https://staging.automationexercise.com
```

---

## 📊 Reports & Artifacts

After a run, artifacts are written under `reports/`:

| Path | Description |
|---|---|
| `reports/logs/test.log` | Plain-text execution log (root logger) |
| `reports/screenshots/*.png` | Screenshots taken **on every test failure** |
| `reports/allure-results/` | Allure raw results (JSON + attachments) |
| `reports/test-report.html` | Self-contained HTML report |
| `reports/downloads/` | Invoice downloads (TC24) |

### View the HTML report
Just open the file:
```bash
# Windows
start reports\test-report.html
```

### View the Allure report
```bash
# 1. Generate the static site
allure generate reports/allure-results -o reports/allure-report --clean

# 2. Open it in your browser
allure open reports/allure-report
```
Or in one shot:
```bash
allure serve reports/allure-results
```

---

## 🧱 Page Object Model (POM)

The framework follows a strict 3-layer POM:

```
┌──────────────────────────┐
│      tests/ (TC01…)      │   ← high-level test intent
└────────────┬─────────────┘
             │ uses
             ▼
┌──────────────────────────┐
│  src/pages/*.py          │   ← actions & flows (e.g. login(), add_to_cart())
└────────────┬─────────────┘
             │ uses
             ▼
┌──────────────────────────┐
│  src/locators/*.py       │   ← XPath / CSS selectors only
└──────────────────────────┘
```

- `BasePage` provides shared helpers: `find_element`, `click_element`, `enter_text`,
  `is_element_visible`, `navigate_to`, `get_text`, etc.
- `AutomationExercisePage` is a higher-level page object that consolidates cross-page flows
  (signup, register, search, add-to-cart, checkout, payment, invoice download) for the
  **official TC** suite.
- Locators are kept in dedicated `*_locators.py` modules so they can be updated in one place.

---

## 🏷 Markers / Test Categorization

Defined in `pytest.ini`:

| Marker | Purpose |
|---|---|
| `smoke` | Critical path sanity tests |
| `regression` | Full regression coverage |
| `critical` | Must-pass tests for releases |
| `ui` | UI interaction tests |
| `api` | API tests |
| `functional` | Functional tests |
| `end_to_end` | Full workflow tests |
| `parametrize` | Parameterized tests |
| `slow` | Tests that take longer than usual |
| `unit` | Unit-level tests |
| `integration` | Integration tests |
| `official` | Official AutomationExercise capstone cases |

**Usage:**
```bash
pytest -m "smoke and not slow"
pytest -m "official and critical"
```

---

## 🧪 Custom Fixtures (defined in `conftest.py`)

| Fixture | Scope | Description |
|---|---|---|
| `base_url` | session | Returns the configured base URL (auto-upgrades `http://` → `https://`) |
| `driver` | function | Initializes a fresh WebDriver (chrome/brave/firefox/edge) with safe defaults and tear-down `quit()` |
| `wait` | function | A `WebDriverWait` instance with `EXPLICIT_WAIT` timeout |
| `action_delay` | function | Helper `action_delay(seconds)` to slow down actions for visibility |
| `auto_action_delay` | function (autouse) | Adds configurable delay between tests |
| `test_data` | function | Dictionary of common test data (emails, password, name, etc.) |
| `log_test_start_end` | session (autouse) | Logs banner at suite start/end |
| `setup_allure_environment` | session (autouse) | Placeholder for Allure env metadata |

CLI options (added by `pytest_addoption`):

| Flag | Default | Description |
|---|---|---|
| `--browser` | `chrome` | `chrome`, `brave`, `firefox`, or `edge` |
| `--headless` | `False` | Run browser in headless mode |
| `--base_url` | `https://automationexercise.com` | Base URL override |

**Hooks:**
- `pytest_runtest_makereport` — captures screenshots on failure and attaches them + browser logs to Allure.
- `pytest_configure` — writes `reports/allure-results/environment.properties`.
- `pytest_collection_modifyitems` — adds default `functional` marker and Allure dynamic IDs.

---

## 📂 Test Data

| File | Purpose |
|---|---|
| `test_data/valid_users.csv` | Valid email/password/name combinations |
| `test_data/invalid_credentials.csv` | Negative login scenarios (empty, weak, SQL injection) |
| `test_data/products.json` | Sample product catalog data |
| `test_data/contact_upload.txt` | File uploaded by the TC06 contact form test |
| `test_data/__init__.py` | Marks directory as importable package |

---

## 🛠 Troubleshooting

| Issue | Solution |
|---|---|
| **`SessionNotCreatedException` / driver version mismatch** | `webdriver-manager` downloads matching drivers automatically. Ensure you have write permission in the project directory. |
| **Click intercepted by Google ads** | The framework hides `iframe[id^='aswift']` and `ins.adsbygoogle` before each click. If a new ad format appears, update `_hide_ad_frames()` in `automation_exercise_page.py`. |
| **`ElementClickInterceptedException` persists** | Increase `EXPLICIT_WAIT` / `IMPLICIT_WAIT` in `.env`. The `BasePage.click_element` already falls back to JS-click. |
| **Timeouts on slow networks** | Bump `PAGE_LOAD_TIMEOUT` in `.env` (default 40s). |
| **Allure command not found** | Install via `scoop install allure` or `npm i -g allure-commandline`. |
| **Headless mode looks broken** | Some sites behave differently headless. Run headed first to validate, then re-run with `--headless`. |
| **Brave not launching** | Set `BRAVE_PATH` in `.env` to the correct `brave.exe` location. |
| **Empty Allure report** | Confirm `--alluredir=reports/allure-results` ran (configured in `pytest.ini`) and that the test was discovered (`pytest --collect-only`). |
| **HTML report blank** | Open via `file://` URL, not the raw `\\` path. Use `start reports\test-report.html` on Windows. |
| **Tests fail on `https://`** | The `base_url` fixture auto-upgrades `http://` → `https://`. If you genuinely need HTTP, override `BASE_URL` in `.env`. |

---

## 💡 Tips & Best Practices

- **Run the framework-demo tests first** if you suspect a config issue:
  ```bash
  pytest tests/DEMO_framework_demo.py -v
  ```
- **Debug a single step**: drop a `breakpoint()` (Python 3.7+) inside a page object method and run with `pytest -s`.
- **Speed up CI**: combine `-n auto` (parallel) with `--headless`.
- **Avoid flakiness**: prefer the high-level `AutomationExercisePage` for the official TC suite — it bakes in
  retries, JS-click fallback, and ad-iframe hiding.
- **Don't commit** `reports/`, `.env`, `.pytest_cache/`, or `__pycache__/` — all are already in `.gitignore`.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📜 License

This project is provided for educational and capstone-assessment purposes.
The application under test ([AutomationExercise.com](https://automationexercise.com)) is a public demo
site owned by its respective owner.

---

## 👤 Author

**Manish Sharma**
GitHub: [@themanishpndt](https://github.com/themanishpndt)
Repository: [Capstone-Project](https://github.com/themanishpndt/Capstone-Project)

---

## 🗺 Roadmap

- [ ] Add API test layer for `/api/products` endpoints
- [ ] CI/CD integration (GitHub Actions) with Allure bot
- [ ] Cross-browser matrix on Selenium Grid / Docker Selenium
- [ ] Visual regression testing with `Pillow` + baseline diff
- [ ] Auto-generate page objects via code-gen

---

> ⭐ If you find this framework useful, please consider starring the repository!
