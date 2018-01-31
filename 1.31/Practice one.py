'''
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1
'''


def binary_array_to_number(arr):
    return int("".join([str(x) for x in arr]),2)
    
    
    
'''
题目虽然很简单 ，但是是我第一个一行代码项目，哈哈
'''
