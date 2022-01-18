# Numbers Divisible by Another Number
# Empty list
x = []
n = int(input("enter the limit: "))

for i in range(n):
    y = int(input("enter the number: "))
    x.append(y)

div = int(input("enter the div num: "))
res = list(filter(lambda z: z % div == 0,x))

print(res)