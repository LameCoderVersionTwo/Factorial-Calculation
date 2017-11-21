import sys
import functools
numberToBeFactorialed = int(input("Number to be reverse factorialed: "))
while True:
  endFactorial = numberToBeFactorialed / 2
  number2 = 2
  while endFactorial > 1:
    number2 = number2 + 1
    endFactorial= endFactorial / number2
    if endFactorial < 2 > 1:
      print("The reverse factorial of: ", numberToBeFactorialed, "is", endFactorial + number2 - 1)
      break
  break
