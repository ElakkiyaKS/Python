d = {}
n = int(input())
for x in range(n):
  key = input()
  value = input()
  d[key]=value
  print(d)
print(sorted(d.values()))  
