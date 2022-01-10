def fact(x):
    fact = 1
    for i in range(2,x+1):
        fact = fact * i
    return fact

f1 = fact(5)
print(f1)