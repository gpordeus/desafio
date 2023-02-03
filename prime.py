primeDict = {0:0, 1:1}
def isPrime(n):
    for i in range(2, n+1//2):
        if n%i==0:
            return False
    return True


def primes(n):
    if n < 2 or not isinstance(n, int):
        return []

    returnList = []
    for i in range(2,n+1):
        if isPrime(i):
            returnList.append(i);
    return returnList

def recursivePrimes(n):
    if n < 2 or not isinstance(n, int):
        return []

    if n == 2:
        return [2]

    if isPrime(n):
        return recursivePrimes(n-1) + [n]
    else:
        return recursivePrimes(n-1)


print(primes(1000))
print()
print(recursivePrimes(900))