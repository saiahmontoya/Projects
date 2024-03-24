'''
Saiah Montoya
CECS 342
Prog Assignment 1 Fibonacci Race
9/12/23

I certify that this program is my own original work. I did not copy any part of this program from
any other source. I further certify that I typed each and every line of code in this program.
'''

import time

total = 0
def fibo(n):
    global total
    total = total + 1
    if n == 1 or n == 0: 
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

    
for n in range(51):
    start = time.time()
    total = fibo(n)
    end = time.time()

    t = end - start
    print(n," : ", total, " Time Taken: ", t)
    