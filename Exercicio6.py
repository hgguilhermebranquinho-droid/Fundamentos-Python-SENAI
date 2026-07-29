num1 = input("digite um numero")
num2 = input("digite outro numero")
num3 = input("digite mais um numero")
if num1 <= num2 <= num3:
    print(f"{num1,num2,num3}")
elif num2 <= num3 <= num1:
    print(f"{num2,num1,num3}")
elif num3 <= num2 <= num1:
    print(f"{num3,num2,num1}")
elif num1 <= num3 <= num2:
    print(f"{num1,num3,num2}")
elif num3 <= num1 <= num2: 
    print(f"{num3,num1,num2}")
elif num2 <= num1 <= num3:
    print(f"{num2,num1,num3}")
else:
    print("impossivel")
