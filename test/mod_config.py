#encoding:utf-8
#name:mod_config.py

import ConfigParser
import os

#获取config配置文件
def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/stock.conf'
    config.read(path)
    return config.get(section, key)

