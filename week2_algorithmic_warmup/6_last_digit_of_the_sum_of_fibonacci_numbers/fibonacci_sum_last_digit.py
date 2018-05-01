# Uses python3
import sys

def fibonacci_sum(n):
    current=1
    previous=0
    sum=1
    if (n <= 1):
        return n

    for i in range(2,n+1):
        tmp_previous=previous
        previous=current
        current=(tmp_previous+ current) % 10
        sum=(sum+current) % 10
        
        
    return sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
