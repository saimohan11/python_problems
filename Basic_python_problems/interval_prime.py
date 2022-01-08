x = int(input("enter the num: "))
y = int(input("enter the num2: "))

# iterate over x ,y using for loop
for i in range(x,y+1):
    
    # then prime number codition only one factor only 1
    if i > 1:
        for z in range(2,i):
            if (i%z == 0):
                break

        else:
            print(i)
