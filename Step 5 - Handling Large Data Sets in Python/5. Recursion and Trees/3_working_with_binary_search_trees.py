'''1.Introduction to AVL Trees'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0

'''2.Node Height and Imbalance'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height
        


'''3.Keeping Height and Imbalance Updated'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height
    
# avl = AVLTree()
# avl.add(1)
# avl.add(2)
# avl.add(3)
# height = avl.get_height()
# print(height)


'''4.Imbalance and Height Relation''' 


'''5.Left Rotation'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height

#     def _rotate_left(self, node):
#         pivot = node.right_child
#         node.right_child = pivot.left_child
#         pivot.left_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot


'''6.Right Rotation'''

# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height

#     def _rotate_left(self, node):
#         pivot = node.right_child
#         node.right_child = pivot.left_child
#         pivot.left_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _rotate_right(self, node):
#         pivot = node.left_child
#         node.left_child = pivot.right_child
#         pivot.right_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot


'''7.Balancing the Tree — Part 1'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height

#     def _rotate_left(self, node):
#         pivot = node.right_child
#         node.right_child = pivot.left_child
#         pivot.left_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _rotate_right(self, node):
#         pivot = node.left_child
#         node.left_child = pivot.right_child
#         pivot.right_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _balance(self, node):
#         if node.imbalance == 2:
#             pivot = node.left_child
#             if pivot.imbalance == 1:
#                 return self._rotate_right(node)
            

'''8.Balancing the Tree — Part 2'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height

#     def _rotate_left(self, node):
#         pivot = node.right_child
#         node.right_child = pivot.left_child
#         pivot.left_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _rotate_right(self, node):
#         pivot = node.left_child
#         node.left_child = pivot.right_child
#         pivot.right_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _balance(self, node):
#         if node.imbalance == 2:
#             pivot = node.left_child
#             if pivot.imbalance == 1:
#                 return self._rotate_right(node)
#             else:
#                 node.left_child = self._rotate_left(pivot)
#                 return self._rotate_right(node)


'''9.Balancing the Tree — Part 3'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height

#     def _rotate_left(self, node):
#         pivot = node.right_child
#         node.right_child = pivot.left_child
#         pivot.left_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _rotate_right(self, node):
#         pivot = node.left_child
#         node.left_child = pivot.right_child
#         pivot.right_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _balance(self, node):
#         if node.imbalance == 2:
#             pivot = node.left_child
#             if pivot.imbalance == 1:
#                 return self._rotate_right(node)
#             else:
#                 node.left_child = self._rotate_left(pivot)
#                 return self._rotate_right(node)
#         elif node.imbalance == -2:
#             pivot = node.right_child
#             if pivot.imbalance == -1:
#                 return self._rotate_left(node)
#             else:
#                 node.right_child = self._rotate_right(pivot)
#                 return self._rotate_left(node)



'''10.Balancing on Insertion'''
# from bst import Node, BST
# class AVLNode(Node):
#     def __init__(self, value):
#         super().__init__(value)
#         self.height = 1
#         self.imbalance = 0
    
#     def calculate_height_and_imbalance(self):
#         # Calculate left height
#         left_height = 0
#         if self.left_child is not None:
#             left_height = self.left_child.height
#         # Calculate right height
#         right_height = 0
#         if self.right_child is not None:
#             right_height = self.right_child.height
#         # Use formulas to calculate height and imbalance
#         self.height = 1 + max(left_height, right_height)
#         self.imbalance = left_height - right_height

# class AVLTree(BST):
    
#     def __init__(self):
#         super().__init__()
        
#     def _add_recursive(self, current_node, value):
#         if current_node is None:
#             return AVLNode(value)
#         if value <= current_node.value:
#             current_node.left_child = self._add_recursive(current_node.left_child, value)
#         else:
#             current_node.right_child = self._add_recursive(current_node.right_child, value)
#         # Add code here to calculate the height and balance of the current node
#         current_node.calculate_height_and_imbalance()
#         if abs(current_node.imbalance) == 2:
#             return self._balance(current_node)
#         return current_node

#     # Add get_height() method here
#     def get_height(self):
#         return self.root.height

#     def _rotate_left(self, node):
#         pivot = node.right_child
#         node.right_child = pivot.left_child
#         pivot.left_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _rotate_right(self, node):
#         pivot = node.left_child
#         node.left_child = pivot.right_child
#         pivot.right_child = node
#         node.calculate_height_and_imbalance()
#         pivot.calculate_height_and_imbalance()
#         return pivot
    
#     def _balance(self, node):
#         if node.imbalance == 2:
#             pivot = node.left_child
#             if pivot.imbalance == 1:
#                 return self._rotate_right(node)
#             else:
#                 node.left_child = self._rotate_left(pivot)
#                 return self._rotate_right(node)
#         elif node.imbalance == -2:
#             pivot = node.right_child
#             if pivot.imbalance == -1:
#                 return self._rotate_left(node)
#             else:
#                 node.right_child = self._rotate_right(pivot)
#                 return self._rotate_left(node)



'''11.Testing the Implementation'''
from bst import Node, BST
class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1
        self.imbalance = 0
    
    def calculate_height_and_imbalance(self):
        # Calculate left height
        left_height = 0
        if self.left_child is not None:
            left_height = self.left_child.height
        # Calculate right height
        right_height = 0
        if self.right_child is not None:
            right_height = self.right_child.height
        # Use formulas to calculate height and imbalance
        self.height = 1 + max(left_height, right_height)
        self.imbalance = left_height - right_height

class AVLTree(BST):
    
    def __init__(self):
        super().__init__()
        
    def _add_recursive(self, current_node, value):
        if current_node is None:
            return AVLNode(value)
        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)
        # Add code here to calculate the height and balance of the current node
        current_node.calculate_height_and_imbalance()
        if abs(current_node.imbalance) == 2:
            return self._balance(current_node)
        return current_node

    # Add get_height() method here
    def get_height(self):
        return self.root.height

    def _rotate_left(self, node):
        pivot = node.right_child
        node.right_child = pivot.left_child
        pivot.left_child = node
        node.calculate_height_and_imbalance()
        pivot.calculate_height_and_imbalance()
        return pivot
    
    def _rotate_right(self, node):
        pivot = node.left_child
        node.left_child = pivot.right_child
        pivot.right_child = node
        node.calculate_height_and_imbalance()
        pivot.calculate_height_and_imbalance()
        return pivot
    
    def _balance(self, node):
        if node.imbalance == 2:
            pivot = node.left_child
            if pivot.imbalance == 1:
                return self._rotate_right(node)
            else:
                node.left_child = self._rotate_left(pivot)
                return self._rotate_right(node)
        elif node.imbalance == -2:
            pivot = node.right_child
            if pivot.imbalance == -1:
                return self._rotate_left(node)
            else:
                node.right_child = self._rotate_right(pivot)
                return self._rotate_left(node)

avl = AVLTree()
avl.add(42)
assert avl.contains(42), "The AVL tree doesn't contain the value 42 after it was added."