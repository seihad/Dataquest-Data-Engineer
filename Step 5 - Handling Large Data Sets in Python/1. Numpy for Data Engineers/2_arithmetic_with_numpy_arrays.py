'''
1.Introduction
'''
# import numpy as np
# table = np.array([
#     [ 1,  2,  3,  4,  5],
#     [ 6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ])
# col = table[:, 1]
# print(col)

# row = table[2]
# print(row)

# center = table[1:3, 1:4]
# print(center)

'''
2.Adding ndarrays
'''
# def add_list_values(list1, list2):
#     result = []
#     for idx in range(len(list1)):
#         result.append(list1[idx] + list2[idx])
#     return result
# list1 = [3, 4, 3, 2]
# list2 = [1, 2, 4, 3]
# result = add_list_values(list1, list2)
# print(result)

'''
3.Comparing Ndarrays to Lists
'''
# import numpy as np
# import time
# import random
# random.seed(0)

# # Generate test lists
# list1 = [random.randint(0, 1000) for _ in range(100000)]
# list2 = [random.randint(0, 1000) for _ in range(100000)]

# # Measure the execution time of adding lists
# def add_list_values(list1, list2):
#     result = []
#     for idx in range(len(list1)):
#         result.append(list1[idx] + list2[idx])
#     return result
# start = time.time()
# add_list_values(list1, list2)
# end = time.time()
# time_list = end - start

# # Write your code below
# x1 = np.array(list1)
# x2 = np.array(list2)
# start = time.time()
# x3 = x1 + x2
# end = time.time()
# time_array =  end - start

# ratio = time_list / time_array

# print(ratio)


'''
5.Arithmetic Operations
'''
# import numpy as np
# people_data = np.array([
#     [27, 67, 1.65],
#     [35, 81, 1.84],
#     [29, 55, 1.60],
#     [41, 73, 1.79]
# ])

# w = people_data[:,1]
# print(w)

# h = people_data[:,2]
# print(h)

# bmi = w / (h ** 2)
# print(bmi)

'''
6.Arithmetic in Higher Dimensions
'''
# import numpy as np
# scores = np.array([
#     [46, 74, 52, 81],
#     [75, 45, 67, 53],
#     [67, 80, 73, 63],
#     [59, 94, 43, 78]
# ])

# scores_day1 = scores[:,:2]
# print(scores_day1)

# scores_day2 = scores[:,-2:]
# print(scores_day2)

# shape1 = scores_day1.shape
# print(shape1)

# shape2 = scores_day2.shape
# print(shape2)

# total_scores = scores_day1 + scores_day2
# print(total_scores)

'''
7.Minimum and Maximum
'''
# import numpy as np
# total_scores = np.array([
#  [ 98, 155],
#  [142,  98],
#  [140, 143],
#  [102, 172]
# ])

# scores_game1 = total_scores[:,0] 
# scores_game2 = total_scores[:,1] 

# min_game1 = scores_game1.min()
# max_game1 = scores_game1.max()

# min_game2 = scores_game2.min()
# max_game2 = scores_game2.max()

'''
8.The Axis Parameter
'''
# import numpy as np
# total_scores = np.array([
#  [ 98, 155],
#  [142,  98],
#  [140, 143],
#  [102, 172]
# ])

# max_game_scores = total_scores.max(axis=0)
# print(max_game_scores)

# min_game_scores = total_scores.min(axis=0)
# print(min_game_scores)


# max_people_scores = total_scores.max(axis=1)
# print(max_people_scores)

# min_people_scores = total_scores.min(axis=1)
# print(min_people_scores)

'''
9.Sum
'''
import numpy as np
total_scores = np.array([
 [ 98, 155],
 [142,  98],
 [140, 143],
 [102, 172]
])
total_people_score = total_scores.sum(axis=1)
print(total_people_score)
max_score = total_people_score.max()
print(max_score)