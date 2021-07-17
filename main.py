import math

print("Welcome to Mathe World")
print('''Let's do calculation.....\n
A - Addition\n
S - Subtraction\n
M - Multiplication\n
D - Division\n
E - Exponential\n
SR - Square Root\n
CR - Cube Root\n
ID - Integer Division\n
R - Modulus\n
RD - Round\n
F - Factorial\n
Sin - Sin Value\n
Cos - Cos Value\n
Tan - Tan Value\n
Deg - Degree\n
Rad - Radians\n
Log - Logarithm base 2\n
0 - exit\n\n''')
while True :
  ch=input("Enter your Choice : ")
  if(ch=="0"):
    print("Thanks for using...!")
    break
  else:
    if(ch=="A" or ch=="a"):
      a=int(input("Enter num 1 : "))
      b=int(input("Enter num 2 : "))
      print("Result is ",a+b)
    if(ch=="S" or ch=="s"):
      a=int(input("Enter num 1 : "))
      b=int(input("Enter num 2 : "))
      print("Result is ",a-b)
    if(ch=="M" or ch=="m"):
      a=int(input("Enter num 1 : "))
      b=int(input("Enter num 2 : "))
      print("Result is ",a*b)
    if(ch=="D" or ch=="d"):
     a=int(input("Enter num 1 : "))
     b=int(input("Enter num 2 : "))
     print("Result is ",a/b)
    if(ch=="E" or ch=="e"):
      a=int(input("Enter num : "))
      b=int(input("Power value : "))
      print("Result is ",pow(a,b))
    if(ch=="SR" or ch =="sr"):
      a=int(input("Enter num : "))
      print("Result is ",math.sqrt(a))
    if(ch=="CR" or ch=="cr"):
      a=int(input("Enter num: "))
      print("Result is ",a ** (1. / 3))
    if(ch=="ID" or ch=="id"):
      a=int(input("Enter num 1 : "))
      b=int(input("Enter num 2 : "))
      print("Result is ",a//b)
    if(ch=="R" or ch=="r"):
      a=int(input("Enter num 1 : "))
      b=int(input("Enter num 2 : "))
      print("Result is ",a%b)
    if(ch=="RD" or ch=="rd"):
      a=int(input("Enter num : "))
      b=int(input("Enter the digits to be rounded: "))
      print("Result is ",round(a,b))
    if(ch=="F" or ch=="f"):
      a=int(input("Enter a number : "))
      print("Result is ",math.factorial(a))
    if(ch=="Sin" or ch=="sin"):
      a=int(input("Enter a number : "))
      print("Result is ",math.sin(a))
    if(ch=="Cos" or ch=="cos"):
      a=int(input("Enter a number : "))
      print("Result is ",math.cos(a))
    if(ch=="Tan" or ch=="tan"):
      a=int(input("Enter a number : "))
      print("Result is ",math.tan(a))
    if(ch=="Deg" or ch=="deg"):
      a=int(input("Enter a number : "))
      print("Result is ",math.degrees(a))
    if(ch=="  Rad" or ch=="rad"):
      a=int(input("Enter a number : "))
      print("Result is ",math.radians(a))
    if(ch=="Log" or ch=="log"):
      a=int(input("Enter a number : "))
      b=int(input("Enter base value : "))
      print("Result is ",math.log(a,b))