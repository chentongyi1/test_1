# coding:utf8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.get_logger import logger
from common.get_baseurl import base_url
from common.get_logger import log_path
import time

class BasePage():
    def __init__(self,driver):
        logger.info("base实例化开始")
        self.driver=driver
        # self.driver=webdriver.Chrome(executable_path="../resources/chromedriver.exe")
        self.driver.maximize_window()
        self.baseURL=base_url

    def get_screenshot(self,filename=None):
        logger.info("开始截图")
        date_time = time.strftime("%Y%m%d%H%M%S")
        if not filename:
            file=log_path+date_time+".png"
        else:
            file=log_path+filename+date_time+".png"
        self.driver.get_screenshot_as_file(filename=file)

    def ele_find(self,locator):
        ele=None
        logger.info("开始查找元素")
        wait=WebDriverWait(self.driver,10)
        try:
            wait.until(EC.presence_of_element_located(locator=locator))
            ele=self.driver.find_element(*locator)
            logger.info("元素{}的查找成功".format(locator))
        except Exception as err:
            logger.error("元素{}的查找失败".format(locator))
            self.get_screenshot(filename="eleFind")
            raise err
        finally:
            logger.info("元素查找结束")
        return ele

    def ele_click(self,locator):
        logger.info("元素click操作开始")
        ele=self.ele_find(locator=locator)
        wait=WebDriverWait(self.driver,10)
        if ele.is_enabled():
            try:
                wait.until(EC.element_to_be_clickable(locator=locator))
                ele.click()
                logger.info("元素{}的click操作成功".format(locator))
            except Exception as err:
                logger.error("元素{}的click操作失败".format(locator))
                self.get_screenshot(filename="eleClick")
                raise err
            finally:
                logger.info("元素click操作结束")
        else:
            logger.error("元素{}的click操作失败,该元素不能交互".format(locator))
            self.get_screenshot(filename="eleClick")
            logger.info("元素click操作结束")

    def ele_sendkeys(self,locator,parameters):
        logger.info("元素的send_keys操作开始!")
        ele=self.ele_find(locator=locator)
        if ele.is_enabled():
            try:
                ele.send_keys(parameters)
                logger.info("元素{}的send_keys操作成功".format(locator))
            except Exception as err:
                logger.error("元素{}的send_keys操作失败".format(locator))
                self.get_screenshot(filename="eleSendKeys")
                raise err
            finally:
                logger.info("元素的send_keys操作结束")
        else:
            logger.error("元素{}的send_keys操作失败，该元素不能交互".format(locator))
            self.get_screenshot(filename="eleSendKeys")
            logger.info("元素send_keys操作结束")

    def ele_clear(self,locator):
        logger.info("元素clear操作开始")
        ele = self.ele_find(locator=locator)
        if ele.is_enabled():
            try:
                ele.clear()
                logger.info("元素{}的clear操作成功".format(locator))
            except Exception as err:
                logger.error("元素{}的clear操作失败".format(locator))
                self.get_screenshot(filename="eleClear")
                raise err
            finally:
                logger.info("元素clear操作结束")
        else:
            logger.error("元素{}的clear操作失败,该元素不能交互".format(locator))
            self.get_screenshot(filename="eleClear")
            logger.info("元素clear操作结束")

    def get_alert(self):
        logger.info("开始获取JS弹框")
        alert=None
        wait=WebDriverWait(self.driver,10)
        try:
            wait.until(EC.alert_is_present())
            alert=self.driver.switch_to.alert
            logger.info("获取JS弹框成功")
        except Exception as err:
            logger.error("获取JS弹框失败")
            self.get_screenshot(filename="getAlert")
            raise err
        return alert


    def driver_quit(self):
        self.driver.quit()


    def add_cookie1(self):
        self.driver.add_cookie({"name":"ECS_ID","value":"79837d145cbb94ee7c0100ee5660949cb56d6211"})