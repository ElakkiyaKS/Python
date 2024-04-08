list=list(map(int,input("enter value").split()))
n = len(list)
if n%2 == 1:
    print(n//2)
else:
    print(n//2-1,n//2+1)
          
