# coding:utf8

from selenium import webdriver
from common.get_conf import get_conf
from common.get_logger import logger
from common.get_logger import resources_path

def get_driver():
    driver=None
    browser_type=get_conf("browser.ini","driver","browser-type")
    waittime=get_conf("browser.ini","driver","waittime")
    try:
        if browser_type=="chrome":
            executable_path=resources_path+"chromedriver.exe"
            driver=webdriver.Chrome(executable_path=executable_path)
        elif browser_type=="firefox":
            executable_path=resources_path+"geckodriver.exe"
            driver=webdriver.Firefox(executable_path=executable_path)
        elif browser_type=="ie":
            executable_path=resources_path+"IEDriverServer.exe"
            driver=webdriver.Ie(executable_path=executable_path)
        else:
            logger.error("出现错误")
            raise Exception("请检查浏览器配置文件browser.ini中的浏览器类型browser-type")
    except Exception as err:
        raise err
    driver.implicitly_wait(waittime)
    return driver

if __name__ == '__main__':
    get_driver()


