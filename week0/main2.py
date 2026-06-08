name = input("What is your name? \n")
greeting = f"Hi {name}"
print(greeting)

numbers = input("Enter your numbers: \n")
#2+2.split()--->["2","+","2"]
number1,number2 = numbers.split()
number1 = int(number1)
number2 = int(number2)

opration = input("Enter your operation (+,-,/,%,x,**): \n")

if opration == "+":
    print(number1+number2)
elif opration == "-":
    print(number1-number2)
elif opration == "/":
    print(number1/number2)
elif opration == "%":
    print(number1%number2)
elif opration == "x":
    print(number1*number2)
elif opration == "**":
    print(number1**number2)
else:
    print("Invalid operation")