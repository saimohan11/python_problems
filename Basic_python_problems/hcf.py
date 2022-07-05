def hcf(x,y):
    if y == 0:
        return x
    else:
        return hcf(y,x%y)

print(hcf(12,14))

# define hcf
# pass two arguements x,y
# using set comprehension
def hcf(x,y): 
    x1 = {i for i in range(1,x+1) if x % i == 0}
    x2 = {j for j in range(1,y+1) if y % j == 0}
    y2 = x1.intersection(x2)
    print(max(y2))
    
hcf(54,24)