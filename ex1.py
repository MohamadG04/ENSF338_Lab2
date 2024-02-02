#1) This code is used to calculate the fibonacci sequence using recursion.

#2)  No it  isn’t  a divide and conquer algorithm because it computes the same fibonacci number multiple times instead of it splitting into independent sub-problems. Also, in the end of the function it doesn't combine all the results which is one of the main aspects of divide and conquer. 

#3) The time complexity of the algorithm is O(2^n) as everytime they split the problem into more and more functions so that it increases exponentially.

#4)

def fibonacci(n,meno={}):
    if n in meno:
        return meno[n]
    if n<=1:
        return n
    meno[n] = fibonacci(n-1,meno) + fibonacci(n-2,meno)
    return meno[n]

answer=fibonacci(15)
print(answer)
