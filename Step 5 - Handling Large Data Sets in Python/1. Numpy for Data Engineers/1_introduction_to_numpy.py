'''
1. Introduction
'''
# import numpy as np

'''
2.Introduction to ndarrays
'''
# import numpy as np
# x = np.array([10, 20, 30])
# length = len(x)
# print(length)

'''
3.Accessing Values in an ndarray
'''
# import numpy as np
# x = np.array([10, 20, 30])
# x0 = x[0]
# x2 = x[2]
# x[1] = 42
# print(x0, x2)
# print(x)

'''
4.Slicing ndarrays
'''
# import numpy as np
# x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])
# first_half = x[:5]
# last_8 = x[2:]
# middle = x[1:-1]
# print(first_half)
# print(last_8)
# print(middle)

'''
5.The Slicing Increment
'''
# import numpy as np
# x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])
# even = x[::2]
# odd = x[1::2]
# mul_3 = x[::3]
# every_2 = x[3:9:2]
# print(even)
# print(odd)
# print(mul_3)
# print(every_2)

'''
6.Copying an ndarray
'''
# import numpy as np
# x = np.array([1, 0, 0, 0, 1])
# y = x[1:-1]
# z  = y.copy()
# z[0] = 9
# print(x)
# print(y)
# print(z)
# y[1] = 7
# print(x)
# print(y)
# print(z)

'''
7.Negative Indexes and Steps
'''
# import numpy as np
# x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])
# second_to_last = x[-2]
# reversed_x = x[::-1]
# first_5_reversed = x[4::-1]
# last_5_reversed = x[-1:-6:-1]
# print(second_to_last)
# print(reversed_x)
# print(first_5_reversed)
# print(last_5_reversed)

'''
8.Two Dimensional Arrays
'''
# import numpy as np
# my_2d_array = np.array([
#     [1,4,7],
#     [2,5,8],
#     [3,6,9]
# ])
# my_2d_array[1,1] = 42
# print(my_2d_array)

'''
9.Slicing Two Dimensional Arrays
'''
# import numpy as np
# array2d = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ])
# x = array2d[:, 3:]
# y = array2d[::2, :]
# z = array2d[::2, ::2]
# print(x)
# print(y)
# print(z)

'''
10.Setting The Slice Value
'''
# import numpy as np
# array2d = np.array([
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ])
# array2d[:,:2] = 1
# print(array2d)

# array2d[2:, :] = 2
# print(array2d)

# array2d[:3, 1:4] = 3
# print(array2d)


'''
11.Selecting Rows and Columns
'''
import numpy as np
people_data = np.array([
    [27, 67, 1.65],
    [35, 81, 1.84],
    [29, 55, 1.60],
    [41, 73, 1.79]
])
anna_row = people_data[2, :]
print(anna_row)
bob_age_height = people_data[-1, 0::2]
print(bob_age_height)
ages_col = people_data[:, 0]
print(ages_col)
weight_dexter_bob = people_data[1::2, -2]
print(weight_dexter_bob)