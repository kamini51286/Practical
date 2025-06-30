import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from datetime import datetime
import shutil


@pytest.fixture
def browser():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/practice-test-login/")  # Change URL as needed
        yield driver
        driver.quit()
    except Exception as e:
        raise e.msg
    
def pytest_configure(config):
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(reports_dir, f"report_{timestamp}.html")

    config.option.htmlpath = report_path  # dynamically set the report path
    config.option.self_contained_html = True  # standalone HTML

    # Step 4: Save for later use
    config._html_report_path = report_path
    config._latest_report_path = os.path.join(reports_dir, "latest.html")

def pytest_unconfigure(config):
    # Step 5: After test run, copy to 'latest.html'
    if hasattr(config, "_html_report_path"):
        shutil.copyfile(config._html_report_path, config._latest_report_path)