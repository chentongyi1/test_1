# coding:utf8

import configparser
from common.get_logger import conf_path

def get_conf(file,section,option):
    conf=configparser.ConfigParser()
    conf.read(filenames=conf_path+file)
    return conf[section][option]
