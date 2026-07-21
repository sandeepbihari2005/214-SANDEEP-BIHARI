def greatest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
print("the largest no is :",greatest(a,b,c))
