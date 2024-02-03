#1) This code is used to calculate the fibonacci sequence using recursion.

#2)  No it  isn’t  a divide and conquer algorithm because it computes the same fibonacci number multiple times instead of it splitting into independent sub-problems. Also, in the end of the function it doesn't combine all the results which is one of the main aspects of divide and conquer. 

#3) The time complexity of the algorithm is O(2^n) as everytime they split the problem into more and more functions so that it increases exponentially.

#4)

import timeit

import matplotlib.pyplot as plt
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) +fibonacci(n-2)
    


time_taken_original = []
time_taken_memo = []


def fibonaciNew(n,meno={}):
    if n in meno:
        return meno[n]
    if n<=1:
        return n
    meno[n] = fibonaciNew(n-1,meno) + fibonaciNew(n-2,meno)
    return meno[n]

for i in range(0,35):
    fibonacci(i)
    time_taken= timeit.timeit(lambda:fibonacci(i),number=100)
    time_taken_original.append(time_taken)
    fibonaciNew(i)
    time_taken_new = timeit.timeit(lambda:fibonaciNew(i,meno={}), number=100)
    time_taken_memo.append(time_taken_new)
plt.figure(figsize=(10,6))
plt.plot(time_taken_original,label="original", marker="o")
plt.title('Fibonacci Computation Time Comparison')
plt.xlabel('n-th Fibonacci Number')
plt.ylabel('Time (seconds)')
plt.show()
plt.figure(figsize=(10,6))
plt.plot(time_taken_memo,label="Optimizedf", marker="x")
plt.title('Fibonacci Computation Time Comparison')
plt.xlabel('n-th Fibonacci Number')
plt.ylabel('Time (seconds)')
plt.show()




#5  The new time comp[lexityy after using memoization is O(n) because each value is only computed once.

#6


