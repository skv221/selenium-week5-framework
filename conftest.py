from keywords.keywords import openBrowser, navigateTo, killBrowser
import pytest
import json
import time

with open('D:\Selenium Practices\Week 5\config\config.json', 'r') as file:
    config = json.load(file)

browserType = config["browser"]["type"]
driverPath = config["driver_paths"]["chrome_driver"]
testURL = config["environment"]["base_url"]

@pytest.fixture
def setup_browser():
    driver = openBrowser(browserType, driverPath)
    driver.maximize_window()
    navigateTo(testURL)
    yield driver
    time.sleep(5)
    killBrowser(driver)