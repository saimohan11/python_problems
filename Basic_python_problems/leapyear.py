# leap year are not check

# Taking x as year
x = int(input("enter the year: "))

# if given number divisible by 100 and 400 then it is a leap year
if (x%100 == 0) and (x%400 == 0):
    print("{} is a leap year".format(x))

# if given num is div by 4 but it is not div by 100 u can consider as a leap year
elif (x%4 == 0) and (x%100 != 0):
    print("{} is a leap year".format(x))

else:
    print("{} is not a leap year".format(x))
