import sys
import functools
numberToBeFactorialed = int(input("Number to be reverse factorialed: "))
endFactorial = numberToBeFactorialed / 1
if (endFactorial == numberToBeFactorialed):
  number1 = 0
  number2 = 1
  number2 = number2 + number1 + 1
  endFactorial = numberToBeFactorialed / number2
elif endFactorial < numberToBeFactorialed:
  number2 = number2 + 1
  endFactorial= endFactorial / number2
elif endFactorial < 1:
  print("The reverse factorial of: ", numberToBeFactorialed, "is", endFactorial)
else:
  print('Cant becalculated')
