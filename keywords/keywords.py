from selenium import webdriver

def openBrowser(browserType, driverPath):
    if browserType == 'chrome':
        return webdriver.Chrome(driverPath)
    elif browserType == 'firefox':
        return webdriver.Firefox(driverPath)

def navigateTo(driver, url):
    driver.get(url)
    
def killBrowser(driver):
    driver.quit()