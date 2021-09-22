# coding:utf8

from common.get_conf import get_conf
from common.get_logger import conf_path

def get_baseurl():
    base_url=get_conf("browser.ini","global","base-url")
    return base_url

base_url=get_baseurl()