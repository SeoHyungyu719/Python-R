# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 08:33:49 2025

@author: miso4
"""

# p.107

import datetime as dt

def birthyear():
  age = input("Enter age: ")
  now = dt.datetime.now()
  curyear = now.year
  b_year = curyear-int(age)
  print("born.year= ", b_year)

birthyear()


# p. 113
# fileio0.py
import pandas as pd

df1 = pd.read_csv('D:/대학/2학년 2학기/데이터분석/python_R/rpy/chap5_data/score.txt', sep=" ", header=0, encoding='utf-8')
df2 = pd.read_csv('D:/대학/2학년 2학기/데이터분석/python_R/rpy/chap5_data/score.csv', header=0, encoding='cp949')
df3 = pd.read_csv('D:/대학/2학년 2학기/데이터분석/python_R/rpy/chap5_data/score.csv', header=0, encoding='euc-kr')
print(df1.head(3))
print(df2.head(3))
print(df3.tail(3))
print(type(df1))

# 열의 일부만 읽기
df5 = pd.read_csv('D:/대학/2학년 2학기/데이터분석/python_R/rpy/chap5_data/score.csv', header=0, encoding='euc-kr',
                 usecols=['english', 'name', 'korean', 'math'])

# 열의 순서 바꾸기
df6 = pd.read_csv('D:/대학/2학년 2학기/데이터분석/python_R/rpy/chap5_data/score.csv', header=0, encoding='euc-kr',
                  usecols=['english', 'name', 'korean', 'math'])[['english', 'korean',
                               'math', 'name']]

#열을 name을 기준으로 구분                                                                  
#df7 = pd.read_csv('D:/대학/2학년 2학기/데이터분석/python_R/rpy/chap5_data/score.csv', sep=" ", index_col='name')
#print(df7.loc['강대성']) 강대성의 이름에 속해있는 데이터 출력
#print(df7.loc[0:]) 범위로 데이터를 잡음

#p. 119
from pandas import DataFrame

cars = {'make': ['Hyundai','Kia','Ford','Chevrolet'],
        'model': ['Sonata', 'K5', 'Taurus', 'Impala'],
        'price':  [3200,3100,3500,3700]         }

df = DataFrame(cars)
write_txt = df.to_csv (r'D:/대학/2학년 2학기/데이터분석/실습코드_서현규/cars_L6.txt',  sep = " ", 
                        index = True, header=True) 
