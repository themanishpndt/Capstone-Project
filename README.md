# Selenium E-commerce Automation Capstone

Python Selenium framework for the AutomationExercise e-commerce practice site.

## Structure

- `tests/test_official_automation_exercise.py` - default 26-case capstone suite.
- `src/pages/automation_exercise_page.py` - page object used by the official suite.
- `src/pages/`, `src/locators/`, `src/utils/` - reusable framework layers.
- `test_data/` - CSV/JSON/input files used by tests.
- `reports/` - generated screenshots, logs, HTML, Allure results, and downloads.

The older exploratory tests are kept in the repository, but `pytest.ini` points the default run at the official 26 AutomationExercise cases.

## Run

```powershell
.venv\Scripts\python.exe -m pytest --headless
```

Useful options:

```powershell
.venv\Scripts\python.exe -m pytest --browser chrome --headless
.venv\Scripts\python.exe -m pytest --browser firefox --headless
.venv\Scripts\python.exe -m pytest --browser edge --headless
.venv\Scripts\python.exe -m pytest tests/test_official_automation_exercise.py::TestOfficialAutomationExercise::test_21_add_review_on_product --headless
```

Reports are generated at `reports/test-report.html` and `reports/allure-results/`.
