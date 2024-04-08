num = int(input("enter number:"))
if num == 1:
    print("it is not prime number")
elif num > 1:
    for i in range(2,num):
        if i%num == 0:
            print("it is not prime number")
else:
    print("it is prime number")
