#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''''''''
        @lvr_refine.py
        @Auther: Jim
'''''''''

import os

import numpy
import pandas as pd

dirs = [d for d in os.listdir("./data")]

dfs = []

for d in dirs:
    print(os.path.join("./data", d))
    df = pd.read_csv(os.path.join("./data", d), index_col=False)
    df['Q'] = d[-1]
    dfs.append(df.iloc[1:])

df = pd.concat(dfs, sort=True)

print (df)
