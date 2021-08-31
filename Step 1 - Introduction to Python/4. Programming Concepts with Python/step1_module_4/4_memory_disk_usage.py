#### 1
# import numpy as np

# x = np.int8(100)
# y = np.int8(25)
# z = x + y
# print(z)

#### 2
# x = (1 * -(2 ** 1)) + (0 * (2 ** 0))
# y = (1 * -(2 ** 3)) + (0 * (2 ** 2)) + (1 * (2 ** 1)) + (0 * (2 ** 0))
# z = (0 * -(2 ** 3)) + (1 * (2 ** 2)) + (1 * (2 ** 1)) + (0 * (2 ** 0))
# print(x, y, z)

#### 3
# import numpy as np
# print(np.binary_repr(-2147483648, width=32))
# print(np.binary_repr(2147483647, width=32))

#### 4
# import sys
# x = 2147483647 # maximum value for 32-bit integers
# num_bytes = sys.getsizeof(x)
# num_mb = 1000000000 * num_bytes / 1000000
# print(num_bytes)
# print(num_mb)

#### 5
# def minimum_required_bits(list_of_integers):
#     min_req_bits = 0 
#     for value in list_of_integers:
#         nb_bits = int.bit_length(value)
#         min_req_bits = max(min_req_bits, nb_bits)
#     return min_req_bits

# with open("identifiers.txt", encoding="UTF-8") as file:
#     file_list = list(file)
#     values = [int(value) for value in file_list]
#     print(minimum_required_bits(values))


#### 6
# import sys
# s = "你"
# size_s = sys.getsizeof(s)
# size_ss = sys.getsizeof(s + s)
# print(size_s, size_ss)

#### 7
# import sys
# message = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"

# message_latin_bytes = message.encode(encoding="Latin-1",errors="ignore")
# cleaned_message = message_latin_bytes.decode(encoding="Latin-1")
# message_size = sys.getsizeof(message)
# cleaned_message_size = sys.getsizeof(cleaned_message)
# print(message_size)
# print(cleaned_message_size)

#### 8 Disk Consumption of Textual Data
# import os
# messages = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"

# with open("utf8.txt",encoding="UTF-8",mode="w") as file:
#     file.write(messages)

# size_utf8 = os.path.getsize("utf8.txt")
# print(size_utf8)

# with open("utf32.txt",encoding="UTF-32", mode="w") as file:
#     file.write(messages)

# size_utf32 = os.path.getsize("utf32.txt")
# print(size_utf32)

#### 9 Estimating the Disk Requirementss
num_days_in_a_year = 365
num_years = 20
bytes_per_char = 32 / 8
num_transactions = 1000000
username_size = 20
product_name_size = 50

total_days = num_years * num_days_in_a_year
bytes_per_transaction = bytes_per_char * (2 * username_size + product_name_size)
bytes_per_day = bytes_per_transaction * num_transactions
total_bytes = total_days * bytes_per_day
bytes_in_gb = 10 ** 9

num_gb = total_bytes / bytes_in_gb
print(num_gb)








