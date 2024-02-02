import timeit
import cProfile

def sub_function(n):
    # sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

# 1. What is a profiler, and what does it do? [0.25 pts]
# A profiler is a tool used to analyze the runtime behavior of a program. It measures the execution time of functions and statements, providing insights into performance bottlenecks.

# 2. How does profiling differ from benchmarking? [0.25 pts]
# Profiling involves analyzing the runtime behavior of a program to identify performance bottlenecks. Benchmarking, on the other hand, is the process of comparing the performance of different systems or components.

# 3. Use a profiler to measure execution time of the program (skip function definitions) [0.25 pt]
# Using cProfile to profile the execution time of the program
if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    test_function()
    third_function()

    profiler.disable()
    profiler.print_stats(sort='cumulative')

# 4. Discuss a sample output. Where does execution time go? [0.25 pts]
# Sample output may show the cumulative time spent in each function, helping identify performance bottlenecks. The "cumulative" column in the output reveals the total time spent in each function, indicating where the majority of the execution time goes. Functions with higher cumulative time may require optimization.
