def addition(x, y):
    return x + y 

def subtraction(x, y):
    return x - y 

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero is not allowed."
print("Choose your operations: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
        break
else:
    print("Invalid Input")
    
