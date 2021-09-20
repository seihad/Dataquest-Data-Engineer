'''1.Introduction'''
# from node import Node
# class BTree():
    
#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0
    
#     def __len__(self):
#         return self.size

'''2.Key Lookup'''
# from typing import Counter
# from node import *

# class BTree:

#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0

#     def __len__(self):
#         return self.size
    
#     # Add method here
#     def find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key)
#         return self.find_node(current_node.children[child_index], key)




'''3.Helper Method for Contains'''
# from node import *

# class BTree:

#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0

#     def __len__(self):
#         return self.size
    
#     def _find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key)
#         return self._find_node(current_node.children[child_index], key)
    
#     # Add method here
#     def contains(self, key):
#         node = self._find_node(self.root, key)
#         return node is not None




'''4.Value Lookup'''
# from node import *

# class BTree:

#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0

#     def __len__(self):
#         return self.size
    
#     def _find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key) 
#         return self._find_node(current_node.children[child_index], key)
    
#     def contains(self, key):
#         node = self._find_node(self.root, key)
#         return not node is None
    
#     # Add method here
#     def get_value(self, key):
#         node = self._find_node(self.root, key)
#         if node is None:
#             return None
#         else:
#             return node.get_value(key)



'''5.Adding Entries'''
# from node import *

# class BTree:

#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0

#     def __len__(self):
#         return self.size
    
#     def _find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key) 
#         return self._find_node(current_node.children[child_index], key)
    
#     def contains(self, key):
#         node = self._find_node(self.root, key)
#         return not node is None
    
#     def get_value(self, key):
#         node = self._find_node(self.root, key)
#         if node is None:
#             return None
#         return node.get_value(key)
    
#     # Add method here
#     def add(self, current_node, key, value):
#         if current_node.is_leaf():
#             current_node.insert_entry(key, value)
#         else:
#             child_index = current_node.get_insert_index(key)
#             self.add(current_node.children[child_index], key, value)




'''6.Helper Method for Add'''
# from node import *

# class BTree:

#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0

#     def __len__(self):
#         return self.size
    
#     def _find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key) 
#         return self._find_node(current_node.children[child_index], key)
    
#     def contains(self, key):
#         node = self._find_node(self.root, key)
#         return not node is None
    
#     def get_value(self, key):
#         node = self._find_node(self.root, key)
#         if node is None:
#             return None
#         return node.get_value(key)
    
#     def _add(self, current_node, key, value):
#         if current_node.is_leaf(): 
#             current_node.insert_entry(key, value)
#         else:
#             child_index = current_node.get_insert_index(key)
#             self._add(current_node.children[child_index], key, value)
            
#     # Add method here
#     def add(self, key, value):
#         self._add(self.root, key, value)
#         self.size += 1




'''7.Testing the Implementation'''
# from node import *

# class BTree:

#     def __init__(self):
#         self.root = Node()
#         self.height = 0
#         self.size = 0

#     def __len__(self):
#         return self.size
    
#     def _find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key) 
#         return self._find_node(current_node.children[child_index], key)
    
#     def contains(self, key):
#         node = self._find_node(self.root, key)
#         return not node is None
    
#     def get_value(self, key):
#         node = self._find_node(self.root, key)
#         if node is None:
#             return None
#         return node.get_value(key)
    
#     def _add(self, current_node, key, value):
#         if current_node.is_leaf(): 
#             current_node.insert_entry(key, value)
#         else:
#             child_index = current_node.get_insert_index(key)
#             self._add(current_node.children[child_index], key, value)
            
#     # Add method here
#     def add(self, key, value):
#         self._add(self.root, key, value)
#         self.size += 1

# bt = BTree()

# for i in range(1,11):
#     bt.add(i, i)

# print(bt.root.keys)

# print(bt.root.children)




'''8.Node Splitting'''
# from node import *

# class BTree:

#     def __init__(self, split_threshold):
#         self.root = Node()
#         self.height = 0
#         self.size = 0
#         self.split_threshold = split_threshold

#     def __len__(self):
#         return self.size
    
#     def _find_node(self, current_node, key):
#         if current_node.contains_key(key):
#             return current_node
#         if current_node.is_leaf():
#             return None
#         child_index = current_node.get_insert_index(key) 
#         return self._find_node(current_node.children[child_index], key)
    
#     def contains(self, key):
#         node = self._find_node(self.root, key)
#         return not node is None
    
#     def get_value(self, key):
#         node = self._find_node(self.root, key)
#         if node is None:
#             return None
#         return node.get_value(key)
    
#     def _add(self, current_node, key, value):
#         if current_node.is_leaf(): 
#             current_node.insert_entry(key, value)
#         else:
#             child_index = current_node.get_insert_index(key)
#             self._add(current_node.children[child_index], key, value)
        
#         if len(current_node) > self.split_threshold: # Instruction 3
#             parent = current_node.split() # Instruction 3.1
#             if current_node == self.root: # Intruction 3.2
#                 self.root = parent
            
#     # Add method here
#     def add(self, key, value):
#         self._add(self.root, key, value)
#         self.size += 1





'''9.Complexity Analysis'''
from node import *
import matplotlib.pyplot as plt

class BTree:

    def __init__(self, split_threshold):
        self.root = Node()
        self.height = 0
        self.size = 0
        self.split_threshold = split_threshold

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        return not node is None
    
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)
    
    def _add(self, current_node, key, value):
        if current_node.is_leaf(): 
            current_node.insert_entry(key, value)
        else:
            child_index = current_node.get_insert_index(key)
            self._add(current_node.children[child_index], key, value)
        
        if len(current_node) > self.split_threshold: # Instruction 3
            parent = current_node.split() # Instruction 3.1
            if current_node == self.root: # Intruction 3.2
                self.root = parent
                self.height += 1
        
            
    # Add method here
    def add(self, key, value):
        self._add(self.root, key, value)
        self.size += 1
        

bt = BTree(2)
heights = []
for i in range(1,1001):
    bt.add(i, i)
    heights.append(bt.height)

plt.plot(heights)
plt.show()