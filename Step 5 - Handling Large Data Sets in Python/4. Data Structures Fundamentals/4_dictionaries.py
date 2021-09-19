'''1.Introduction'''
# class Entry:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

# my_entry = Entry(12345, "my value")

'''2.Internal Structure'''
# class Dictionary:
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         self.buckets = [None for _ in range(num_buckets)]
#         self.lenth = 0

# my_dict = Dictionary(5)


'''3.Separate Chaining'''
# Add import here
# import linked_list

# class Dictionary:
    
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         # Modify the line below
#         self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
#         self.length = 0

# my_dict = Dictionary(5)


'''4.Hashing'''
# import linked_list

# class Dictionary:
    
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         # Modify the line below
#         self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
#         self.length = 0

#     def _get_index(self, key):
#         hashcode = hash(key)
#         return hashcode % self.num_buckets

# my_dict = Dictionary(5)

# index = my_dict._get_index("data engineering")
# print(index)


''''5.Adding an Entry'''
# import linked_list

# class Entry:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

# class Dictionary:
    
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         # Modify the line below
#         self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
#         self.length = 0

#     def _get_index(self, key):
#         hashcode = hash(key)
#         return hashcode % self.num_buckets

#     def put(self, key, value):
#         index = self._get_index(key)
#         found_key = False
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 entry.value = value
#                 found_key = True
#         if found_key == False:
#             self.buckets[index].append(Entry(key, value))
#             self.length += 1

# my_dict = Dictionary(5)
# my_dict.put("my key", 1)



'''6.Locating an Entry'''
# import linked_list

# class Entry:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

# class Dictionary:
    
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         # Modify the line below
#         self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
#         self.length = 0

#     def _get_index(self, key):
#         hashcode = hash(key)
#         return hashcode % self.num_buckets

#     def put(self, key, value):
#         index = self._get_index(key)
#         found_key = False
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 entry.value = value
#                 found_key = True
#         if found_key == False:
#             self.buckets[index].append(Entry(key, value))
#             self.length += 1

#     def get_value(self, key):
#         index = self._get_index(key)
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 return entry.value
#         raise KeyError(key)

# my_dict = Dictionary(5)
# my_dict.put("my key", 1)
# print(my_dict.get_value("my key"))
# my_dict.put("my key", 2)
# print(my_dict.get_value("my key"))

'''7.Deleting an Entry'''
# import linked_list

# class Entry:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

# class Dictionary:
    
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         # Modify the line below
#         self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
#         self.length = 0

#     def _get_index(self, key):
#         hashcode = hash(key)
#         return hashcode % self.num_buckets

#     def put(self, key, value):
#         index = self._get_index(key)
#         found_key = False
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 entry.value = value
#                 found_key = True
#         if found_key == False:
#             self.buckets[index].append(Entry(key, value))
#             self.length += 1

#     def get_value(self, key):
#         index = self._get_index(key)
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 return entry.value
#         raise KeyError(key)

#     def delete(self, key):
#         index = self._get_index(key)
#         new_bucket = linked_list.LinkedList()
#         for entry in self.buckets[index]:
#             if entry.key != key:
#                 new_bucket.append(entry)
#             if len(new_bucket) < len(self.buckets[index]):
#                 self.length -= 1
#         self.buckets[index] = new_bucket


# my_dict = Dictionary(5)
# my_dict.put("my key", 1)
# my_dict.delete("my key")
# print(my_dict.length)


'''8.Polishing the Dictionary'''
# import linked_list

# class Entry:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

# class Dictionary:
    
#     def __init__(self, num_buckets):
#         self.num_buckets = num_buckets
#         # Modify the line below
#         self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
#         self.length = 0

#     def _get_index(self, key):
#         hashcode = hash(key)
#         return hashcode % self.num_buckets

#     def put(self, key, value):
#         index = self._get_index(key)
#         found_key = False
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 entry.value = value
#                 found_key = True
#         if found_key == False:
#             self.buckets[index].append(Entry(key, value))
#             self.length += 1

#     def get_value(self, key):
#         index = self._get_index(key)
#         for entry in self.buckets[index]:
#             if entry.key == key:
#                 return entry.value
#         raise KeyError(key)

#     def delete(self, key):
#         index = self._get_index(key)
#         new_bucket = linked_list.LinkedList()
#         for entry in self.buckets[index]:
#             if entry.key != key:
#                 new_bucket.append(entry)
#             if len(new_bucket) < len(self.buckets[index]):
#                 self.length -= 1
#         self.buckets[index] = new_bucket
    
#     def __getitem__(self, key):
#         return self.get_value(key)

#     def __setitem__(self, key, value):
#         self.put(key, value)
    
#     def __len__(self):
#         return self.length
        
# my_dict = Dictionary(5)
# my_dict["my key"] = 2
# print(my_dict["my key"])
# print(len(my_dict))

'''9.Dictionary Time Complexity'''
# import matplotlib.pyplot as plt
# import time


# def plot_times(times):
#     plt.plot(times)
#     plt.show()

# import time
# import random
# random.seed(0)

# times = []
# number_of_entries = 1000
# keys = range(number_of_entries)

# d = dict()

# for key in keys:
#     start = time.time()
#     d[key] = key
#     end = time.time()
#     times.append(end - start)
    
# plot_times(times)


''''10.Selecting the Table Size'''
import linked_list

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Dictionary:
    
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        # Modify the line below
        self.buckets = [linked_list.LinkedList() for _ in range(num_buckets)]
        self.length = 0

    def _get_index(self, key):
        hashcode = hash(key)
        return hashcode % self.num_buckets

    def put(self, key, value):
        index = self._get_index(key)
        found_key = False
        for entry in self.buckets[index]:
            if entry.key == key:
                entry.value = value
                found_key = True
        if found_key == False:
            self.buckets[index].append(Entry(key, value))
            self.length += 1

    def get_value(self, key):
        index = self._get_index(key)
        for entry in self.buckets[index]:
            if entry.key == key:
                return entry.value
        raise KeyError(key)

    def delete(self, key):
        index = self._get_index(key)
        new_bucket = linked_list.LinkedList()
        for entry in self.buckets[index]:
            if entry.key != key:
                new_bucket.append(entry)
            if len(new_bucket) < len(self.buckets[index]):
                self.length -= 1
        self.buckets[index] = new_bucket
    
    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __len__(self):
        return self.length

import matplotlib.pyplot as plt

def plot_buckets_sizes(dictionary):
    plt.bar(range(100), [len(dictionary.buckets[i]) for i in range(100)])
    plt.show()
    
import pandas as pd
employees = pd.read_csv("employees.csv", index_col="Id")

# Add code here
dictionary = Dictionary(100)
for identifier, data in employees.iterrows():
    dictionary[identifier] = data
 

plot_buckets_sizes(dictionary)
