# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:43:02 2025

@author: miso4
"""

import numpy as np
import pandas as pd

xv = ([1,2,3])
xv2 = xv #주소값 참조복사
xv3 = xv.copy() # 값의 복사


xv.append("added item")

xp = np.array(range(1,10))

xm = np.array([[1,2,3],[4,5,6],[7,8,9]])
xm2 = xm #참조복사
xm[0][0] = 10
ym = np.array([[1,2,3],[4,5,6],[7,8,9]])
ym2 = ym.copy() # 깊은복사
ym[0][0] = 10
xn = np.arange(1,10)
xn= xn.reshape(3, 3)

country_code = {'korea' : 82, 'us' : 1, 'china' : 86}
d = {'name': ['Kim', 'Lee', 'Park'], 'height': [170, 180, 175]}
df1 = pd.DataFrame(data=d)
print(df1)
df2 =  pd.DataFrame([['Kim', 170], ['Lee', 180], ['Park', 175]],
                    columns=['name', 'height'])
print(df2)
df3=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), 
                 columns=['a','b','c'])\
print(df3)