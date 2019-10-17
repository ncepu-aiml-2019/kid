def isfun(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for x in range(2,101):
    if isfun(x):
        print(x,end=" ")
        
