#CALCULATOR APPLICATION

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
  if b==0:
    return "cannot divide with zero!"
  else:
    return a/b

while True:
    print("\n====Calculator Application====")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplcation")
    print("4.Division")
    print("5.Exit")
    
    choice=input("Enter your choice:")
    
    if choice=="5":
       print("Thankyou for using calculator!")
       break
    
    elif choice in["1","2","3","4"]:
        
       num1=float(input("Enter a first number:"))
       num2=float(input("Enter the second number:"))

       if choice=="1":
          print("Result:",add(num1,num2))
       elif choice=="2":
          print("Result:",subtract(num1,num2))
       elif choice=="3":
          print("Result:",multiply(num1,num2))
       elif choice=="4":
          print("Result:",divide(num1,num2))
    else:
       print("Invalid choice! Try again.")
