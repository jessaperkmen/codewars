'''
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''

def maxSequence(arr):  
    n = 0
    for i in range(1,len(arr)+1):
        for j in range(0,len(arr)-i+1):
            num = sum(arr[j:j+i])
            if num > n:
                n = num
            else:
                continue
    return n
    
    
    '''
    这段代码写的时候，真的有点蒙圈。逻辑有点混乱。但是一边写一边就清晰了。
    不得不说大神还是多，看了别人的代码，有的一行就解决了 哈哈。
    '''
