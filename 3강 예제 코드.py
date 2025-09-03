# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:39:01 2025

@author: miso4
"""

def meal(hungry : bool):
    if hungry:
        print("I am hungry");
    else:
        print("I am not hungry");
        
class Man: 
    def __init__(self, name):
        self.name = name
        print("Initialized")
    def hello(self):
        print("Hello " + self.name + " !")
    def goodbye(self):
        print("Goodbye " + self.name + " !")
        
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self) : 
        print(self.name)
        print(self.age)
        
        
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='-', label = 'cos')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('sin & cos')
plt.legend() # 옆 목차
plt.show()