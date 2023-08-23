def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}" + "\n")


def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}" + "\n")
    
def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}" + "\n")
    
def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}" + "\n")

while True:
    print("A. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice:  ").upper()


    if choice == "A":
        print("Addition")   
        a = int(input("input first number: ")) 
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "S":
        print("Subtraction")
        a = int(input("input first number: ")) 
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "M":
        print("Multiplication")
        a = int(input("input first number: ")) 
        b = int(input("input second number: "))
        mul(a, b)
    elif choice == "D":
        print("Division")
        a = int(input("input first number: ")) 
        b = int(input("input second number: "))
        div(a, b)    
    elif choice == "E":
        print("Exiting")
        quit()    
    else :
        print("you entered wrong input!! try again!!" + "\n")    