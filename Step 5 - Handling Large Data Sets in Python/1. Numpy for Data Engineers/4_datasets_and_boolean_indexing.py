'''
1. Introduction
'''

# import numpy as np
# x = np.array([
#     [44, 70, 49,  2, 19],
#     [62, 68, 64, 18, 12],
#     [91, 90, 63, 98, 69],
#     [22,  9, 98, 16, 58],
#     [47, 92, 39,  8, 19],
#     [ 1, 41,  3, 15, 71],
#     [92, 18, 37, 42,  5]
# ])

# first_four = x[:4]
# print(first_four)
# last_column = x[:,-1]
# print(last_column)

'''
2.Loading CSV Data
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# first_five = sars[:5,]
# print(first_five)


'''
3.Removing Invalid Data
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# print(sars[:5])


'''
4.NumPy Limitations
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# total = sars[:,2]
# max_dead = total.max()
# print(max_dead)


'''
5.Comparing Column Values
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# female = sars[:, 0]
# male = sars[:, 1]
# more_female_deaths = female > male
# print(more_female_deaths)
# equal_deaths = female == male
# print(equal_deaths)
# num_more_female = more_female_deaths.sum()
# print(num_more_female)
# num_equal = equal_deaths.sum()
# print(num_equal)
# num_more_male = len(sars) - num_more_female - num_equal
# print(num_more_male)
# print(len(sars))


'''
6.Comparing With a Single Value
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# any_less_1 = (sars[:,4] < 1).any()
# print(any_less_1)
# all_less_50 = (sars[:,4] <= 50).all()
# print(all_less_50)

'''
7.Logical Connectors
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# deaths = sars[:,3]
# fatality_ratio = sars[:,4]

# death_gt_100_ratio_lt_10 = (deaths >= 100) & (fatality_ratio<=10)
# count = death_gt_100_ratio_lt_10.sum()
# print(count)

'''
8.Boolean Masks
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# deaths = sars[:,3]
# fatality_ratio = sars[:,4]

# mask = fatality_ratio>=10
# print(mask)
# num_deaths = deaths[mask]
# print(num_deaths)

'''
9.Boolean Masks in Higher Dimensions
'''
# import numpy as np
# sars = np.genfromtxt('sars.csv', delimiter=',')
# np.set_printoptions(suppress=True)
# sars = sars[1:]
# sars = sars[:,1:]
# mask_zeros = sars == 0
# zeros = sars[mask_zeros]
# num_zeros = len(zeros)
# print(num_zeros)

'''
10.1D Mask on 2D Array
'''
import numpy as np
sars = np.genfromtxt('sars.csv', delimiter=',')
np.set_printoptions(suppress=True)
sars = sars[1:]
sars = sars[:,1:]

non_zero_deaths = sars[:,3] > 0
sars_subtable = sars[non_zero_deaths,-3:]
print(sars_subtable)