num=int(input("number is:"))
if num>1:
    for i in range(2, (num//2)+1):
        if num%i==0:
            print("This not a prime number")
            break
    else:
        print(num,"This is prime number")
else:
    print("This not a prime number")