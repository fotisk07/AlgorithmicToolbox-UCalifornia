# Uses python3
import sys
import math

def binary_search(a,low,high, x):
    if high < low:
        return -1
    mid=low+math.ceil((high-low)/2)
    #print("mid is ",mid,"low is",low,"high is",high,"a is",a[mid],"x is",x)
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a,low,mid-1,x)
    else:
        return binary_search(a,mid+1,high,x)
    
    



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,0,n-1, x), end = ' ')
