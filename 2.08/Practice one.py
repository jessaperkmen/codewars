'''
This is the second part of this kata series. First part is here and the third is here

Add two English words together!

Implement a class Arith such that

  var k = new Arith("three");
  k.add("one hundred and two"); //this should return "one hundred and five"
Input - Will be between zero and five hundred and will always be in lower case. This input range applies to both the initial value upon object instantiation as well as the input for the add method.

Output - Word representation of the result of the addition. Should be in lower case

Word format - Both input and output shall be in the format 123 = one hundred and twenty three. No hyphen is needed in numbers 21-99. Words should also be separated with one space and no space padding is allowed.


'''


class Arith():
	def __init__(self,number):
		self.number = number
		self.zero = ['zero','one','two','three','four','five','six','seven','eight','nine']
		self.ten = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
		self.tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
		self.hundred = ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred',\
						'nine hundred','one thousand']
	def exchage(self,num):
		li = str(num).split(" ")
		if len(li) == 5:
			digit00 = self.hundred.index(li[0]+" "+li[1]) + 1
			digit00 = int(str(digit00)+'00')
			digit0 =  self.tens.index(li[3]) + 2
			digit0 =  int(str(digit0)+'0')
			digit =   self.zero.index(li[4])
			return digit00 + digit0 + digit
		elif len(li) == 4:
			digit00 = self.hundred.index(li[0]+" "+li[1]) + 1
			digit00 = int(str(digit00)+'00')
			if li[-1] in self.zero:
				digit = self.zero.index(li[-1])
			elif li[-1] in self.ten:
				digit = self.ten.index(li[-1]) + 10
			elif li[-1] in self.tens:
				digit = (self.tens.index(li[-1])+2)*10
			return digit00 + digit
		elif len(li) == 2:
			if 'hundred' in li:
				digit00 = self.hundred.index(li[0]+" "+li[1]) + 1
				digit00 = int(str(digit00)+'00')
				return digit00
			else:
				digit0 =  self.tens.index(li[0]) + 2
				digit0 =  int(str(digit0)+'0')
				digit =   self.zero.index(li[1])
				return digit0 + digit
		elif len(li) == 1:
			if li[0] in self.zero:
				digit = self.zero.index(li[0])
				return digit
			elif li[0] in self.ten:
				digit = self.ten.index(li[0]) + 10
				return digit
			else:
				digit = (self.tens.index(li[0]) + 2)*10
				return digit

	def unexchage(self,num):
		li = list(str(num))
		if len(li) == 3:
			text00 = self.hundred[int(li[0])-1]
			if li[1] == '0':
				if li[2] == '0':
					return text00
				text = self.zero[int(li[2])]
				return text00+' and '+text
			elif li[1] == '1':
				text = self.ten[int(li[2])]
				return text00+' and '+text
			elif li[1] != '1':
				text0 = self.tens[int(li[1])-2]
				if li[-1] == '0':
					return text00+' and '+text0
				text = self.zero[int(li[2])]
				return text00+' and '+text0+' '+text
		elif len(li) == 2:
			if li[0] == '1':
				text = self.ten[int(li[1])]
				return text
			elif li[0] != '1':
				text0 = self.tens[int(li[0])-2]
				if li[1] == '0':
					return text0
				else:
					text = self.zero[int(li[1])]
				return text0+' '+text
		elif len(li) == 1:
			text = self.zero[int(li[0])]
			return text
		elif len(li) == 4:
			return 'one thousand'
	def add(self,num):
		n = self.exchage(self.number)
		print(n)
		m = self.exchage(num)
		print(m)
		i = n + m
		print(i)
		return self.unexchage(i)

a = Arith('one hundred and sixty three')
print(a.add('thirty seven'))




'''
第一个比较有难度的项目，写了一个小时左右，逻辑很清晰，不过还是bug了 好多次，最后顺利运行。
这么多行代码，我已经迫不及待的想去看看别人是怎么写的了
'''
