# Uses python3
import sys

def pisano(m):
    a=0
    b=1
    c=a+b
    for i in range(0,m*m):
        c=(a+b) % m
        a=b
        b=c
        if a==0 and b==1:
            return i+1
    


def solution(n,m):
    remainder= n%pisano(m)
    first=0
    second=1
    res=remainder

    for i in range(1,remainder):
        res=(first + second) % m
        first = second
        second=res

    return res
        
        

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(solution(n,m))
