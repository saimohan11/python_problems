x = int(input("enter the 1st number: "))
y = int(input("enter the 2nd number:"))

def add():
    print(x + y)

def sub():
    print(x - y)

def mul():
    print(x * y)

def div():
    print(x / y)

def pow():
    print(x ** y)

def sqrt():
    print(x ** 0.5)

while True:
    print("select the operation 1.add 2.sub 3.mul 4.div 5.pow 6.sqrt 7.quit")
    choice = int(input("enter the operation"))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        pow()
    elif choice == 6:
        sqrt()
    elif choice == 7:
        break
    else:
        print("select the correct operation")
