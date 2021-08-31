'''
1.Space Complexity
'''
# def make_table2(N):
#     table = []
#     for _ in range(N):
#         row = []
#         for _ in range(N):
#             row.append([1 for _ in range(N)])
#         table.append(row)
#     return table

# # Proposed complexities
# space_complexity1 = "O(N)"
# space_complexity2 = "O(N^2)"
# space_complexity3 = "O(N^3)"

# # Assign the space complexity of make_table2() to answer
# answer = space_complexity3

# print(make_table2(3))

'''
2. Primary and Secondary Memory
'''
# class Person():
    
#     def __init__(self, name, age):
#         self.name = name     #L
#         self.age = age      

# import csv
# def read_persons():
#     persons = []
#     with open('persons.csv') as f:
#         next(f)
#         rows = list(csv.reader(f)) #P
#         for row in rows:
#             person = Person(row[0], int(row[1])) #P * L
#             persons.append(person) #P * L
#     return persons

# # proposed complexities
# space_complexity1 = "O(P)"
# space_complexity2 = "O(P + L)"
# space_complexity3 = "O(P * L)"
# space_complexity4 = "O(L)"

# #Remember that the space complexity of each Person instance is O(len(name)) = O(L). Think about how many of those instances we are creating.

# # Assign the space complexity of read_persons() to answer
# answer = space_complexity3

'''
3. Memory and Speed Tradeoff
'''
# # Provided input
# test_values = [4, 6, 3, 9, 1]
# test_targets = [9, 0, 3]      
# # Expected output: {9: True, 0: False, 3: True}

# # Write your code below
# def find_target_faster(values, targets):
#     value_set = set(values)
#     found = {}
#     for target in targets:
#         found[target] = target in value_set
#     return found

# print(find_target_faster(test_values, test_targets))

'''
4. Pair Sums Problem
'''
# # Provided input
# test_values = [1, 2, 5]
# test_targets = [2, 3, 7, 8]      
# # Expected output:
# # {2: True, 3: True, 7: True, 8: False}

# # Write your code below
# def find_sums(values, target_sums):
#     sums = {}
#     for target in target_sums:
#         sums[target] = False
#         for i in range(len(values)):
#             for j in range(i, len(values)):
#                 if values[i] + values[j] == target:
#                     sums[target] = True
#     return sums

# print(find_sums(test_values, test_targets))

'''
5. Precomputing to Reduce Time Complexity
'''
# # Provided input
# test_values = [1, 2, 5]
# test_targets = [2, 3, 7, 8]      
# # Expected output: 
# # ({2: True, 3: True, 7: True, 8: False}, {2, 3, 4, 6, 7, 10})

# # Write your code below
# def find_sums_precompute(values, target_sums):
#     possible_sums = set()
#     for i in range(len(values)):
#         for j in range(i, len(values)):
#             possible_sums.add(values[i] + values[j])
#     sums = {}
#     for target in target_sums:
#         sums[target] = target in possible_sums
#     return sums, possible_sums

# print(find_sums_precompute(test_values, test_targets))

'''
6. Balancing Time and Space
'''
# # Provided input
# test_values = [1, 2, 5]
# test_targets = [2, 3, 7, 8]      
# # Expected output: 
# # ({2: True, 3: True, 7: True, 8: False}, {1, 2, 5})

# # Write your code below
# def find_sums_balanced(values, target_sums):
#     value_set = set(values)
#     sums = {}
#     for target in target_sums:
#         sums[target] = False
#         for value1 in values:
#             value2 = value1 - target
#             if value2 in value_set:
#                  sums[target] = True
#     return sums, value_set

# print(find_sums_balanced(test_values, test_targets))

'''
8. Challenge (pairs cannot be the same)
'''
# Provided input
values = [1, 2, 5]
targets = [2, 3, 7, 8]      
# Expected output: 
# {2: False, 3: True, 7: True, 8: False}

# Write your code below
def find_sums_distinct(values, target_sums):
    value_set = set(values)
    sums = {}
    for target in target_sums:
        sums[target] = False
        for value1 in values:
            value2 = target - value1
            if value2 in value_set and value1 != value2:
                sums[target] = True
    return sums

print(find_sums_distinct(values, targets))
