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
        start_time = timeit.default_timer()
        search_function(vector, target)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)

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
def log_func(x, a, b):
    return a * np.log(x) + b

# Fit binary search data with logarithmic function
params_binary_log, _ = curve_fit(log_func, vector_sizes, binary_search_times)

# Plot logarithmic fit for binary search
plt.plot(vector_sizes, log_func(np.array(vector_sizes), *params_binary_log), linestyle='--', label='Logarithmic Fit (Binary Search)')



plt.xlabel('Vector Size')
plt.ylabel('Average Time (s)')
plt.title('Performance of Linear and Binary Search')
plt.legend()
plt.show()


# Answer to question 4:
#The linear fit for linear search should closely match the data points, 
#indicating that the time taken increases linearly with the vector size.
# Logarithmic fit allows to appropiately represent binary search since it has a logarithmic time complexity (O(log n)) 
# The results align closesly with the expectations we have of their repsective time complexities 