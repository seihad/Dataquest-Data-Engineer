#### 1 Constant Time Complexity
# def average(values):
#     average = 0                 # 1
#     for value in values:        # N
#         average += value        # N
#     return average / len(values)# 1

# # O(N) = 2 * N + 2
# coefficients = [2, 2]
# order = "O(N)"

#### 2 Constant Time Complexity in Python

# def function1(N):
#     for i in range(N):
#         print(i)

# def function2():
#     for i in range(100000):
#         print(i)

# def function3(N):
#     for i in range(100000):
#         print(i)

# constant1 = False
# constant2 = True
# constant3 = True
    
#### 3 Complexity of Function Calls
# def sum_values(values):
#     total = 0            # 1
#     for value in values: # N
#         total += value   # N
#     return total         # 1

# def num_values(values):
#     total = 0            # 1
#     for _ in values:     # N
#         total += 1       # N
#     return total         # 1

# def average(values):
#     value_sum = sum_values(values)  # N
#     num_values = num_values(values) # N
#     return value_sum / num_values   # 1

#### 4 Hidden Function Calls
# N = 10
# M = 20

# list1 = [_ for i in range(0)]
# list2 = [i for i in range(3)]
# list3 = [i * i for i in range(M)]
# list4 = [[i + j for j in range(M)] for i in range(N)]
# list5 = [min(list4[i]) for i in range(N)]
# list6 = [i for i in range(1000)]

# complexity1 = 'O(1)'
# complexity2 = 'O(N)'
# complexity3 = 'O(M)'
# complexity4 = 'O(N + M)'
# complexity5 = 'O(N * M)'

# # Example answer for list1
# answer1 = complexity1
# answer2 = complexity1
# answer3 = complexity3
# answer4 = complexity5
# answer5 = complexity5
# answer6 = complexity1

#### 6 Amortized Analysis of Append
# import matplotlib.pyplot as plt

# def plot_costs(times):
#     plt.plot(times, label='append cost')
#     plt.ylabel('cost')
#     plt.xlabel('N')
#     plt.show()
    
# def append_cost(array_length, list_length):
#     if array_length == list_length:
#         return array_length
#     return 1

# def append_N_list_cost(N):
#     array_length = 1 # initially the array will have length 1
#     list_length = 0 # initially the list has 0 elements
#     total_cost = 0 # this variable will keep track of the total cost
#     for i in range(N):
#         total_cost = append_cost(array_length, list_length)
#         total_cost += cost
#         # update the array and list lengths
#         if array_length == list_length:
#             array_length *= 2
#         list_length += 1
#     return total_cost

# # add you code below
# costs = []
# for N in range(5000):
#     cost = append_N_list_cost(N)
#     costs.append(cost)

# plot_costs(costs)

#### 7 List Complexities
# def add_with_append(N):
#     values = []
#     for i in range(N):
#         values.append(i)
#     return values

# def add_with_insert(N):
#     values = []
#     for i in range(N):
#         values.insert(0, i)
#     return values

# # write code below
# import time
# start = time.time()
# add_with_append(5000)
# end = time.time()
# time_append = end - start
# print(time_append)

# start = time.time()
# add_with_insert(5000)
# end = time.time()
# time_append = end - start
# print(time_append)

#### 8 Arithmetic Operations
# import matplotlib.pyplot as plt

# pairs = [(3, 5),
#  (73, 98),
#  (175, 967),
#  (4196, 4917),
#  (39513, 31893),
#  (125832, 846781),
#  (8578541, 5495644),
#  (66745978, 48629483),
#  (192985863, 321846841),
#  (5932992992, 3944445511),
#  (34549655924, 84546724993),
#  (489827388993, 953415635411),
#  (3222624238443, 9986646235274),
#  (83112312223688, 87972197936816),
#  (275642256581448, 217328448937274),
#  (8496452495386688, 4571261474319539),
#  (92557162321176783, 72987693654871596)]

# def plot_times(times):
#     plt.plot(times)
#     plt.ylabel('multiplication runtime')
#     plt.xlabel('number of digits')
#     plt.yscale('log')
#     plt.yticks([])
#     plt.show()

# print(pairs[:5])
# # write code below
# import time
# times = []
# for x,y in pairs:
#     start = time.time()
#     x * y
#     end = time.time()
#     run_time = end - start
#     times.append(run_time)

# plot_times(times)

#### 9 String Concatenation
# import time
 
# def concat_with_add(word_list):
#     concat = ''
#     for word in word_list:
#         concat += word
#     return concat

# def concat_with_join(word_list):
#     return ''.join(word_list)

# random_strings = ['tdrxvpaiut\n',
#  'ltzxjepsgl\n',
#  'zaxiqsdzpi\n',
#  'naprvwggts\n',
#  'rhorhifeqf\n',
#  'fdfhsysihx\n',
#  'sywwancqku\n',
#  'jlmjnvsykr\n',
#  'tlwwqxyxip\n',
#  'xluvdygihg\n',
#  'mdkmcphljb\n',
#  'dscyhlkbal\n',
#  'rhyjdyfgsw\n',
#  'rojlnadaac\n',
#  'uqikveceef\n',
#  'fllsvnebbw\n',
#  'aywvyxgpsc\n',
#  'vrjhlzhgby\n',
#  'qqvcnkqhxd\n',
#  'jeytnamqhu\n',
# ]

# print(random_strings[:5])

# # write code below
# start = time.time()
# concat_with_add(random_strings)
# end = time.time()
# time_add = end - start

# start = time.time()
# concat_with_join(random_strings)
# end = time.time()
# time_join = end - start
    
# print(time_add)
# print(time_join)

#### 10 Hidden Python Optimizations #########
import time

with open('random_words.txt', mode='r') as f:
   word_list = f.readlines() 

def concat_with_add(word_list):
    concat = ''
    for word in word_list:
        concat += word
        temp = concat
    return concat

def concat_with_join(word_list):
    return ''.join(word_list)

start = time.time()
concat_with_add(random_strings)
end = time.time()
time_add = end - start

start = time.time()
concat_with_join(random_strings)
end = time.time()
time_join = end - start
    
print(time_add)
print(time_join)