# Uses python3
def calc_fib(n):
    current=1
    previous=0
    if (n <= 1):
        return n

    for i in range(2,n+1):
        tmp_previous=previous
        previous=current
        current=(tmp_previous+ current) % 10
    return current
    

n = int(input())
print(calc_fib(n))
