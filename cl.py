### predifined, and custom functions.
### print=predifined and input=predifined
### def=custom
number1=int(input("enter a number "))
oprations=input("enter any opretion sign divide(/),sutract(-),add(+),multiply(*) ") 
number2=int(input("enter another number "))


if oprations== "+":
    print(number1 + number2)
elif oprations== "/":
    print(number1/number2)
elif oprations== "-":
    print(number1-number2)
elif oprations== "*":
    print(number1*number2)
else:
    print("that's not a valid opration, please try another one")






