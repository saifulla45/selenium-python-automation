import time
import pytest
from selenium import webdriver
from pages.login_admin_page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker

class Test_Admin_Login:
    admin_page_url =  Read_config.get_page_url()
    username = Read_config.get_email_id()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_email_id()
    logger = Log_Maker.log_generator()
    
    def test_title_verification(self,setup):
        self.logger.info("****** Start Execution of test_title_verification Test Method ********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.logger.info("Entered the URL")
        time.sleep(4)
        actual_title = self.driver.title
        self.logger.info("Got the Title of the Text")
        expected_title = "Demo Web Shop"
        if actual_title == expected_title:
            assert True
            self.logger.info("assertion for title passed")
            self.driver.close()
        else:
            self.driver.close()
            assert False
            
    def test_valid_login(self,setup):
        self.logger.info("****** Start Execution of test_valid_login Test Method ********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_loginPage = Login_Admin_Page(self.driver)
        self.admin_loginPage.click_login_link()
        self.logger.info("Clicked on Login Link")
        time.sleep(3)
        self.admin_loginPage.enter_email_address(self.username)
        self.logger.info("Entered Email Address")
        self.admin_loginPage.enter_password(self.password)
        self.logger.info("Entered Password Address")
        self.admin_loginPage.click_login_button()
        self.logger.info("Clicked on Login Button")
        time.sleep(2)
        email_text = self.driver.find_element(By.XPATH,"//div[@class='header-links']/ul/li[1]/a").text
        
        if email_text == self.username:
            self.logger.info("Assertion for the email text Match is passed")
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.quit()
            assert False
            
    def test_invalid_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_loginPage = Login_Admin_Page(self.driver)
        self.logger.info("Clicking on Login Link")
        self.admin_loginPage.click_login_link()
        time.sleep(3)
        self.logger.info("Entering Email Address")
        self.admin_loginPage.enter_email_address(self.invalid_username)
        self.logger.info("Entering password Address")
        self.admin_loginPage.enter_password(self.password)
        self.logger.info("Going to click on Login Button")
        self.admin_loginPage.click_login_button()
        time.sleep(2)
        email_text = self.driver.find_element(By.XPATH,"//div[@class='validation-summary-errors']//li").text
        
        if email_text == "No customer account found":
            self.logger.info("ASSERTION PASSED")
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            self.driver.quit()
            assert False