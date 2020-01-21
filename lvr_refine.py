#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''''''''
        @lvr_refine.py
        @Auther: Jim
'''''''''

import os
import re
import string
import csv

import numpy
import pandas as pd

def main():

    dirs = [d for d in os.listdir("./data") if d.endswith(".csv")] #找尋所有資料
    dfs = []

    for d in dirs:

        matches = re.findall(r'(?P<year>\d{3})S(?P<season>\d)_(?P<region>\w)_lvr_land_(?P<type>\w)', d)

        df_name = ("{year}_{season}_{region}_{type}").\
        format(year=matches[0][0],season=matches[0][1],region=matches[0][2],type=matches[0][3])

        df = pd.read_csv(os.path.join("./data", d), index_col=False, header=1)
        df['df_name'] = df_name #新增df_name欄位
        dfs.append(df.iloc[0:])
        df = pd.concat(dfs, sort=True) #結合所有df

    #不動產買賣資料 總樓層為中文數字
    df['total floor number'] = df['total floor number'].str.replace("層","")
    df['total floor number'] = df['total floor number'].str.replace("地下","0")
    df['total floor number'] = df['total floor number'].str.replace("五十","5")
    df['total floor number'] = df['total floor number'].str.replace("四十","4")
    df['total floor number'] = df['total floor number'].str.replace("三十","3")
    df['total floor number'] = df['total floor number'].str.replace("二十","2")
    df['total floor number'] = df['total floor number'].str.replace("十","1")
    df['total floor number'] = df['total floor number'].str.translate(str.maketrans({'一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}))
    df['total floor number'] = df['total floor number'].fillna(0).astype(int)

    mask1 = df["building state"].str.contains(pat = '住宅大樓')
    mask2 = df["main use"] == "住家用"
    mask3 = df['total floor number'] >= 13
    df = df[(mask1 & mask2 & mask3)] # 篩選條件
    df.to_csv("./summary/filter.csv", index=False)

    total_count = df.shape[0]

    pk = 0 #停車位初始值
    for i in df['transaction pen number']:
        count = re.findall(r"土地\d建物\d車位(?P<stats>\d)",i)
        try:
            pk += int(count[0])
        except:
            pass
    parking_count = pk

    mean_price = df['total price NTD'].mean()
    mean_parkingprice = df['the berth total price NTD'].mean()

    target_write = open("./summary/count.csv", 'a+')
    w = csv.writer(target_write)
    w.writerow(['總件數', '總車位數', '平均總價元', '平均車位總價元'])
    w.writerow([total_count, parking_count, mean_price, mean_parkingprice])

if __name__ == "__main__":
    folder = "summary"
    if not os.path.isdir(folder):
        os.mkdir(folder)
    main()
