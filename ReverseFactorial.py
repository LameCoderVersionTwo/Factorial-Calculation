import sys
import functools
import decimal
type = input("exponent, or normal (e or n)")
if type == "normal" or type == "n":
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
  
elif type == "exponent" or type == "e":
      number1 = int(input("Number below the exponent: "))
      exponent1 = int(input("Exponent: "))
      while True:
        numberToBeFactorialed = number1 ** exponent1
        endFactorial = numberToBeFactorialed / 2
        number2 = 2
        while endFactorial > 1:
          number2 = number2 + 1
          endFactorial= endFactorial / number2
          if endFactorial < 2 > 1:
            print("The reverse factorial of: ", numberToBeFactorialed, "is", endFactorial + number2 - 1)
            break
        break
else:
  print ("Please input as 'exponent' or 'normal'")
