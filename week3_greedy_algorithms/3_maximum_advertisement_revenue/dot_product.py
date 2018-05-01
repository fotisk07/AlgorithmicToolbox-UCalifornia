#Uses python3
import sys



def max_dot_product(a, b):
    res=0
    a2=a.sort()
    b2=b.sort()
    for i in range(0,n):
            res=res+a[i]*b[i]

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
