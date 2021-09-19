'''1.Introduction'''
# root = 5
# leaves = [1, 6, 10]
# internal = [3,9,8]


'''2.Binary Tree Node Structure'''
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None



'''3.Building Your First Tree'''
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None

# node_1 = Node(1)
# node_3 = Node(3)
# node_5 = Node(5)
# node_9 = Node(9)
# node_8 = Node(8)
# node_6 = Node(6)
# node_10 = Node(10)

# node_3.left_child = node_1
# node_5.left_child = node_3
# node_5.right_child = node_9
# node_9.left_child = node_8
# node_9.right_child = node_10
# node_8.left_child = node_6



'''4.Binary Search Trees'''
# class BST:
#     def __init__(self):
#         self.root = None



'''5.BST Inserting Values'''
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None

# class BST:
    
#     def __init__(self):
#         self.root = None
        
#     def add(self, value):
#         if self.root is None:
#             # The root does exist yet, create it
#             self.root = Node(value)
#         else:
#             # Find the right place and insert new value
#             self.add_recursive(self.root, value)
            
#     # Define and implement the add_recursive() method here
#     def add_recursive(self, current_node, value):
#         if value <= current_node.value:
#             if current_node.left_child is None:
#                 current_node.left_child = Node(value)
#             else:
#                 self.add_recursive(current_node.left_child, value)
#         elif value >= current_node.value:
#             if current_node.right_child is None:
#                 current_node.right_child = Node(value)
#             else:
#                 self.add_recursive(current_node.right_child, value)



'''6.BST Contains'''
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None

# class BST:
    
#     def __init__(self):
#         self.root = None
        
#     def add(self, value):
#         if self.root is None:
#             # The root does exist yet, create it
#             self.root = Node(value)
#         else:
#             # Find the right place and insert new value
#             self.add_recursive(self.root, value)
            
#     # Define and implement the add_recursive() method here
#     def add_recursive(self, current_node, value):
#         if value <= current_node.value:
#             if current_node.left_child is None:
#                 current_node.left_child = Node(value)
#             else:
#                 self.add_recursive(current_node.left_child, value)
#         elif value >= current_node.value:
#             if current_node.right_child is None:
#                 current_node.right_child = Node(value)
#             else:
#                 self.add_recursive(current_node.right_child, value)
    
#     def contains(self, current_node, value):
#         if current_node is None:
#             return False
#         else:
#             if value == current_node.value:
#                 return True
#             elif value < current_node.value:
#                 return self.contains(current_node.left_child, value)
#             else:
#                 return self.contains(current_node.right_child, value)


'''7.Polishing the Implementation'''
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None

# class BST:
    
#     def __init__(self):
#         self.root = None
        
#     def add(self, value):
#         if self.root is None:
#             # The root does exist yet, create it
#             self.root = Node(value)
#         else:
#             # Find the right place and insert new value
#             self._add_recursive(self.root, value)
            
#     # Define and implement the add_recursive() method here
#     def _add_recursive(self, current_node, value):
#         if value <= current_node.value:
#             if current_node.left_child is None:
#                 current_node.left_child = Node(value)
#             else:
#                 self._add_recursive(current_node.left_child, value)
#         elif value >= current_node.value:
#             if current_node.right_child is None:
#                 current_node.right_child = Node(value)
#             else:
#                 self._add_recursive(current_node.right_child, value)
    
#     def _contains(self, current_node, value):
#         if current_node is None:
#             return False
#         else:
#             if value == current_node.value:
#                 return True
#             elif value < current_node.value:
#                 return self._contains(current_node.left_child, value)
#             else:
#                 return self._contains(current_node.right_child, value)
    
#     def contains(self, value):
#         return self._contains(self.root, value)


'''8.Building Your Second Tree'''
# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None

# class BST:
    
#     def __init__(self):
#         self.root = None
        
#     def add(self, value):
#         if self.root is None:
#             # The root does exist yet, create it
#             self.root = Node(value)
#         else:
#             # Find the right place and insert new value
#             self._add_recursive(self.root, value)
            
#     # Define and implement the add_recursive() method here
#     def _add_recursive(self, current_node, value):
#         if value <= current_node.value:
#             if current_node.left_child is None:
#                 current_node.left_child = Node(value)
#             else:
#                 self._add_recursive(current_node.left_child, value)
#         elif value >= current_node.value:
#             if current_node.right_child is None:
#                 current_node.right_child = Node(value)
#             else:
#                 self._add_recursive(current_node.right_child, value)
    
#     def _contains(self, current_node, value):
#         if current_node is None:
#             return False
#         else:
#             if value == current_node.value:
#                 return True
#             elif value < current_node.value:
#                 return self._contains(current_node.left_child, value)
#             else:
#                 return self._contains(current_node.right_child, value)
    
#     def contains(self, value):
#         return self._contains(self.root, value)

# bst = BST()
# for value in [5, 3, 9, 1, 8, 10, 6]:
#     bst.add(value)




'''9.BST Complexity'''
