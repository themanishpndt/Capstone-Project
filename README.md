<div align="center">

# 🧪 Capstone Project — AutomationExercise Test Automation Framework

### A robust, end-to-end **Selenium WebDriver + Pytest** automation framework built on the **Page Object Model (POM)** to exercise the public demo site [AutomationExercise.com](https://automationexercise.com).

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15.2-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.3-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.13.2-FF6A00?style=for-the-badge&logo=qameta&logoColor=white)](https://docs.qameta.io/allure/)
[![License](https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge)]()
[![Repo](https://img.shields.io/badge/GitHub-Capstone--Project-181717?style=for-the-badge&logo=github)](https://github.com/themanishpndt/Capstone-Project)

</div>

> The framework automates the **official 26-test-case AutomationExercise capstone suite** (register, login, search, cart, checkout, payment, subscription, categories, brands, reviews, scroll, invoice download, etc.) and produces rich **Allure** + **HTML** reports with automatic screenshots and browser logs on failure.

---

## 📑 Table of Contents

1. [🌟 Highlights](#-highlights)
2. [🚀 Project Overview](#-project-overview)
3. [📖 About This Project](#-about-this-project)
4. [🧩 Framework Overview — Selenium Automation (Python)](#-framework-overview--selenium-automation-python)
5. [🎨 Project Design Patterns](#-project-design-patterns)
6. [📐 Design Considerations](#-design-considerations)
7. [✅ Best Practices](#-best-practices)
8. [✨ Features](#-features)
9. [🧰 Tech Stack](#-tech-stack)
10. [🗂 Project Structure](#-project-structure)
11. [🧭 File & Folder Guide (Every File Explained)](#-file--folder-guide-every-file-explained)
12. [✅ Test Coverage (TC01 – TC26 — Step-by-Step)](#-test-coverage-tc01--tc26--step-by-step)
13. [🧱 Page Object Model (POM)](#-page-object-model-pom)
14. [🏷 Markers / Test Categorization](#-markers--test-categorization)
15. [🧪 Custom Fixtures](#-custom-fixtures)
16. [📂 Test Data](#-test-data)
17. [⚙ Prerequisites](#-prerequisites)
18. [🛠 Installation & Setup](#-installation--setup)
19. [🔧 Configuration](#-configuration)
20. [▶ Running the Tests](#-running-the-tests)
21. [📊 Reports & Artifacts](#-reports--artifacts)
22. [💡 Tips & Best Practices](#-tips--best-practices)
23. [🛠 Troubleshooting](#-troubleshooting)
24. [🤝 Contributing](#-contributing)
25. [📜 License](#-license)
26. [🗺 Roadmap](#-roadmap)
27. [👤 Author](#-author)

---

## 🌟 Highlights

- 🎯 **100% Page Object Model** — clean separation of locators, page actions, and test intent.
- 🌐 **Multi-browser** — Chrome, Brave, Firefox, Edge (headless optional).
- 📊 **Rich reporting** — Allure + self-contained HTML with auto-screenshots & browser logs.
- ⚡ **Parallel-ready** — `pytest-xdist` (`-n auto`) for fast regression.
- 🛡 **Flakiness hardened** — JS-click fallback, ad-frame hiding, explicit waits.
- 🧰 **Production-grade fixtures** — driver, wait, action_delay, test_data, auto-use logging.
- 🧪 **Data-driven** — CSV + JSON fixtures under `test_data/`.
- 🧱 **Helper layer** — `tests/helpers.py` provides `build_user()`, `create_account_from_signup_page()`, `login_existing_user()`.
- 🪪 **Demo / sanity tests** — `DEMO_framework_demo.py` validates the framework in seconds.
- 🔁 **Auto retry helper** baked into `AutomationExercisePage` for the official TC suite.

---

## 🚀 Project Overview

| Item | Value |
|---|---|
| **Application Under Test (AUT)** | [https://automationexercise.com](https://automationexercise.com) |
| **Domain** | E-commerce |
| **Framework** | Selenium 4 + Pytest 7 |
| **Design Pattern** | Page Object Model (POM) |
| **Language** | Python 3.12 (works on 3.10+) |
| **Supported Browsers** | Chrome, Brave, Firefox, Edge (headless optional) |
| **Reporting** | Allure + pytest-html (self-contained) |
| **Parallelization** | pytest-xdist |
| **Repository** | [Capstone-Project](https://github.com/themanishpndt/Capstone-Project) |
| **Author** | [Manish Sharma (@themanishpndt)](https://github.com/themanishpndt) |

---

## 📖 About This Project

> **Automated tests using Selenium with Python for an E-commerce website.**

This project was created to **practice test automation skills** using the **Selenium (Java/Python) framework**, leveraging skills learned through structured coursework (Udemy-style). The website under test — [**AutomationExercise.com**](https://automationexercise.com) — is a website **specifically designed for automated testing**, making it the ideal playground for end-to-end practice.

The project contains a **total of 26 automated tests**, created directly from the **official test cases defined by the site's developers**. After running and executing the tests, using the proper command, a **test report can be generated** which describes in detail the activities performed and the status (pass/fail) of each test.

**Why this project matters**

- 🛒 Exercises every layer of a real e-commerce site: **auth, browse, search, cart, checkout, payment, account, post-order actions**.
- 🧰 Demonstrates an **industry-grade hybrid framework** (POM + Data-driven + Helpers + Reporting).
- 🧪 Built for both **learning** and **interview/portfolio review** — every file has a clear purpose.

---

## 🧩 Framework Overview — Selenium Automation (Python)

The framework is built on a **hybrid Selenium + Python + PyTest** stack. Each pillar has a specific responsibility:

| Pillar | Role |
|---|---|
| **Selenium WebDriver** | Browser automation for validating web-application functionality across different browsers. |
| **Python** | Core programming language used for writing test scripts and framework logic. |
| **PyTest** | Test execution framework supporting assertions, fixtures, parameterization, parallel execution (`xdist`), and test grouping (`markers`). |
| **Page Object Model (POM)** | Design pattern to **enhance test maintainability** and **reduce code duplication** — each page is a class; locators are isolated. |
| **Data-Driven Testing** | Test data managed using **Excel / CSV / JSON** files (this project uses CSV + JSON) to execute the same test with multiple data sets. |
| **Git** | Version-control system for managing and tracking changes in test scripts. |
| **Allure Reports / PyTest HTML Reports** | Rich, interactive test reports with step details, screenshots, and execution history. |
| **Screenshot Utility** | Automatic screenshot capture on test failure for better debugging. |
| **Logging (`colorlog` / stdlib `logging`)** | Centralized logging for test execution and error tracking. |
| **Cross-Browser Testing** | Execution on **Chrome, Brave, Firefox, Edge** (headless optional) via `webdriver-manager`. |

---

## 🎨 Project Design Patterns

The framework intentionally combines **four proven design approaches** to maximize readability, scalability, and reuse:

| Pattern | Why we use it |
|---|---|
| **Page Object Model (POM)** | Keeps locators + page actions in dedicated classes — tests never touch raw selectors. |
| **Fluent Interface** | Page methods return `self` (or the next page object) so test code reads like a sentence: `home.click_signup_login().enter_name(...).click_signup()`. |
| **Data-Driven approach** | Same test logic, multiple inputs — users, products, payment cards, etc. are read from `test_data/`. |
| **Behavior-Driven approach** | Tests are written as human-readable scenarios (e.g., `test_register_user`, `test_login_incorrect`) with step-wise assertions. |

---

## 📐 Design Considerations

The following design considerations were applied while architecting this framework:

1. **POM (Page Object Model) pattern** in the hybrid framework — clear separation of concerns.
2. **PyTest-based test orchestration** with proper markers, fixtures, and `pytest.ini` configuration.
3. **Reusable functional components** kept separately to improve readability (e.g., `tests/helpers.py`, `src/utils/`).
4. **Multi-browser execution** — handles at least two browsers, in practice four (Chrome, Brave, Firefox, Edge).
5. **Data-driven concept** — input data imported from external files (CSV / JSON), not hard-coded.
6. **Handled exceptions with try/except** + clear error messages and a global `pytest_runtest_makereport` hook.
7. **Relative XPath used wherever necessary** (and ID / Name locators preferred for stability).
8. **End-to-end executable** — every test in the suite runs to completion against the live demo site.
9. **Locator hygiene** — prefer **ID or Name** locators; fall back to **relative XPath** when needed (no brittle absolute XPaths).
10. **Screenshots for failed steps** are created automatically and attached to the Allure report.
11. **Extent / Allure reports** are generated on every run, with step history, screenshots, and trends.

---

## ✅ Best Practices

The framework follows these best practices:

1. **`if-else` conditions** are written to control the test-script flow (e.g., browser / headless / URL selection).
2. **Screenshot helper code** is centralized in `src/utils/screenshot_utils.py` and re-used by the failure hook.
3. **Coding standards** are followed with proper comments and docstrings on every class/function.
4. **All scripts / business components / test results are in their respective folders** (`tests/`, `src/`, `reports/`).
5. **Page-synchronization timers** are used throughout — implicit + explicit waits via `WebDriverWait`.
6. **Scripts run end-to-end without any issue** — verified against the live demo site.
7. **Assertion and exception handling** is consistently applied — assertions on user-visible state, exception handling inside the page-object helpers.

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1 | **Page Object Model** | Clean 3-layer separation — *tests → pages → locators*. |
| 2 | **Multi-browser Support** | Chrome, Brave, Firefox, Edge via `webdriver-manager`. |
| 3 | **Data-driven Testing** | CSV / JSON fixtures under `test_data/`. |
| 4 | **Robust Waits** | Implicit + explicit (`WebDriverWait` with EC). |
| 5 | **Auto Screenshots** | Captured on every test failure (file + Allure attach). |
| 6 | **Browser Log Capture** | `driver.get_log('browser')` saved as JSON in Allure. |
| 7 | **Allure Environment** | Auto-generated `environment.properties`. |
| 8 | **HTML Report** | Self-contained via `--self-contained-html`. |
| 9 | **Parallel Execution** | Ready with `pytest-xdist -n auto`. |
| 10 | **Action-delay Fixture** | Slows playback for human-friendly demos. |
| 11 | **Hardened Click Helper** | Falls back to JS-click on `ElementClickInterceptedException`. |
| 12 | **Ad-frame Hiding** | Hides `iframe[id^='aswift']` & `ins.adsbygoogle` before clicks. |
| 13 | **High-level API** | `AutomationExercisePage` consolidates full E2E flows. |
| 14 | **Centralized Locators** | All XPath / CSS selectors isolated in `src/locators/`. |
| 15 | **Helper Functions** | `build_user()`, `create_account_from_signup_page()`, `login_existing_user()`. |
| 16 | **Sanity Tests** | `DEMO_framework_demo.py` validates the framework in <1s. |
| 17 | **Test-timeout** | 300s per test via `pytest-timeout`. |
| 18 | **CI-friendly** | Allure + HTML + log + screenshot artifacts on every run. |

---

## 🧰 Tech Stack

| Layer | Tool | Version |
|---|---|---|
| 🌐 Browser Automation | Selenium WebDriver | 4.15.2 |
| 🧰 Driver Management | webdriver-manager | 4.0.1 |
| 🧪 Test Runner | Pytest | 7.4.3 |
| ⚡ Parallelization | pytest-xdist | 3.5.0 |
| 🧾 HTML Report | pytest-html | 4.1.1 |
| 📈 Coverage | pytest-cov | 4.1.0 |
| ⏱ Timeout | pytest-timeout | 2.2.0 |
| 📊 Reporting | allure-pytest | 2.13.2 |
| 🎭 Fake Data | Faker | 21.0.0 |
| 📑 Excel Support | openpyxl | 3.1.2 |
| 🖼 Image Support | Pillow | 10.1.0 |
| 🌐 HTTP / API | requests | 2.31.0 |
| 🔐 Env Mgmt | python-dotenv | 1.0.0 |
| 📜 Logging | colorlog | 6.8.0 |
| 🧹 Code Quality | black | 23.12.1 |
| 🧹 Code Quality | flake8 | 6.1.0 |
| 🧹 Code Quality | pylint | 3.0.3 |

---

## 🗂 Project Structure

```text
Capstone-Project/
│
├── conftest.py                                # Global pytest fixtures & hooks (driver, wait, hooks, logging)
├── pytest.ini                                 # Pytest config, markers, addopts, log_cli
├── requirements.txt                           # Python dependencies (pinned)
├── .gitignore                                 # Git ignore rules (reports/, .env, caches, etc.)
├── README.md                                  # You are here 🧭
│
├── .venv/                                     # Local virtual environment (gitignored)
│
├── config/
│   ├── __init__.py
│   └── config.py                              # Config + URLs classes (loads from .env)
│
├── src/                                       # Framework source code (pages / locators / utils)
│   ├── __init__.py
│   ├── pages/                                 # Page Object Model classes
│   │   ├── __init__.py
│   │   ├── base_page.py                       # BasePage — shared helpers (find/click/enter/get/wait)
│   │   ├── home_page.py                       # HomePage
│   │   ├── login_page.py                      # LoginPage (signup + login + register form)
│   │   ├── product_page.py                    # ProductPage
│   │   ├── cart_page.py                       # CartPage
│   │   ├── checkout_page.py                   # CheckoutPage
│   │   ├── contact_page.py                    # ContactPage (TC06)
│   │   ├── category_page.py                   # CategoryPage (TC18)
│   │   ├── brand_page.py                      # BrandPage (TC19)
│   │   ├── review_page.py                     # ReviewPage (TC21)
│   │   ├── scroll_page.py                     # ScrollPage (TC25, TC26)
│   │   ├── subscription_page.py               # SubscriptionPage (TC10, TC11)
│   │   ├── invoice_page.py                    # InvoicePage (TC24)
│   │   └── automation_exercise_page.py        # High-level unified page object (official TC suite)
│   │
│   ├── locators/                              # Centralized XPath / CSS locators
│   │   ├── __init__.py
│   │   ├── common_locators.py                 # Common locators (nav, header, footer, alerts)
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
│   │   └── __init__.py                        # Reserved for future driver factory
│   │
│   └── utils/                                 # Helpers: logging, waits, screenshots
│       ├── __init__.py
│       ├── logger_utils.py                    # setup_logger(), log_test_start(), log_test_end()
│       ├── wait_utils.py                      # wait_for_element_visibility/clickable/presence/url/text
│       └── screenshot_utils.py                # take_screenshot(), take_screenshot_on_failure()
│
├── tests/                                     # Test suite (official TC01 – TC26)
│   ├── __init__.py
│   ├── helpers.py                             # Shared helpers (build_user, create_account, login)
│   ├── DEMO_framework_demo.py                 # Sanity / framework validation tests
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
├── test_data/                                 # Data-driven test inputs
│   ├── __init__.py
│   ├── valid_users.csv                        # Valid email/password/name fixtures
│   ├── invalid_credentials.csv                # Negative login scenarios + SQL-injection
│   ├── products.json                          # Sample product catalog
│   └── contact_upload.txt                     # File uploaded by TC06 contact form
│
└── reports/                                   # Auto-generated outputs (gitignored)
    ├── logs/
    │   └── test.log
    ├── screenshots/                           # On-failure PNGs
    ├── allure-results/                        # Allure raw JSON
    ├── allure-report/                         # Generated Allure HTML (after `allure generate`)
    ├── downloads/                             # Invoice downloads (TC24)
    └── test-report.html                       # Self-contained HTML report
```

---

## 🧭 File & Folder Guide (Every File Explained)

> This is a one-stop explanation of **every meaningful file/folder** in the repository, what it does, and when to touch it.

### 🔝 Root-level files

| File | Purpose |
|---|---|
| `conftest.py` | **Global pytest configuration.** Defines the `driver`, `wait`, `action_delay`, `test_data`, `log_test_start_end`, `setup_allure_environment` fixtures; registers CLI options (`--browser`, `--headless`, `--base_url`); implements the `pytest_runtest_makereport` hook (auto-screenshot + browser-log attach to Allure on failure). |
| `pytest.ini` | Pytest configuration: discovery patterns (`test_*.py tc*.py`), 12 custom markers (`smoke`, `critical`, `official`, etc.), addopts (`-v`, `--tb=short`, `--strict-markers`, `--alluredir`, `--html`), `log_cli` settings, `testpaths`, `timeout=300`, `asyncio_mode=auto`. |
| `requirements.txt` | All Python dependencies, version-pinned. Installed via `pip install -r requirements.txt`. |
| `.gitignore` | Excludes `__pycache__/`, `.venv/`, `reports/`, `.env`, `.pytest_cache/`, logs, IDE/OS junk. |
| `README.md` | This file. The single source of truth for setup, usage, and architecture. |
| `Capstone Project-E-commerce_Web automation using Selenium and Python.docx` | The original capstone project brief / report document. |

### 📁 `config/`

| File | Purpose |
|---|---|
| `config.py` | Defines the `Config` class (browser, wait timeouts, log/screenshot/report flags, proxy) and the `URLs` helper class (LOGIN, REGISTER, PRODUCTS, CART, CHECKOUT, PROFILE, ORDERS, WISHLIST). Loads from environment via `python-dotenv`. |

### 📁 `src/pages/` — *Page Object Model*

| File | Purpose |
|---|---|
| `base_page.py` | `BasePage` — the parent of all page objects. Provides `find_element`, `find_elements`, `click_element` (with JS-click fallback), `enter_text`, `get_text`, `is_element_visible`, `wait_for_url_contains`, `navigate_to`, `refresh_page`, `get_current_url`, `go_back`, `go_forward`. |
| `home_page.py` | `HomePage` — home page actions (navigate, click signup/login, etc.). |
| `login_page.py` | `LoginPage` — signup, login, register form (title, DOB, name, address, company, mobile, country, etc.). |
| `product_page.py` | `ProductPage` — product browsing, search, detail page. |
| `cart_page.py` | `CartPage` — add/remove products, quantity, view cart. |
| `checkout_page.py` | `CheckoutPage` — address review, place order, payment. |
| `contact_page.py` | `ContactPage` — TC06 contact-us form. |
| `category_page.py` | `CategoryPage` — TC18 women/men/kids category navigation. |
| `brand_page.py` | `BrandPage` — TC19 brand listing & brand-product filtering. |
| `review_page.py` | `ReviewPage` — TC21 add review on product. |
| `scroll_page.py` | `ScrollPage` — TC25/TC26 arrow-button & no-arrow scroll-up verification. |
| `subscription_page.py` | `SubscriptionPage` — TC10 (home footer) & TC11 (cart footer) subscription. |
| `invoice_page.py` | `InvoicePage` — TC24 invoice download. |
| `automation_exercise_page.py` | **High-level unified page object** that consolidates the full E2E flows (signup, register, search, add-to-cart, checkout, payment, invoice download) used by the official TC suite. Includes helpers like `_hide_ad_frames()` and `_xpath_literal()` for safer XPath construction. |

### 📁 `src/locators/` — *Centralized Selectors*

| File | Purpose |
|---|---|
| `common_locators.py` | Shared locators (nav, header, footer, success/error/warning messages, submit/cancel/OK buttons). |
| `home_locators.py` | Home-page-specific selectors. |
| `login_locators.py` | Login + signup + register-form selectors. |
| `cart_locators.py` | Cart-page selectors (rows, qty input, remove button, totals). |
| `checkout_locators.py` | Address + payment selectors. |
| `product_locators.py` | Product cards, search input, view-product link. |
| `contact_locators.py` | TC06 contact-form selectors. |
| `category_locators.py` | Women/Men/Kids category panel selectors (TC18). |
| `brand_locators.py` | Brand list + brand product page selectors (TC19). |
| `review_locators.py` | Add-review form selectors (TC21). |
| `scroll_locators.py` | Scroll-up arrow + scroll target (TC25/TC26). |
| `subscription_locators.py` | Footer subscription form (TC10/TC11). |
| `invoice_locators.py` | Invoice download button (TC24). |

### 📁 `src/drivers/`

| File | Purpose |
|---|---|
| `__init__.py` | **Reserved** for a future driver factory / cross-browser driver manager. |

### 📁 `src/utils/` — *Reusable Helpers*

| File | Purpose |
|---|---|
| `logger_utils.py` | `setup_logger(name, log_file, level)` → logger with file + console handlers; `log_test_start()` / `log_test_end()` for banners. |
| `wait_utils.py` | `wait_for_element_visibility / clickable / presence / url_contains / text_in_element` — return `True`/`False` instead of raising. |
| `screenshot_utils.py` | `take_screenshot(driver, filename, directory)` and `take_screenshot_on_failure(driver, test_name)` for the on-failure hook. |

### 📁 `tests/` — *Test Suite*

| File | Purpose |
|---|---|
| `__init__.py` | Marks the directory as an importable package. |
| `helpers.py` | Shared helpers — `build_user(prefix)` (timestamped unique user), `create_account_from_signup_page(login_page, action_delay, user)`, `login_existing_user(login_page, email, password, action_delay)`. |
| `DEMO_framework_demo.py` | 9 sanity tests that validate fixtures, config, page objects, locators, and utility modules. Run these first when something looks wrong. |
| `tc01_register_user.py` → `tc26_verify_scroll_up_without_arrow_button.py` | The 26 official AutomationExercise test cases (see [Test Coverage](#-test-coverage-tc01--tc26)). |

### 📁 `test_data/` — *Data-driven Inputs*

| File | Purpose |
|---|---|
| `__init__.py` | Marks the directory as an importable package. |
| `valid_users.csv` | Valid login credentials + names (`test1@example.com`, `Password123!`, etc.). |
| `invalid_credentials.csv` | Negative login scenarios — empty fields, weak password, **SQL-injection attempt** (`' OR '1'='1`). |
| `products.json` | Sample product catalog (5 products across Electronics, Accessories, Cables). |
| `contact_upload.txt` | Tiny text file uploaded by the TC06 contact-us test. |

### 📁 `reports/` — *Auto-generated Artifacts (gitignored)*

| Path | Purpose |
|---|---|
| `reports/logs/test.log` | Plain-text execution log (root logger) with timestamps + file/line info. |
| `reports/screenshots/<test>_<timestamp>.png` | Auto-screenshot on every test failure (also attached to Allure). |
| `reports/allure-results/` | Allure raw JSON results. |
| `reports/allure-report/` | Generated Allure HTML site (after `allure generate`). |
| `reports/downloads/` | Invoice downloads captured by TC24. |
| `reports/test-report.html` | Self-contained HTML report (`pytest-html --self-contained-html`). |

---

## ✅ Test Coverage (TC01 – TC26 — Step-by-Step)

The framework implements the **official AutomationExercise 26-step capstone suite** — the complete step-by-step test scenarios defined by the site's developers. Each test below is mapped 1-to-1 to a file under `tests/`.

> **Quick navigation:** [TC01](#-test-case-1-register-user) · [TC02](#-test-case-2-login-user-with-correct-email-and-password) · [TC03](#-test-case-3-login-user-with-incorrect-email-and-password) · [TC04](#-test-case-4-logout-user) · [TC05](#-test-case-5-register-user-with-existing-email) · [TC06](#-test-case-6-contact-us-form) · [TC07](#-test-case-7-verify-test-cases-page) · [TC08](#-test-case-8-verify-all-products-and-product-detail-page) · [TC09](#-test-case-9-search-product) · [TC10](#-test-case-10-verify-subscription-in-home-page) · [TC11](#-test-case-11-verify-subscription-in-cart-page) · [TC12](#-test-case-12-add-products-in-cart) · [TC13](#-test-case-13-verify-product-quantity-in-cart) · [TC14](#-test-case-14-place-order-register-while-checkout) · [TC15](#-test-case-15-place-order-register-before-checkout) · [TC16](#-test-case-16-place-order-login-before-checkout) · [TC17](#-test-case-17-remove-products-from-cart) · [TC18](#-test-case-18-view-category-products) · [TC19](#-test-case-19-view--cart-brand-products) · [TC20](#-test-case-20-search-products-and-verify-cart-after-login) · [TC21](#-test-case-21-add-review-on-product) · [TC22](#-test-case-22-add-to-cart-from-recommended-items) · [TC23](#-test-case-23-verify-address-details-in-checkout-page) · [TC24](#-test-case-24-download-invoice-after-purchase-order) · [TC25](#-test-case-25-verify-scroll-up-using-arrow-button-and-scroll-down-functionality) · [TC26](#-test-case-26-verify-scroll-up-without-arrow-button-and-scroll-down-functionality)

---

### 🧪 Test Case 1: Register User
*File: `tests/tc01_register_user.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Signup / Login'` button
5. Verify `'New User Signup!'` is visible
6. Enter name and email address
7. Click `'Signup'` button
8. Verify that `'ENTER ACCOUNT INFORMATION'` is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox `'Sign up for our newsletter!'`
11. Select checkbox `'Receive special offers from our partners!'`
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click `'Create Account button'`
14. Verify that `'ACCOUNT CREATED!'` is visible
15. Click `'Continue'` button
16. Verify that `'Logged in as username'` is visible
17. Click `'Delete Account'` button
18. Verify that `'ACCOUNT DELETED!'` is visible and click `'Continue'` button

---

### 🧪 Test Case 2: Login User with correct email and password
*File: `tests/tc02_login_correct.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Signup / Login'` button
5. Verify `'Login to your account'` is visible
6. Enter correct email address and password
7. Click `'login'` button
8. Verify that `'Logged in as username'` is visible

---

### 🧪 Test Case 3: Login User with incorrect email and password
*File: `tests/tc03_login_incorrect.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Signup / Login'` button
5. Verify `'Login to your account'` is visible
6. Enter incorrect email address and password
7. Click `'login'` button
8. Verify error `'Your email or password is incorrect!'` is visible

---

### 🧪 Test Case 4: Logout User
*File: `tests/tc04_logout.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Signup / Login'` button
5. Verify `'Login to your account'` is visible
6. Enter correct email address and password
7. Click `'login'` button
8. Verify that `'Logged in as username'` is visible
9. Click `'Logout'` button
10. Verify that user is navigated to login page

---

### 🧪 Test Case 5: Register User with existing email
*File: `tests/tc05_register_existing_email.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Signup / Login'` button
5. Verify `'New User Signup!'` is visible
6. Enter name and already registered email address
7. Click `'Signup'` button
8. Verify error `'Email Address already exist!'` is visible

---

### 🧪 Test Case 6: Contact Us Form
*File: `tests/tc06_contact_us.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Contact Us'` button
5. Verify `'GET IN TOUCH'` is visible
6. Enter name, email, subject and message
7. Upload file
8. Click `'Submit'` button
9. Click OK button
10. Verify success message `'Success! Your details have been submitted successfully.'` is visible
11. Click `'Home'` button and verify that landed to home page successfully

---

### 🧪 Test Case 7: Verify Test Cases Page
*File: `tests/tc07_test_cases_page.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Test Cases'` button
5. Verify user is navigated to test cases page successfully

---

### 🧪 Test Case 8: Verify All Products and product detail page
*File: `tests/tc08_product_browse.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Products'` button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. The products list is visible
7. Click on `'View Product'` of first product
8. User is landed to product detail page
9. Verify that detail detail is visible: product name, category, price, availability, condition, brand

---

### 🧪 Test Case 9: Search Product
*File: `tests/tc09_product_search.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click on `'Products'` button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify `'SEARCHED PRODUCTS'` is visible
8. Verify all the products related to search are visible

---

### 🧪 Test Case 10: Verify Subscription in home page
*File: `tests/tc10_home_subscription.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Scroll down to footer
5. Verify text `'SUBSCRIPTION'`
6. Enter email address in input and click arrow button
7. Verify success message `'You have been successfully subscribed!'` is visible

---

### 🧪 Test Case 11: Verify Subscription in Cart page
*File: `tests/tc11_cart_subscription.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click `'Cart'` button and scroll down to footer
5. Verify text `'SUBSCRIPTION'`
6. Enter email address in input and click arrow button
7. Verify success message `'You have been successfully subscribed!'` is visible

---

### 🧪 Test Case 12: Add Products in Cart
*File: `tests/tc12_shopping_cart.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click `'Products'` button
5. Hover over first product and click `'Add to cart'`
6. Click `'Continue Shopping'` button
7. Hover over second product and click `'Add to cart'`
8. Click `'View Cart'` button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price

---

### 🧪 Test Case 13: Verify Product quantity in Cart
*File: `tests/tc13_product_quantity.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click `'View Product'` for any product on home page
5. Verify product detail is opened
6. Increase quantity to 4
7. Click `'Add to cart'` button
8. Click `'View Cart'` button
9. Verify that product is displayed in cart page with exact quantity

### 🧪 Test Case 14: Place Order: Register while Checkout
*File: `tests/tc14_place_order_register_checkout.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Add products to cart
5. Click `'Cart'` button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click `'Register / Login'` button
9. Fill all details in Signup and create account
10. Verify `'ACCOUNT CREATED!'` and click `'Continue'` button
11. Verify `' Logged in as username'` at top
12. Click `'Cart'` button
13. Click `'Proceed To Checkout'` button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click `'Place Order'`
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click `'Pay and Confirm Order'` button
18. Verify success message `'Congratulations! Your order has been confirmed!'`
19. Click `'Delete Account'` button
20. Verify `'ACCOUNT DELETED!'` and click `'Continue'` button

---

### 🧪 Test Case 15: Place Order: Register before Checkout
*File: `tests/tc15_place_order_register_before_checkout.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click `'Signup / Login'` button
5. Fill all details in Signup and create account
6. Verify `'ACCOUNT CREATED!'` and click `'Continue'` button
7. Verify `' Logged in as username'` at top
8. Add products to cart
9. Click `'Cart'` button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify Address Details and Review Your Order
13. Enter description in comment text area and click `'Place Order'`
14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
15. Click `'Pay and Confirm Order'` button
16. Verify success message `'Congratulations! Your order has been confirmed!'`
17. Click `'Delete Account'` button
18. Verify that `'ACCOUNT DELETED!'` and click `'Continue'` button

---

### 🧪 Test Case 16: Place Order: Login before Checkout
*File: `tests/tc16_place_order_login_before_checkout.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click `'Signup / Login'` button
5. Fill email, password and click `'Login'` button
6. Verify `'Logged in as username'` at top
7. Add products to cart
8. Click `'Cart'` button
9. Verify that cart page is displayed
10. Click Proceed To Checkout
11. Verify Address Details and Review Your Order
12. Enter description in comment text area and click `'Place Order'`
13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
14. Click `'Pay and Confirm Order'` button
15. Verify success message `'Congratulations! Your order has been confirmed!'`

---

### 🧪 Test Case 17: Remove Products From Cart
*File: `tests/tc17_remove_products_from_cart.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Add products to cart
5. Click `'Cart'` button
6. Verify that cart page is displayed
7. Click `'X'` button corresponding to particular product
8. Verify that product is removed from the cart

---

### 🧪 Test Case 18: View Category Products
*File: `tests/tc18_view_category_products.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that categories are visible on left side bar
4. Click on `'Women'` category
5. Click on any category link under `'Women'` category, for example: Dress
6. Verify that category page is displayed and confirm text `'WOMEN - DRESS PRODUCTS'`
7. On left side bar, click on any sub-category link of `'Men'` category
8. Verify that user is navigated to that category page

---

### 🧪 Test Case 19: View & Cart Brand Products
*File: `tests/tc19_view_cart_brand_products.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Click on `'Products'` button
4. Verify that Brands are visible on left side bar
5. Click on any brand name
6. Verify that user is navigated to brand page and brand products are displayed
7. On left side bar, click on any other brand link
8. Verify that user is navigated to that brand page and can see products

---

### 🧪 Test Case 20: Search Products and Verify Cart After Login
*File: `tests/tc20_search_products_verify_cart_after_login.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Click on `'Products'` button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Enter product name in search input and click search button
6. Verify `'SEARCHED PRODUCTS'` is visible
7. Verify all the products related to search are visible
8. Add those products to cart
9. Click `'Cart'` button and verify that products are visible in cart
10. Click `'Signup / Login'` button and submit login details
11. Again, go to Cart page
12. Verify that those products are visible in cart after login as well
13. Remove all products that have been added
14. Verify `'Cart is empty! Click here to buy products.'` is visible

---

### 🧪 Test Case 21: Add review on product
*File: `tests/tc21_add_review_on_product.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Click on `'Products'` button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Click on `'View Product'` button
6. Verify `'Write Your Review'` is visible
7. Enter name, email and review
8. Click `'Submit'` button
9. Verify success message `'Thank you for your review.'`

---

### 🧪 Test Case 22: Add to cart from Recommended items
*File: `tests/tc22_add_to_cart_from_recommended_items.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Scroll to bottom of page
4. Verify `'RECOMMENDED ITEMS'` are visible
5. Click on `'Add To Cart'` on Recommended product
6. Click on `'View Cart'` button
7. Verify that product is displayed in cart page

---

### 🧪 Test Case 23: Verify address details in checkout page
*File: `tests/tc23_verify_address_details_in_checkout_page.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Click `'Signup / Login'` button
5. Fill all details in Signup and create account
6. Verify `'ACCOUNT CREATED!'` and click `'Continue'` button
7. Verify `' Logged in as username'` at top
8. Add products to cart
9. Click `'Cart'` button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify that the delivery address and the billing address is same address filled at the time registration of account
13. Click `'Delete Account'` button
14. Verify `'ACCOUNT DELETED!'` and click `'Continue'` button

---

### 🧪 Test Case 24: Download Invoice after purchase order
*File: `tests/tc24_download_invoice_after_purchase_order.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfull
4. Add products to cart
5. Click `'Cart'` button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click `'Register / Login'` button
9. Fill all details in Signup and create account
10. Verify `'ACCOUNT CREATED!'` and click `'Continue'` button
11. Verify `' Logged in as username'` at top
12. Click `'Cart'` button
13. Click `'Proceed To Checkout'` button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click `'Place Order'`
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click `'Pay and Confirm Order'` button
18. Verify success message `'Congratulations! Your order has been confirmed!'`
19. Click `'Download Invoice'` button and verify invoice is downloaded successfully
20. Click `'Continue'` button
21. Click `'Delete Account'` button
22. Verify `'ACCOUNT DELETED!'` and click `'Continue'` button

---

### 🧪 Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
*File: `tests/tc25_verify_scroll_up_using_arrow_button.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify `'SUBSCRIPTION'` is visible
6. Click on arrow at bottom right side to move upward
7. Verify that page is scrolled up and `'Full-Fledged practice website for Automation Engineers'` text is visible on screen

---

### 🧪 Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
*File: `tests/tc26_verify_scroll_up_without_arrow_button.py`*

1. Launch browser
2. Navigate to url `'http://automationexercise.com'`
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify `'SUBSCRIPTION'` is visible
6. Scroll up page to top
7. Verify that page is scrolled up and `'Full-Fledged practice website for Automation Engineers'` text is visible on screen


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
│  src/pages/*.py          │   ← actions & flows (login(), add_to_cart() …)
└────────────┬─────────────┘
             │ uses
             ▼
┌──────────────────────────┐
│  src/locators/*.py       │   ← XPath / CSS selectors only
└──────────────────────────┘
```

- **`BasePage`** provides shared helpers: `find_element`, `click_element`, `enter_text`, `is_element_visible`, `navigate_to`, `get_text`, `wait_for_url_contains`, `go_back`, `go_forward`, `refresh_page`.
- **`AutomationExercisePage`** is a *higher-level* page object that consolidates cross-page flows (signup, register, search, add-to-cart, checkout, payment, invoice download) for the **official TC** suite — pick this when you want a single call per E2E step.
- **Locators** are kept in dedicated `*_locators.py` modules so they can be updated in one place without touching the page objects or tests.

---

## 🏷 Markers / Test Categorization

Defined in `pytest.ini`:

| Marker | Purpose |
|---|---|
| `official` | Official AutomationExercise capstone test cases |
| `smoke` | Critical path sanity tests |
| `regression` | Full regression coverage |
| `critical` | Must-pass tests for releases |
| `ui` | UI interaction tests |
| `api` | API tests |
| `functional` | Functional tests (default if no marker set) |
| `end_to_end` | Full workflow tests |
| `parametrize` | Parameterized tests |
| `slow` | Tests that take longer than usual |
| `unit` | Unit-level tests |
| `integration` | Integration tests |

**Usage:**

```bash
pytest -m "smoke and not slow"
pytest -m "official and critical"
pytest -m "smoke or critical" -n auto
```

---

## 🧪 Custom Fixtures (defined in `conftest.py`)

| Fixture | Scope | Description |
|---|---|---|
| `base_url` | session | Returns the configured base URL (auto-upgrades `http://` → `https://`). |
| `driver` | function | Initializes a fresh WebDriver (chrome/brave/firefox/edge) with safe defaults and tear-down `quit()`. |
| `wait` | function | A `WebDriverWait` instance with `EXPLICIT_WAIT` timeout. |
| `action_delay` | function | Helper `action_delay(seconds)` to slow down actions for visibility. |
| `auto_action_delay` | function (autouse) | Adds configurable delay before/after each test. |
| `test_data` | function | Dictionary of common test data (emails, password, name, etc.). |
| `log_test_start_end` | session (autouse) | Logs banner at suite start/end. |
| `setup_allure_environment` | session (autouse) | Placeholder for Allure env metadata (written in `pytest_configure`). |

**CLI options (added by `pytest_addoption`):**

| Flag | Default | Description |
|---|---|---|
| `--browser` | `chrome` | `chrome`, `brave`, `firefox`, or `edge` |
| `--headless` | `False` | Run browser in headless mode |
| `--base_url` | `https://automationexercise.com` | Base URL override |

**Hooks:**

- `pytest_runtest_makereport` — captures screenshots on failure and attaches them + browser logs to Allure.
- `pytest_configure` — writes `reports/allure-results/environment.properties` and registers all custom markers.
- `pytest_collection_modifyitems` — adds default `functional` marker and Allure dynamic IDs.

---

## 📂 Test Data

| File | Purpose |
|---|---|
| `test_data/valid_users.csv` | Valid email/password/name combinations (4 fixtures). |
| `test_data/invalid_credentials.csv` | Negative login scenarios (empty, weak, **SQL injection**). |
| `test_data/products.json` | Sample product catalog (5 products). |
| `test_data/contact_upload.txt` | File uploaded by the TC06 contact-form test. |
| `test_data/__init__.py` | Marks directory as importable package. |

---

## ⚙ Prerequisites

- **Python 3.10+** (developed on Python 3.12)
- **Git**
- One or more of the following browsers installed:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - Brave (optional — path configurable in `.env`)
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

# Download directory (for TC24 invoice test)
DOWNLOAD_DIR=reports/downloads

# Brave (optional)
BRAVE_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe

# Page load strategy
PAGE_LOAD_STRATEGY=eager

# Logging
LOG_LEVEL=INFO
LOG_FILE=reports/logs/test.log

# Screenshot / Report toggles
TAKE_SCREENSHOT_ON_FAILURE=True
SCREENSHOT_PATH=reports/screenshots/
GENERATE_HTML_REPORT=True
GENERATE_ALLURE_REPORT=True

# Proxy (optional)
USE_PROXY=False
PROXY_URL=

# Test user defaults (used by test_data fixture)
TEST_USER_EMAIL=test@example.com
TEST_USER_PASSWORD=Password123!
```

---

## 🔧 Configuration

Two configuration layers — both fed from environment variables:

1. **`conftest.py`** — runtime browser driver config (used by the `driver` fixture).
2. **`config/config.py`** — long-lived `Config` + `URLs` classes for cross-module access.

| Class | Notable attributes |
|---|---|
| `Config` | `BASE_URL`, `BROWSER`, `HEADLESS`, `WINDOW_SIZE`, `IMPLICIT_WAIT`, `EXPLICIT_WAIT`, `PAGE_LOAD_TIMEOUT`, `TEST_USER_EMAIL`, `TEST_USER_PASSWORD`, `LOG_LEVEL`, `LOG_FILE`, `TAKE_SCREENSHOT_ON_FAILURE`, `SCREENSHOT_PATH`, `GENERATE_HTML_REPORT`, `GENERATE_ALLURE_REPORT`, `USE_PROXY`, `PROXY_URL` |
| `URLs` | `BASE_URL`, `LOGIN_URL`, `REGISTER_URL`, `PRODUCTS_URL`, `CART_URL`, `CHECKOUT_URL`, `PROFILE_URL`, `ORDERS_URL`, `WISHLIST_URL` |

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

### Run the official AutomationExercise suite only
```bash
pytest -m official
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

### Sanity-check the framework (no browser needed for most)
```bash
pytest tests/DEMO_framework_demo.py -v
```

### Collect tests without running
```bash
pytest --collect-only
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

## 💡 Tips & Best Practices

- **Run the framework-demo tests first** if you suspect a config issue:
  ```bash
  pytest tests/DEMO_framework_demo.py -v
  ```
- **Debug a single step**: drop a `breakpoint()` (Python 3.7+) inside a page-object method and run with `pytest -s`.
- **Speed up CI**: combine `-n auto` (parallel) with `--headless`.
- **Avoid flakiness**: prefer the high-level `AutomationExercisePage` for the official TC suite — it bakes in retries, JS-click fallback, and ad-iframe hiding.
- **Unique test data**: use `tests/helpers.py::build_user()` to generate timestamped, isolated users for every test.
- **Don't commit** `reports/`, `.env`, `.pytest_cache/`, or `__pycache__/` — all are already in `.gitignore`.
- **Code style**: keep tests readable, one assertion per logical step; rely on the framework's automatic screenshot for failure context.

---

## 🛠 Troubleshooting

| Issue | Solution |
|---|---|
| **`SessionNotCreatedException` / driver version mismatch** | `webdriver-manager` downloads matching drivers automatically. Ensure you have write permission in the project directory. |
| **Click intercepted by Google ads** | The framework hides `iframe[id^='aswift']` and `ins.adsbygoogle` before each click via `_hide_ad_frames()` in `automation_exercise_page.py`. If a new ad format appears, update that method. |
| **`ElementClickInterceptedException` persists** | Increase `EXPLICIT_WAIT` / `IMPLICIT_WAIT` in `.env`. The `BasePage.click_element` already falls back to JS-click. |
| **Timeouts on slow networks** | Bump `PAGE_LOAD_TIMEOUT` in `.env` (default 40s). |
| **Allure command not found** | Install via `scoop install allure` or `npm i -g allure-commandline`. |
| **Headless mode looks broken** | Some sites behave differently headless. Run headed first to validate, then re-run with `--headless`. |
| **Brave not launching** | Set `BRAVE_PATH` in `.env` to the correct `brave.exe` location. |
| **Empty Allure report** | Confirm `--alluredir=reports/allure-results` ran (configured in `pytest.ini`) and that the test was discovered (`pytest --collect-only`). |
| **HTML report blank** | Open via `file://` URL, not the raw `\\` path. Use `start reports\test-report.html` on Windows. |
| **Tests fail on `https://`** | The `base_url` fixture auto-upgrades `http://` → `https://`. If you genuinely need HTTP, override `BASE_URL` in `.env`. |
| **Test times out at 300s** | The default is set in `pytest.ini` (`timeout = 300`). Bump it for very slow tests, or split them up. |
| **ModuleNotFoundError: src** | Run pytest from the project root so the `src/` package is importable. |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a Pull Request

**Coding standards**
- `black` for formatting
- `flake8` / `pylint` for linting
- Page Objects first, locators in dedicated modules, helper functions in `tests/helpers.py`.

---

## 📜 License

This project is provided for **educational and capstone-assessment purposes**.
The application under test ([AutomationExercise.com](https://automationexercise.com)) is a public demo
site owned by its respective owner.

---

## 🗺 Roadmap

- [ ] Add API test layer for `/api/products` endpoints
- [ ] CI/CD integration (GitHub Actions) with Allure bot
- [ ] Cross-browser matrix on Selenium Grid / Docker Selenium
- [ ] Visual regression testing with `Pillow` + baseline diff
- [ ] Auto-generate page objects via code-gen
- [ ] Implement the reserved `src/drivers/` factory
- [ ] Dockerize the framework (one-command CI run)

---

## 👤 Author

**Manish Sharma**
GitHub: [@themanishpndt](https://github.com/themanishpndt)
Repository: [Capstone-Project](https://github.com/themanishpndt/Capstone-Project)

---

> ⭐ If you find this framework useful, please consider **starring** the repository!
>
> 🐛 Found a bug? Report it via `/reportbug` (Cline) or open a GitHub issue.
>
> 💡 Have an idea? Open a PR — every contribution is welcome.

<div align="center">

**Built with ❤️ using Selenium + Pytest + POM**

</div>
