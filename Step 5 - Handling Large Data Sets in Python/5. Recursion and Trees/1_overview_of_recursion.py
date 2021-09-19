'''2.Recursive Sum'''
# fruits = ["apple", "orange", "pear", "fig", "passionfruit"]
# def list_len(lst):
#     if not lst:
#         return 0
#     return 1 + list_len(lst[1:])

# num_fruits = list_len(fruits)
# print(num_fruits)


'''3.Stack Overflow'''
# fruits = ["apple", "orange", "pear", "fig", "passionfruit"]

# def list_len(lst):
#     return 1 + list_len(lst[1:])
# list_len(fruits)

'''4.Towers of Hanoi'''
# def solve_hanoi(num_disks, first_peg, middle_peg, last_peg):
#     if num_disks == 1:
#         # Base case
#         print("Move the top disk from peg {} to peg {}.".format(first_peg, last_peg))
#     else:
#         # General Case
#         # Instruction 1: Add code to solve the first subproblem
#         solve_hanoi(num_disks - 1, first_peg, last_peg, middle_peg)
        
#         # Second subproblem: Move disk num_disks from first_peg to last_peg
#         solve_hanoi(1, first_peg, middle_peg, last_peg)
        
#         # Instruction 2: Add code to solve the third subproblem
#         solve_hanoi(num_disks - 1, middle_peg, first_peg, last_peg)

# solve_hanoi(3, 'A', 'B', 'C')


'''5.Recursive Thinking'''



'''6.Listing All Files in a Directory'''
# import os
# def list_files(current_path):
#     #Base case
#     if not os.path.isdir(current_path):
#         print(current_path)
#     else:
#         # General case
#         for name in os.listdir(current_path):
#             file_path = os.path.join(current_path, name)
#             list_files(file_path)
            
# list_files("folder1")



'''7.Merge Sort (Part 1)'''
# def merge_sorted_lists(list1, list2):
#     index1 = 0
#     index2 = 0
#     merged_list = []
#     while index1 < len(list1) and index2 < len(list2):
#         if list1[index1] < list2[index2]:
#             merged_list.append(list1[index1])
#             index1 += 1
#         else:
#             merged_list.append(list2[index2])
#             index2 += 1
#     merged_list += list1[index1:]
#     merged_list += list2[index2:]
#     return merged_list

# merged_lists = merge_sorted_lists([2,4,7,8], [1,3,5,6])
# print(merged_lists)


'''8.Merge Sort (Part 2)'''
def merge_sorted_lists(list1, list2):
    index1 = 0
    index2 = 0
    merged_list = []
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1
    merged_list += list1[index1:]
    merged_list += list2[index2:]
    return merged_list

def merge_sort(values):
    if len(values) < 2:
        return values
    midpoint = len(values) // 2
    sorted_first_half = merge_sort(values[:midpoint])
    sorted_second_half = merge_sort(values[midpoint:])
    return merge_sorted_lists(sorted_first_half, sorted_second_half)

print(merge_sort([2, 4, 7, 8, 1, 3, 5, 6]))


'''9.Analysis of Merge Sort'''