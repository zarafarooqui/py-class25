def numberOfBits(n):
    count = 0
    while(n):
        count +=1
        n>>=1
    return count

n=int(input("Enter your number:"))
print("Numbers of bits:", numberOfBits(n))
