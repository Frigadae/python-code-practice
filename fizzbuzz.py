"""
A small program that takes an input number and counts to the input number (inclusive).
The program will print based on the following rules:
* If number is divisible by 3, print fizz
* If number is divisible by 5, print buzz
* If number is divisible by both 3 and 5, print fizzbuzz
* Otherwise, print the number
"""

def main(inputNum):
    for i in range(inputNum+1):
        if i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        else:
            print(i)

inputNum = input("Enter an integer: ")
main(int(inputNum))