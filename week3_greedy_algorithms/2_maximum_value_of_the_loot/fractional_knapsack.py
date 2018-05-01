# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    A=[0]*100000
    C=[0]*1000

    for i in range(0,n):
        if capacity == 0:
            return value 
        for j in range(0,n):
            if weights[j]> 0:
                C[j]=values[j]/weights[j]
        ab=max(C)
        i=C.index(ab)
        a=min(weights[i], capacity)
        value=value+a*ab
        weights[i]=weights[i]-a
        A[i]=A[i] + a
        capacity=capacity-a
        C=[0]*1000
    return value
    

    

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    print (weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
