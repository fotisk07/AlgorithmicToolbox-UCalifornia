# Uses python3
import sys

def gcd(a,b):
    if a<b:
        t=a
        a=b
        b=t

    while True:
        if b==0:
            return a
        remainder=a%b
        a=b
        b=remainder
    

   

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
    
