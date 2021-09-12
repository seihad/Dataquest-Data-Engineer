'''1.Introduction'''
# import numpy as np
# x = np.array([1, 2, 3, 4])
# x[0] = 5.5
# print(x)


'''2.Fixed NumPy Datatypes'''
# import numpy as np
# values = [1, 2, 3, 4]
# x = np.array(values, dtype=np.float64)
# x[0] = 5.5
# print(x)

'''3.Finding the Datatype'''
# import numpy as np

# boolean_list = [True, False, True, False]
# integer_list = [6, -5, -9, 10]
# float_list   = [0.5, 10.74, 65.5, 0.2]

# boolean_array = np.array(boolean_list)
# print(boolean_array.dtype)

# integer_array = np.array(integer_list)
# print(integer_array.dtype)

# float_array = np.array(float_list)
# print(float_array.dtype)

'''4.Ndarray From Mixed Lists'''
# import numpy as np
# values = [3.14, 6.42, 5.0, 0.5]
# x = np.array(values,dtype=np.int64)
# print(x.dtype)


'''5.Fixed-Length Bit Representations'''
# import numpy as np
# value_list = [-127, -57, -6, 0, 9, 42, 125]
# value_array = np.array(value_list,dtype=np.int8)
# print(value_array.dtype)


'''6.Memory Consumption'''
# import numpy as np
# x = np.array([-127, -57, -6, 0, 9, 42, 125], dtype=np.int8)
# print(x-2)
# print(x+3)


'''7.Arithmetic Overflow'''



'''8.Float Limitations'''



'''9.Calculating Memory Requirements'''
# num_values = 8 * (10 ** 9)
# num_bits = 64 * num_values
# gb = num_bits / (8 * (10 ** 9))
# print(gb)

