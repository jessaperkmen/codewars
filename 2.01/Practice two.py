'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

Calculate the row sums of this triangle from the row index (starting at index 1)
'''


def row_sum_odd_numbers(n):
    num = sum(range(n)) + 1
    a = 2 * num - 1
    m = 0
    for i in range(n):
        m += a
        a += 2
    return m
    
    
    
'''
最近codewars升到5级了，出现了好多很复杂的题目。。随意把题目等级调成了随机 哈哈。慢慢来吧
'''
