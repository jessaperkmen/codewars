'''
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
'''

import math
class Vector:
  def __init__(self,vec):
      self.__data = vec
      
  def equals(self,other):
      if self.__data == other.__data:
          return True
      else:
          return False
          
  def add(self,other):
      if len(self.__data) == len(other.__data):
          li = []
          for i,j in zip(self.__data,other.__data):
              li.append(i+j)
          return Vector(li)
      else:
          raise TypeError
          
  def subtract(self,other):
      if len(self.__data) == len(other.__data):
          li = []
          for i,j in zip(self.__data,other.__data):
              li.append(i-j)
          return Vector(li)
          
  def dot(self,other):
      if len(self.__data) == len(other.__data):
          li = []
          for i,j in zip(self.__data,other.__data):
              li.append(i*j)
          return sum(li) 
  
  def norm(self):
      li = []  
      for i in self.__data:
          li.append(i**2)
      return math.sqrt(sum(li))
  
  def __str__(self):
      return str(tuple(li))
          
        
