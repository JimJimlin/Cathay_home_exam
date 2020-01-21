#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''''''''
        @lvr_crawler.py
        @Usage: python lvr_crawler.py <config>
        @Auther: Jim
'''''''''

import os
import sys
import zipfile
import time

import configparser
import requests

config = configparser.ConfigParser()
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

    setting.year = list(config.get(setting_section, 'year').split(","))
    setting.season = list(config.get(setting_section, 'season').split(","))
    setting.region = list(config.get(setting_section, 'region').split(","))
    setting.type = int(config.get(setting_section, 'type'))

    type_code = mapping(setting.type)
    region_code = mapping(setting.region)

    for year in range(int(setting.year[0]),int(setting.year[1])+1):
      for season in setting.season:
          for region in region_code:
              print(year, season, region, type_code)
              real_estate_crawler(int(year), season, region, type_code)

def real_estate_crawler(year, season, region, type_code):

    folder = "data"
    if not os.path.isdir(folder):
        os.mkdir(folder)

    if year > 1000:
        year -= 1911

    request = ("https://plvr.land.moi.gov.tw//DownloadSeason?season={year}S{season}&fileName={region}_lvr_land_{type}.csv")\
    .format(year=year, season=season, region=region, type=type_code)

    data = requests.get(request)

    fname = ("./data/{year}S{season}_{region}_lvr_land_{type}.csv").format(year=year, season=season, region=region, type=type_code)
    file = fname
    open(file, 'wb').write(data.content)

    time.sleep(6)

def mapping(word):

    type_pattern = ("A", "B", "C") #A = 不動產買賣,B = 預售屋買賣,C = 不動產租賃
    region_pattern = {
    '基隆市' : 'C', '臺北市' : 'A', '新北市' : 'F', '桃園市' : 'H',
    '新竹市' : 'O', '新竹縣' : 'J', '苗栗縣' : 'K', '臺中市' : 'B',
    '南投縣' : 'M', '彰化縣' : 'N', '雲林縣' : 'P', '嘉義市' : 'I',
    '嘉義縣' : 'Q', '臺南市' : 'D', '高雄市' : 'E', '屏東縣' : 'T',
    '宜蘭縣' : 'G', '花蓮縣' : 'U', '臺東縣' : 'V', '澎湖縣' : 'X',
    '金門縣' : 'W', '連江縣' : 'Z'}

    if type(word) == int:
        word -=1
        return type_pattern[word]
    elif type(word) == list:
        word = [ region_pattern.get(item, item) for item in word ]
        return word

if __name__ == "__main__":
    main(sys.argv[1:])
