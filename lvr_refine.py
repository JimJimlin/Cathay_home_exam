#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''''''''
        @lvr_refine.py
        @Auther: Jim
'''''''''

import os
import re

import numpy
import pandas as pd

def main():

    dirs = [d for d in os.listdir("./data") if d.endswith(".csv")]
    dfs = []

    for d in dirs:

        matches = re.findall(r'(?P<year>\d{3})S(?P<season>\d)_(?P<region>\w)_lvr_land_(?P<type>\w)', d)
        df_name = ("{year}_{season}_{region}_{type}").\
        format(year=matches[0][0],season=matches[0][1],region=matches[0][2],type=matches[0][3])

        df = pd.read_csv(os.path.join("./data", d), index_col=False, header=1)
        df['df_name'] = df_name
        dfs.append(df.iloc[0:])
        df = pd.concat(dfs, sort=True)

    df.to_csv("df_all.csv", encoding='utf-8')

if __name__ == "__main__":
    main()
