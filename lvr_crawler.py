#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''''''''
        @lvr_crawler.py:
        @
        @Usage: python lvr_crawler.py <integrity_category>
'''''''''

import requests
import os
import zipfile
import time
import ConfigParser

config = ConfigParser.ConfigParser()
setting_section = 'setting'

class Setting:
    def __init__(self):
        self.config_file = ''
        self.year = ''
        self.season = ''
        self.region = ''
        self.type = ''

setting = Setting()

def main(argv):

    setting.config_file = argv[0]

    config.read(setting.config_file)

    setting.year = config.get(setting_section, 'year')
    setting.season = config.get(setting_section, 'season')
    setting.region = config.get(setting_section, 'region')
    setting.type = config.get(setting_section, 'type')
    DBDataExport(setting)

def real_estate_crawler(year, season):
    if year > 1000:
        year -= 1911

    CuteBB = requests.get("https://plvr.land.moi.gov.tw//DownloadSeason?season=108S3&type=zip&fileName=lvr_landcsv.zip")

    fname = 'BB.zip'  #str(year)+str(season)+'.zip'
    open(fname, 'wb').write(CuteBB.content)

    folder = 'real_estate' + str(year) + str(season)
    if not os.path.isdir(folder):
        os.mkdir(folder)

    # extract files to the folder
    with zipfile.ZipFile(fname, 'r') as zip_ref:
        zip_ref.extractall(folder)

    time.sleep(10)

if __name__ == "__main__":
    main(sys.argv[1:])

# real_estate_crawler(101, 3)
# real_estate_crawler(101, 4)
#
# for year in range(102, 108):
#   for season in range(1,5):
#     print(year, season)
#     real_estate_crawler(year, season)
#
# real_estate_crawler(108, 1)
# real_estate_crawler(108, 2)


# A - 不動產買賣
# B - 預售屋買賣
# C - 不動產租賃

# C - 基隆市
# A - 臺北市
# F - 新北市
# H - 桃園市
# O - 新竹市
# J - 新竹縣
# K - 苗栗縣
# B - 臺中市
# M - 南投縣
# N - 彰化縣
# P - 雲林縣
# I - 嘉義市
# Q - 嘉義縣
# D - 臺南市
# E - 高雄市
# T - 屏東縣
# G - 宜蘭縣
# U - 花蓮縣
# V - 臺東縣
# X - 澎湖縣
# W - 金門縣
# Z - 連江縣
