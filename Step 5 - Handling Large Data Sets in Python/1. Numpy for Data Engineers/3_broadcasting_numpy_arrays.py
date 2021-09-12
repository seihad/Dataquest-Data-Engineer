'''
1.Introduction
'''
# import numpy as np
# x = np.array([
#  [7., 9., 2., 2.],
#  [3., 2., 6., 4.],
#  [5., 6., 5., 7.]
# ])
# ones = np.ones((3,4))
# print(ones)
# x = x - ones
# print(x)

'''
2.Broadcasting With a Single Value
'''
# import numpy as np
# x = np.array([3, 2, 4, 5])
# r = 1 / x
# print(r)

'''
3.Broadcasting Mental Model
'''
# import numpy as np
# x = np.array([
#     [4, 2, 1, 5],
#     [6, 7, 3, 8]
# ])
# y = np.array([
#     [1],
#     [2]
# ])
# z = x + y
# print(z)

'''
4.Broadcasting Horizontally
'''
# import numpy as np
# x = np.array([
#     [4, 2, 1, 5],
#     [6, 7, 3, 8]
# ])
# y = np.array([1,2,3,4])
# z = x + y
# print(z)

'''
5.Broadcasting Vertically
'''
# import numpy as np
# x = np.array([
#     [1], 
#     [2],
#     [3]
# ])
# y = np.array([1,2,3])
# z = x + y
# print(z)

'''
6.Broadcasting on Both
'''
# import numpy as np
# dice1 = np.array([1,2,3,4,5,6])
# dice2 = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6]
# ])
# dice_sums = dice1 + dice2
# print(dice_sums)

'''
7.Broadcasting Rules
'''
# import numpy as np
# x = np.array([1, 2, 3, 4])
# y = np.array([
#     [1], 
#     [2], 
#     [3], 
#     [4]
# ])

# shape_x = x.shape
# print(shape_x)
# shape_y = y.shape
# print(shape_y)

# shape_x_step1 = (1,4)
# print(x)
# shape_y_step1 = (4,1)
# print(y)

# shape_x_step2 = (4,4)
# print(x)
# shape_y_step2 = (4,4)
# print(y)

# print(x+y)

# error = False

'''
8.Reshaping
'''
# import numpy as np
# dice1 = np.array([1,2,3,4,5,6])
# dice2 = dice1.reshape(6,1)
# dice_sums = dice1 + dice2
# print(dice_sums)

'''
9.Compatible Shapes
'''
import numpy as np
cell_numbers = np.array([num for num in range(1,37)])
numbering_by_row = cell_numbers.reshape((6,6))
print(numbering_by_row)
numbering_by_col = cell_numbers.reshape((6,6), order='F')
print(numbering_by_col)