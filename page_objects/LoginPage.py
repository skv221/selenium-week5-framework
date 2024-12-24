from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage

class LoginPage(BasePage):
    userNameField = (By.NAME, "user-name")
    passwordField = (By.NAME, "password")
    loginButton = (By.XPATH, "//input[@type='submit']")
    successElement = (By.XPATH, "//div[@class='inventory_item']")
    errorElement = (By.XPATH, "//h3[@data-test='error']")
    
    def login(self, userName, password):
        self.sendText(self.userNameField, userName)
        self.sendText(self.passwordField, password)
        self.clickElement(self.loginButton)
        self.validatelogin(self)
        
    def validatelogin(self):
        if self.isElementPresent(self.successElement):
            return True
        elif self.isElementPresent(self.errorElement):
            return False