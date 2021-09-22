# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

class GoodPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(self.baseURL+"goods.php?id=1")
        self.add_cookie1()
        self.driver.get(self.baseURL+"goods.php?id=1")

    number_input=(By.NAME,"number")
    final_price=(By.ID,"ECS_GOODS_AMOUNT")

    def get_ele_number(self):
        ele=self.ele_find(self.number_input)
        return ele
    def get_ele_price(self):
        ele=self.ele_find(self.final_price)
        return ele

    def get_action(self):
        action=ActionChains(self.driver)
        return action


# if __name__ == '__main__':
#     driver=webdriver.Chrome(executable_path="../resources/chromedriver.exe")
#     g=GoodPage(driver)