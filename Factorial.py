import sys
import datetime
import operator
import functools
import decimal
maxNumber = int(input('What will the maximum count be?: '))
#This number will dictate how long the program will go (suggested under 100k or it may #take large amounts of time
numberIncrease = int(input('What will be the number added per round?: '))
#the code starts at zero and adds this number to the previous number to calculate the
#factorial of the number
number1 = 0
while (number1 < maxNumber):
	now = datetime.datetime.now()
	number2=number1+1
	number1=number1+numberIncrease
	multipliers=list()
	for i in range(number1,0,-1):
			multipliers.append(i)
	result = functools.reduce(operator.mul,multipliers, 1)
	x = decimal.Decimal(result)
	now1 = datetime.datetime.now()
	sys.stdout=open("Factorial.txt","a")
	print ("Start time", now.strftime('%H%m%S.%f'))
	print ("End time", now1.strftime('%H%m%S.%f'))
	print("Factorial of", number1, "is", format(x, '.6e'))
	print("The time difference is", (now1 - now).total_seconds(), "seconds")
	sys.stdout.close()
