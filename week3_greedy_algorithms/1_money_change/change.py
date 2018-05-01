# Uses python3
import sys
import time



def get_change(m):
    count=0
    sum1=0
    while True:
        if sum1 + 10 <= m:
            sum1=sum1 + 10
            count=count + 1
        elif sum1 + 5 <= m:
            sum1=sum1  + 5
            count=count + 1
        else:
            count=count+(m-sum1)
            sum1=m
            
        
        if sum1==m:
            return count
                 

if __name__ == '__main__':
    m = int(sys.stdin.read())
    start = time.time()
    print(get_change(m))
    end = time.time()
    print(end - start)





