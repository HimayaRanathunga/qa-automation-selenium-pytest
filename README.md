# QA Automation Suite - Selenium + PyTest + CI/CD

Automated test suite for web application login functionality, built with Selenium WebDriver and PyTest. Integrated with GitHub Actions for continuous integration, running tests automatically in headless Chrome on every push.

## Overview

This project demonstrates end-to-end test automation practices including:
- Positive and negative test scenario coverage
- Headless browser execution for CI/CD environments
- Automated pipeline triggered on every code push

## Tech Stack

- **Language:** Python
- **Testing Framework:** PyTest
- **Automation Tool:** Selenium WebDriver
- **CI/CD:** GitHub Actions
- **Target Application:** [SauceDemo](https://www.saucedemo.com) (e-commerce demo site)

## Test Cases

| Test | Description | Expected Result |
|------|-------------|------------------|
| `test_valid_login` | Logs in with valid credentials | User redirected to inventory page |
| `test_invalid_login` | Logs in with invalid credentials | Error message displayed |

## Project Structure
qa-automation-project/
├── .github/workflows/
│   └── test.yml          # CI/CD pipeline configuration
├── test_login.py         # Login test cases
├── test_first.py         # Basic Selenium setup test
└── README.md

## Running Locally

1. Clone the repository:
git clone https://github.com/HimayaRanathunga/qa-automation-selenium-pytest.git 
cd qa-automation-selenium-pytest

2. Create a virtual environment and install dependencies:
python -m venv venv
venv\Scripts\activate
pip install selenium pytest webdriver-manager

3. Run the tests:
pytest test_login.py -v -s

## CI/CD Pipeline

Tests run automatically on every push to `main` via GitHub Actions. The pipeline:
1. Checks out the code
2. Sets up Python and Chrome
3. Installs dependencies
4. Runs the test suite in headless mode

## Author
Himaya Ranathunga


