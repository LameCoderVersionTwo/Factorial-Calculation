maxNumber = int(input('What will the maximum count be? (any large numbers over 500k may take a while to calculate): '))
numberIncrease = int(input('What will be the number added per round?(any small numbers in proportion to maximum count may take a very long time): '))
number1 = 0
while (number1 < maxNumber):
	import sys
	number2=number1+1
	number1=number1+numberIncrease
	multipliers=list()
	import datetime
	now = datetime.datetime.now()
	sys.stdout=open("Factorial.txt","a")
	print ("Start time", now.strftime('%H%m%S.%f'))
	import sys
	sys.stdout.close()
	for i in range(number1,0,-1):
			multipliers.append(i)
			#print(i)
	import operator
	import functools
	import decimal
	result = functools.reduce(operator.mul,multipliers, 1)
	import datetime
	now1 = datetime.datetime.now()
	sys.stdout=open("Factorial.txt","a")
	print ("End time", now1.strftime('%H%m%S.%f'))
	sys.stdout.close()
	x = decimal.Decimal(result)
	sys.stdout=open("Factorial.txt","a")
	print("Factorial of", number1, "is", format(x, '.6e'))
	sys.stdout.close()
	sys.stdout=open("Factorial.txt","a")
	print("The time difference is", (now1 - now).total_seconds(), "seconds")
	sys.stdout.close()
