'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
'''
def make_readable(seconds):
    SS = seconds % 60
    HH = seconds // 60 % 60
    MM = seconds // 60 // 60
    li = [MM,HH,SS]
    for i in li:
        if len(str(i)) == 1 :
            li[li.index(i)] = '0'+str(i)
            print(li)
        else:
          li[li.index(i)] = str(i)
    return ":".join(li)
    
'''
很简单的题,大神们写的代码都好短
'''
