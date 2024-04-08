arr = [7,8,4,5]
for i in range(0,arr-1):
  for j in range(0,arr-1):
    if a[j] > a[j+1]:
      a[j],a[j+1] = a[j+1],a[j]
