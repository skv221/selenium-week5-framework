from keywords.keywords import openBrowser, navigateTo, killBrowser
from utilities.data_reader import read_json, read_excel
import pytest
import time

config = read_json("D:\Selenium Practices\Week 5\config\config.json")

browserType = config["browser"]["type"]
driverPath = config["driver_paths"]["chrome_driver"]
testURL = config["environment"]["base_url"]
testDataPath = config["test_data"]["file_path"]
columnsRequired = config["test_data"]["columns_required"]

@pytest.fixture
def setup_browser():
    driver = openBrowser(browserType, driverPath)
    driver.maximize_window()
    navigateTo(testURL)
    yield driver
    time.sleep(5)
    killBrowser(driver)
    
@pytest.fixture
def testData():
    return read_excel(testDataPath, columnsRequired)