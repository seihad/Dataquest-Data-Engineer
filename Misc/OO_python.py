#### 1
# l = [1, 2, 3]
# s = "string"
# d = {"a": 1, "b": 2}
# my_set = {2, 3, 5}

# print(d)
# print(type(l))
# print(type(s))
# print(type(d))
# print(type(my_set))

#### 2
# tri_num_sequence = [1, 3, 6, 10, 15, 10, 6, 3, 1]
# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# trinum_5 = set(tri_num_sequence)
# odd_20 = set(odd_numbers)
# odd_trinum = odd_20.intersection(trinum_5)
# print(odd_trinum)

#### 4
# class NewList():
#     pass

#### 5
# class NewList:
#     pass

# newlist_1 = NewList()
# print(type(newlist_1))

#### 6
# class NewList:
#     def first_method():
#         return "This is my first method"

# newlist = NewList()

#### 7
# class NewList:
#     def first_method(self):
#         return "This is my first method"

# newlist = NewList()
# result = newlist.first_method()
# print(result)

#### 8
# class NewList:
#     def return_list(self, input_list):
#         return input_list

# newlist = NewList()
# result = newlist.return_list([1,2,3])
# print(result)

#### 9 
# class NewList:
#     def __init__(self, initial_state):
#         self.data = initial_state

# my_list = NewList([1,2,3,4,5])
# print(my_list.data)


#### 10
# class NewList:
#     def __init__(self, initial_state):
#         self.data = initial_state
#     def append(self,argument):
#         self.data += [argument]


# my_list = NewList([1,2,3,4,5])
# my_list.append(6)
# print(my_list.data)

#### 11
class NewList:
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]
        self.calc_length()

    def calc_length(self):
        length = 0
        for item in self.data:
            length += 1
        self.length = length

fibonacci = NewList([1,1,2,3,5])
print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)