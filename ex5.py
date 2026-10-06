x=int(input("Enter x:"))
y=int(input("Enter y:"))

M=max(x,y)
m=min(x,y)
r=M%m

while r!=0:
    M=m
    m=r
    r=M%m

print("GCD:",m)
