import sys
import functools
while True:
  numberToBeFactorialed = int(input("Number to be reverse factorialed: "))
  endFactorial = numberToBeFactorialed / 2
  number2 = 2
  if endFactorial > 1:
    number2 = number2 + 1
    endFactorial= endFactorial / number2
    if endFactorial == 1:
      print("The reverse factorial of: ", numberToBeFactorialed, "is", number2)
  else:
    print('Cant be calculated')
  
