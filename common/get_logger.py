# coding:utf8

import logging
import os

print(os.path.abspath(__file__))
project_path=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(project_path)
conf_path=os.path.join(project_path+"/conf/")
log_path=os.path.join(project_path+"/output/log/")
# print(log_path)
report_path=os.path.join(project_path+"/output/report/")
resources_path=os.path.join(project_path+"/resources/")
test_datas_path=os.path.join(project_path+"/test_datas/")

def get_logger():
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
    filehandler=logging.FileHandler(filename=log_path+"log.txt",mode="w",encoding="UTF-8")
    filehandler.setFormatter(formatter)
    filehandler.setLevel(logging.INFO)
    logger.addHandler(filehandler)
    streamhandler=logging.StreamHandler()
    streamhandler.setFormatter(formatter)
    streamhandler.setLevel(logging.ERROR)
    logger.addHandler(streamhandler)
    return logger


logger=get_logger()

# if __name__ == '__main__':
#     get_logger()
