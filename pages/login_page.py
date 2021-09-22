# coding:utf8

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from common.get_logger import logger

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(self.baseURL+"user.php")

    username_input=(By.NAME,"username")
    password_input=(By.NAME,"password")
    check_box=(By.NAME,"remember")
    login_button=(By.NAME,"submit")
    login_content=(By.XPATH,"//div[@class='boxCenterList RelaArticle']/div/p")

    def login(self,username,password,check_type=False):
        self.ele_sendkeys(self.username_input,username)
        self.ele_sendkeys(self.password_input,password)
        if check_type:
            self.ele_click(self.check_box)
        else:
            logger.info("不勾选保存登录信息")
        self.ele_click(self.login_button)

    def get_login_content(self):
        content=self.ele_find(self.login_content)
        return content