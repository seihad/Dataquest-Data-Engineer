#### 1 Introduction to Time Complexity
#returning the maximum value in values
# test_values = [4, 3, 5, 6, 2, 1]

# def maximum(values):
#     answer = None
#     for value in values:
#         if answer == None or answer < value:
#             answer = value
#     return answer

# max_value = maximum(test_values)
# print(max_value)


#### 2 Measuring the Execution Time
# test_values = [4, 3, 5, 6, 2, 1]
# def maximum(values):
#     answer = None
#     for value in values:
#         if answer == None or answer < value:
#             answer = value
#     return answer

# import time
# start = time.time()

# max_value = maximum(test_values)

# end = time.time()
# runtime = end - start
# print(runtime)

#### 3 Generating Random Inputs
# import time
# import random

# def maximum(values):
#     answer = None
#     for value in values:
#         if answer == None or answer < value:
#             answer = value
#     return answer

# def gen_input(length):
#     return [random.randint(-1000, 1000) for _ in range(length)]

# # add your code below
# times = []
# for length in range(1,501):
#     values = gen_input(length)
#     start = time.time()
#     maximum(values)
#     end = time.time()
#     times.append(end - start)
# print(time)

#### 5 Modeling Execution Times
# import time
# import random
# import matplotlib.pyplot as plt

# def plot_times(times):
#     plt.plot(times)
#     plt.ylabel('runtime')
#     plt.xlabel('size')
#     plt.show()

# def sum_values(values):
#     total = 0            
#     for value in values: 
#         total += value   
#     return total  

# def gen_input(length):
#     return [random.randint(-1000, 1000) for _ in range(length)]

# # add your code below
# times = []
# for length in range(1,501):
#     values = gen_input(length)
#     start = time.time()
#     sum_values(values)
#     end = time.time()
#     run_time = end - start
#     times.append(run_time)
# plot_times(times)

#### 6 Worst-Case Analysis
# def count_zeros(values):
#     count = 0            # c1, 1, c1
#     for value in values: # c2, N, c2 * N
#         if value == 0:   # c3, N, c3 * N
#             count += 1   # c4, N, c4 * N
#     return count         # c5, 1, c5 * N

# model1 = '(c1 + c2) * N + (c3 + c4 + c5)'
# model2 = '(c2 + c3) * N + (c1 + c4 + c5)'
# model3 = '(c2 + c3 + c4) * N + (c1 + c5)'

# # c1 + (c2 * N) + (c3 * N) + (c4 * N) + c5 
# # c1 + c5 + (N * (c2 + c3 + c4)) --> model 3
# # a + (N * b)
# correct = model3

#### 7 Quadratic Complexity
# def sum_pairs(values):
#     pair_sums = 0              # c1, 1, c1            
#     for x in values:           # c2, N, c2 * N     
#         for y in values:       # c3, N * N, c3 * N * N     
#             pair_sums += x + y # c4, N * N, c4 * N * N
#     return pair_sums           # c5, 1, c5

# model1 = '(c3 + c4) * N^2 + c2 * N + (c1 + c5)'
# model2 = 'c4 * N^2 + (c2 + c3) * N + (c1 + c5)'
# model3 = '(c2 + c3 + c4) * N^2 + (c1 + c5)'

# # c1 + (c2 * N) + (c3 * N * N) + (c4 * N * N) + c5
# # c1 + c5 + N * N * (c3 + c4) + c2 * N
# correct = model1

#### 8 Simplifying Further
# time1 = 'N^4 + N^2 + 1'
# time2 = '7 * N^3 + 0.5 * N^2 + 100'
# time3 = 'N^2 + 10000 * N + 999'

# O1 = "O(N^4)"
# O2 = "O(N^3)"
# O3 = "O(N^2)"

#### 9 A Common Misconception
# def count_triples(values):
#     count = 0                                               # 1
#     N = len(values)                                         # 1
#     for i in range(N):                                      # N
#         for j in range(N):                                  # N^2
#             for k in range(N):                              # N^3
#                 if values[i] + values[j] + values[k] == 0:  # N^3
#                     count += 1                              # N^3
#     return count                                            # 1

# # N + (N ^ 2) + (3 * N ^ 3)
# # 3N ^ 3
# # O(N^3)


# coefficients = [3,1,1,3] # 3N^3 + N^2 + N + 3
# order = "O(N^3)"


