# find given number is positive or negative or zero

x = float(input("enter the number: "))

if x > 0:
    print("positive number")

elif x == 0:
    print("Given number is equal to zero")

elif x < 0:
    print("negative number")

else:
    print("entered wrong input")