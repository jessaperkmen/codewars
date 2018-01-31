'''
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
'''


def expanded_form(num):
    n = 0
    li = []
    lis = list(str(num))
    lis.reverse()
    for i in lis :
        if i == '0':
            n += 1
            continue
        li.append(i+'0'*n)
        n += 1
    li.reverse()
    return " + ".join(li)
    
'''
列表的reverse 返回的是None  直接调用即可，不用赋值.....
'''
