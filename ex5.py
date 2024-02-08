import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def measure_performance(search_function, vector_size):
    vector = np.arange(vector_size)
    times = []

    for _ in range(1000):
        target = np.random.randint(0, vector_size)
        time_taken = timeit.timeit(lambda: search_function(vector, target), number=100)
        times.append(time_taken)

    return np.mean(times)

vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linear_search_times = []
binary_search_times = []

for size in vector_sizes:
    linear_time = measure_performance(linear_search, size)
    binary_time = measure_performance(binary_search, size)
    linear_search_times.append(linear_time)
    binary_search_times.append(binary_time)

# Plotting
plt.plot(vector_sizes, linear_search_times, label='Linear Search', marker='o')
plt.plot(vector_sizes, binary_search_times, label='Binary Search', marker='o')

# Interpolate with quadratic functions
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

params_linear, _ = curve_fit(lambda x, a, b: a * x + b, vector_sizes, linear_search_times)
params_binary, _ = curve_fit(quadratic_func, vector_sizes, binary_search_times)

plt.plot(vector_sizes, params_linear[0] * np.array(vector_sizes) + params_linear[1], linestyle='--', label='Linear Fit (Linear Search)')
plt.plot(vector_sizes, quadratic_func(np.array(vector_sizes), *params_binary), linestyle='--', label='Quadratic Fit (Binary Search)')

plt.xlabel('Vector Size')
plt.ylabel('Average Time (s)')
plt.title('Performance of Linear and Binary Search')
plt.legend()
plt.show()
