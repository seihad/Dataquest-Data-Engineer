'''
1. Sorting in Python
'''
# values = [6, 8, 7, 4, 3, 5, 2, 1, 9]
# sorted_values = sorted(values)
# sorted_values_reverse = sorted(values,reverse=True)
# print(sorted_values)
# print(sorted_values_reverse)

'''
2. Swapping
'''

# value_list = [1, 4, 5, 2, 3]
# i = 1
# j = 3

# def swap(values, i, j):
#     temp = 0
#     temp = values[i]
#     values[i] = values[j]
#     values[j] = temp

# swap(value_list, i,j)
# print(value_list)

'''
3. Selecting the Minimum
'''
# def swap(values, i, j):
#     temp = values[i]
#     values[i] = values[j]
#     values[j] = temp

# def select_minimum_index_in_range(values, range_start):
#     minimum = None
#     minimum_index = None
#     N = len(values)
#     for i in range(range_start, N):
#         if minimum == None or values[i] < minimum:
#             minimum = values[i]
#             minimum_index = i
#     return minimum_index

# values = [5, 4, 6, 1, 3, 2]

# # Add your code below
# index = select_minimum_index_in_range(values, 0)
# print(index)
# swap(values, 0, index)
# print(values)

'''
4. Selection Sort
'''
# def swap(values, i, j):
#     temp = values[i]
#     values[i] = values[j]
#     values[j] = temp

# def select_minimum_index_in_range(values, range_start):
#     minimum = None
#     minimum_index = None
#     N = len(values)
#     for i in range(range_start, N):
#         if minimum == None or values[i] < minimum:
#             minimum = values[i]
#             minimum_index = i
#     return minimum_index

# values = [5, 4, 6, 1, 3, 2]

# # Add your code below
# def selection_sort(values):
#     for range_start in range(len(values)):
#         index = select_minimum_index_in_range(values, range_start)
#         swap(values, range_start, index)
# selection_sort(values)
# print(values)

'''
5. Complexity of Selection Sort
'''
# import matplotlib.pyplot as plt

# def plot_values(values):
#     plt.plot(values, label='1+2+...+N', color='y')
#     plt.ylabel('1+2+...+N')
#     plt.xlabel('N')
#     plt.legend()
#     plt.show()
    
# # Write your code below
# sum_first_N = 0
# values = []
# for N in range(1, 1001):
#     sum_first_N += N
#     values.append(sum_first_N)
# plot_values(values)

'''
6. Sum of the Frist N Naturals
'''
# sum_first_N = 0
# values = []
# for N in range(1, 1001):
#     sum_first_N += N
#     values.append(sum_first_N)

# values_formula = []
# for N in range(1,1001):
#     value = (N * N / 2) + (N / 2)
#     values_formula.append(value)

# print(values == values_formula)

'''
7. Find Equal Pairs of Indexes
'''
# sum_first_N = 0
# values = []
# for N in range(1, 1001):
#     sum_first_N += N
#     values.append(sum_first_N)

# def find_pair(values):
#     N = len(values)
#     count = 0
#     for i in range(N):
#         for j in range(i + 1, N):
#             count += 1
#             if values[i] == values[j]:
#                 return (i, j)
#     print(count)
#     return None

# # Write your code below
# def num_if_executions(N):
#     # We need to substract N elements
#     # These corresponds to pairs with i = j
#     return N*N/2 + N/2 - N

# count_1000 = num_if_executions(1000)
# print(count_1000)

'''
8.Comparing Insertion Sort with Python Sort
'''
import matplotlib.pyplot as plt

def plot_times(times_python, times_selection):
    plt.plot(times_python, label='time sorted()')
    plt.plot(times_selection, label='time selection_sort()')
    plt.ylabel('runtime')
    plt.xlabel('N')
    plt.legend()
    plt.show()

def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def select_minimum_index_in_range(values, range_start):
    minimum = None
    minimum_index = None
    N = len(values)
    for i in range(range_start, N):
        if minimum == None or values[i] < minimum:
            minimum = values[i]
            minimum_index = i
    return minimum_index
    
def selection_sort(values):
    N = len(values)
    for range_start in range(N):
        index = select_minimum_index_in_range(values, range_start)
        swap(values, range_start, index)

# Write your code below
import time, random
times_python = []
times_selection = []
for N in range (1,501):
    values = [random.randint(1,10000) for _ in range(N)]
    start_py = time.time()
    sorted(values)
    end_py = time.time()
    runtime_py = end_py - start_py
    times_python.append(runtime_py)
    start_sel = time.time()
    selection_sort(values)
    end_sel = time.time()
    runtime_sel = end_sel - start_sel
    times_selection.append(runtime_sel)
plot_times(times_python, times_selection)