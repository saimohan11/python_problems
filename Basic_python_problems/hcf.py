def hcf(x,y):
    if y == 0:
        return x
    else:
        return hcf(y,x%y)

print(hcf(12,14))