from selenium.webdriver.common.by import By

class Login_Admin_Page:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_css = "input[class*='login-button']"
    link_login_linkText = "Log in"
    
    def __init__(self,driver):
         self.driver = driver
         
    
    def enter_email_address(self,email_id):
        self.driver.find_element(By.ID,self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email_id)
    
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
        
    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_css).click()
    
    def click_login_link(self):
        self.driver.find_element(By.LINK_TEXT,self.link_login_linkText).click()
    
        
    