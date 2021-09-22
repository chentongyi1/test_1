# coding:utf8

import pytest
import time
from selenium.webdriver.common.keys import Keys
from pages.good_page import GoodPage
from common.get_driver import get_driver
from common.get_testdata import numberdatas1
from common.get_logger import logger

class TestPrice():
    def setup(self):
        self.driver=get_driver()
        self.good=GoodPage(self.driver)

    def teardown(self):
        self.good.driver_quit()

    @pytest.mark.parametrize("dict1",numberdatas1)
    def test_price(self,dict1):
        ele_number=self.good.get_ele_number()
        ele_price=self.good.get_ele_price()
        action=self.good.get_action()
        action.send_keys_to_element(ele_number,Keys.BACKSPACE).send_keys(dict1["number"]).perform()
        time.sleep(2)
        action=self.good.get_action()
        action.click(ele_price).perform()
        time.sleep(2)

        number=int(dict1["number"])
        if number<=0:
            logger.error("number必须大于0")
        elif number<5:
            assert str(1378*number) in ele_price.text
        else:
            assert str(1366*number) in ele_price.text

