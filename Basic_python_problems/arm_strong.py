# Only positive integer are Arm strong numbers
# Arm strong using for loop and list comprehension
# Take input from user
x = int(input("enter the number: "))
# Take empty list
y = []
# use for loop
for i in str(x):
    y.append(int(i))
# store output in list1
list1 = y
# use list comprehension on list1
new = [n**3 for n in list1]
# sum the list
z = sum(new)

# sum is equal to x it is arm strong
if x == z:
    print("arm strong number")
else:
    print("it is not a arm strong number")