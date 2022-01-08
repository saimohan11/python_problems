# prime number using flag variable

x = int(input("enter the num: "))

# flag variable define to have one value until some condition is true

flag = False
if x > 1:
    for i in range(2,x):
        if (x%i == 0):
            flag = True
            break

if flag:
    print("{} is not a prime number".format(x))
else:
    print("{} is a prime number".format(x))

