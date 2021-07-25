"""
FizzBuzz but using division or modulus is forebidden
A small program that takes an input number and counts to the input number (inclusive).
The program will print based on the following rules:
* If number is divisible by 3, print fizz
* If number is divisible by 5, print buzz
* If number is divisible by both 3 and 5, print fizzbuzz
* Otherwise, print the number
"""

def fizzBuzz(num):
    checkCount3 = 0
    checkCount5 = 0
    for i in range(0, num+1):
        flagCheck = False
        if checkCount3 == 3 and checkCount5 == 5:
            print("fizzbuzz")
            flagCheck = True
            checkCount3 = 0
            checkCount5 = 0
        if checkCount3 == 3:
            print("fizz")
            flagCheck = True
            checkCount3 = 0
        if checkCount5 == 5:
            print("buzz")
            flagCheck = True
            checkCount5 = 0
        if flagCheck == False:
            print(i)
        checkCount3 += 1
        checkCount5 += 1

def main():
    inputNum = 15
    fizzBuzz(inputNum)

main()
