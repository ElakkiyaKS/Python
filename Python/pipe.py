lst = list(map(int,input().split()))
ip = list(map(int,input().split()))
op = list(map(int,input().split()))
a = lst[2]
if sum(ip) > sum(op):
    print(sum(ip)-2)
elif sum(ip) < sum(op):
    print(
