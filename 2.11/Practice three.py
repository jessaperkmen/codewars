'''
一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,请你帮助计算这个字符串的所有碎片的平均长度是多少。
'''
def fn(n):
	li = list(n)
	cu = 1
	while n:
		try:
			if li[0] == li[1]:
				li.pop(0)
			else:
				li.pop(0)
				cu += 1
		except:
			break
	print('%.2f'%(len(n)/cu))


'''
网易面试（三）
'''
