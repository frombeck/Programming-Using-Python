max=int(input("Find primes upto what numbers?"))
primeList=[]
for x in range(2,max+1):
    isPrime=True
    for y in range(2,int(x**0.5)+1) :
        if x%y==0:
            isPrime=False
            break

    if isPrime:
        primeList.append(x)
print(primeList)
