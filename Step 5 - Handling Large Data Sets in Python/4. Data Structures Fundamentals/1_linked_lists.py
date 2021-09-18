'''1.Introduction'''
# class Book:
#     def __init__(self, name, num_pages):
#         self.name = name
#         self.num_pages = num_pages
# book = Book("Lord of the Flies", 228)
# print(book.name)


'''2.Linked Structure'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node = Node(42)

# print(node.data)


'''3.Head and Tail'''
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

# lst = LinkedList()


'''4.Appending to a Linked List'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     # Implement append() method here
#     def append(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1

# lst = LinkedList()
# lst.append(10)
# print(lst.length, lst.head.data, lst.tail.data)
# lst.append(11)
# print(lst.length, lst.head.data, lst.tail.data)


'''5.Iterating Over List Elements Part 1'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     # Implement append() method here
#     def append(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1

#     def __iter__(self):
#         self._iter_node = self.head
#         return self



'''6.Iterating Over List Elements Part 2'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     # Implement append() method here
#     def append(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1

#     def __iter__(self):
#         self._iter_node = self.head
#         return self
    
#     def __next__(self):
#         if self._iter_node is None:
#             raise StopIteration
#         ret = self._iter_node.data
#         self._iter_node = self._iter_node.next
#         return ret

# lst = LinkedList()
# lst.append(5)
# lst.append(3)
# lst.append(8)
# for value in lst:
#     print(value)




'''7.Prepending Elements'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     # Implement append() method here
#     def append(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1

#     def __iter__(self):
#         self._iter_node = self.head
#         return self
    
#     def __next__(self):
#         if self._iter_node is None:
#             raise StopIteration
#         ret = self._iter_node.data
#         self._iter_node = self._iter_node.next
#         return ret
    
#     def prepend(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.head.prev = new_node
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1

# lst = LinkedList()
# lst.prepend(10)
# print(lst.length, lst.head.data, lst.tail.data)
# lst.prepend(11)
# print(lst.length, lst.head.data, lst.tail.data)




'''8.Length of a List'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     # Implement append() method here
#     def append(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1

#     def __iter__(self):
#         self._iter_node = self.head
#         return self
    
#     def __next__(self):
#         if self._iter_node is None:
#             raise StopIteration
#         ret = self._iter_node.data
#         self._iter_node = self._iter_node.next
#         return ret
    
#     def prepend(self, data):
#         new_node = Node(data)
#         if self.length == 0:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             self.head.prev = new_node
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
    
#     def __len__(self):
#         return self.length

# lst = LinkedList()
# lst.append(10)
# print(len(lst))


'''9.String Representation'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # Implement append() method here
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        ret = self._iter_node.data
        self._iter_node = self._iter_node.next
        return ret
    
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def __len__(self):
        return self.length

    def __str__(self):
        return str([value for value in self])

lst = LinkedList()
print(lst)

lst.append(1)
print(lst)

lst.append(2)
print(lst)

