a=list(map(int,input("enter the values:").split()))
b=[]
c=[]
for i in a:
    if i%2==0:
        print("even numbers",i)
        b.append(i)
    else:
        print("odd numbers",i)
        c.append(i)
print(f"even count:{sum(b)}")
print(f"odd count:{sum(c)}")
