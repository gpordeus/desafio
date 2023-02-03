def fib(n):
    if n < 0 or not isinstance(n, int):
        return None
    if n < 2:
        return n

    older = 0
    old = 1
    for i in range(2, n+1):
        j = older
        older = old
        old = old + j
    return old

def recursiveFib(n):
    if n < 0 or not isinstance(n, int):
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursiveFib(n-1) + recursiveFib(n-2)

fibDict = {0:0, 1:1}
def linearFib(n):
    if n < 0 or not isinstance(n, int):
        return None

    if n not in fibDict:
        fibDict[n] = linearFib(n-1) + linearFib(n-2)
    
    return fibDict[n]
    

def test (f, n):
    for i in range(n):
        print(f(i))


test(fib, 20)
print()
test(recursiveFib, 20)
#print()
#test(linearFib, 20)
