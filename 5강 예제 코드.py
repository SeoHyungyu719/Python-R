# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 10:06:01 2025

@author: miso4
"""

# if_test1.py
def if_test1 (x) :
 if (x % 2 == 0) :
   print ("x는 짝수입니다")
 else: 
   if (x % 2 == 1): 
     print("x는 홀수입니다")
   else:  
       print ("x는 자연수가 아닙니다")
# end function if.test

# if_test2.py
def if_test2 (x) :
 if (x % 2 == 0) :
   print ("x는 짝수입니다")
 elif (x % 2 == 1): 
   print("x는 홀수입니다")
 else:  
   print ("x는 자연수가 아닙니다")
# end function if.test

# pp.82 (for py)
mysum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    mysum = mysum + x**2
else:
    print(mysum)
    
 # whiletest1.py (pp. 84)
x = 1
sum = 0
while (x <= 10): 
  sum = sum + x**2
  x = x + 1
else:
  print(sum)
  
  ## pp. 86

x = range(1,6)
for j in x:   
    if (j == 3): continue
    print(j, " ")
else: 
    print("정상적인 반복종료")
 
x = range(1,6)
for j in x:   
   if (j == 3): break
   print(j, " ")
else: 
   print("정상적인 반복종료") 
   
   
 ## pp. 92
def sum2(x, y):
  mysum = x + y
  return(mysum)
  
#a = int(input("a=")); b=int(input("b="))
#print(a, "와", b, "의 합: ", sum2(a,b)) 

## pp. 92
# function_test1.py
def my_sums(a=0, b=10):
  import numpy as np
  sum1 = 0; sum2 = 0
  data = np.arange(a,b+1)
  for i in data: 
    sum1 = sum1 + i
    sum2 = sum2 + i**2
  return sum1, sum2, len(data)
# end of function my_sums
# try my_sums(1, 10) ; my_sums(); my_sums(b=100, a=0); my_sums(a=0, b=100)
  
a = my_sums(1,10)
mm = a[0]/a[2]
vv = (a[1] - a[2]*(mm**2)) / (a[2] - 1)

## pp. 97
class Student:
    def __init__(self, first, last):
        self.first = first        
        self.last = last

    def capital_first(self):
        return self.first.upper()
    
    
aa =Student('John', 'Doe')    
bb =Student('Jane', 'Doe')    

class StudentGrade(Student):
        def __init__(self, first, last, score):
            super().__init__(first,last)
            self.score =score
 
        def grade(self):
            if self.score < 80: 
                grade ='B'
            else:
                grade ='A'
            return grade

aa =StudentGrade('John', 'Doe',75)    
bb =StudentGrade('Jane', 'Doe', 95)