lst = list(map(int,input("enter number:").split()))
for i in range(len(lst)-2):
  if lst[i] == lst[i+1] == lst[i+2]:
    print(lst[i])
