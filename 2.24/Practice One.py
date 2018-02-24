'''
求导
'''

def derivative(eq):
	eq = eq.split("+")
	print(eq)
	#去掉常数项
	try:
		num = int(li[-1])
		li.pop()
		eq = list("+".join(li))
	except:
		eq = list(eq)
	print(eq)
	#去掉一次幂的X
	Change = True
	while Change:
		for index,i in enumerate(eq):
			try:
				if i == "x" and eq[index+1] == "+" :
					eq.pop(index)
					Change = True
					break
			except:
				eq.pop(index)
				Change = True
				break
		else:
			Change = False
			break
	#X幂数前置
	Change = True
	while Change:
		for index,i in enumerate(eq):
				if i == "^" :
					try:
						if int(eq[index-2]):
							if index-2 >= 0:
								eq[index-2] = str(int(eq[index+1])*int(eq[index-2]))
								eq[index] = "_"
							else:
								eq.insert(index-1,eq[index+1])
								Change = True
								eq[index+1] = "_"
								break
					except:

						eq.insert(index-1,eq[index+1])
						Change = True
						eq[index+1] = "_"
						break
		else:
			Change = False
			break
	#幂数减一
	for index,i in enumerate(eq):
			if i == "_" :
				eq[index] = '^'
				eq[index+1] = str(int(eq[index+1]) - 1)
	#幂数是否是一检查
	Change = True
	while Change:
		for index,i in enumerate(eq):
				if i == "^" and eq[index+1] == "1":
					eq.pop(index)
					eq.pop(index)
					Change = True
					break
		else:
			Change = False
			break
	return "".join(eq)
