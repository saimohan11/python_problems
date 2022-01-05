# To find quadratic equation 
# using quadratic eq formula

a = int(input("enter the number1:"))
b = int(input("enter the number2:"))
c = int(input("enter the number3:"))

d = (b**2-4*a*c)**0.5

sol1= (-b+d)/2*a
sol2 = (-b-d)/2*a

print("the quadratic eq{0} and{1}".format(sol1,sol2))

