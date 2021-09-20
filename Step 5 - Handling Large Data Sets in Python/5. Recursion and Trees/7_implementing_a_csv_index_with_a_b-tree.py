'''1.Introduction'''
# import csv
# with open('ratings.csv') as file:
#     reader = csv.reader(file)
#     rows = list(reader)
#     header = rows[0]
#     rows = rows[1:]

# print(len(rows))

'''2.Extending the B-tree'''
# from btree import BTree

# class CSVIndex(BTree):
#     def __init__(self, split_threshold):
#         super().__init__(split_threshold)

# index = CSVIndex(10)


'''3.Reading the CSV Into the Tree'''
# from btree import BTree
# import csv

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name # Instruction 2
#         with open(csv_filename) as file: # Instruction 3.1
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name) # Instruction 3.2
#             for row in rows: # Instruction 3.3
#                 self.add(float(row[col_index]), row)

# metacritic_index = CSVIndex(2, "ratings.csv", "Metacritic")
# print(len(metacritic_index))





'''4.Movie Lookup'''
# from btree import BTree
# import csv

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name # Instruction 2
#         with open(csv_filename) as file: # Instruction 3.1
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name) # Instruction 3.2
#             for row in rows: # Instruction 3.3
#                 self.add(float(row[col_index]), row)

# index = CSVIndex(3, "ratings.csv", "Imdb")
# movie_6_3 = index.get_value(6.3)
# movie_8_5 = index.get_value(8.5)
# print(movie_6_3)
# print(movie_8_5)



'''5.Implementing Range Queries'''
# from btree import BTree
# import csv

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name # Instruction 2
#         with open(csv_filename) as file: # Instruction 3.1
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name) # Instruction 3.2
#             for row in rows: # Instruction 3.3
#                 self.add(float(row[col_index]), row)
    
#     def _range_query(self, range_start, range_end, current_node, min_key, max_key): 
#         if range_start > max_key or range_end < min_key: 
#             return []
#         results = [] 
#         for i, key in enumerate(current_node.keys): 
#             if range_start <= key and key <= range_end:
#                 results.append(current_node.values[i])
#         return results




'''6.Implementing Range Queries'''
# from btree import BTree
# import csv

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name
#         with open(csv_filename) as file:
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name)
#             for row in rows:
#                 self.add(float(row[col_index]), row)
                
#     def _range_query(self, range_start, range_end, current_node, min_key, max_key):
#         if range_start > max_key or range_end < min_key:
#             return []
#         results = []
#         for i, key in enumerate(current_node.keys):
#             if range_start <= key and key <= range_end:
#                 results.append(current_node.values[i])
#         # Add code here
#         if not current_node.is_leaf(): 
#             for i, child in enumerate(current_node.children):
#                 new_min_key = min_key if i == 0 else current_node.keys[i - 1]
#                 new_max_key = max_key if i == len(current_node) else current_node.keys[i] 
#                 results += self._range_query(range_start, range_end, child, new_min_key, new_max_key) 
#         return results



'''7.Polishing the Range Query Method'''
# from btree import BTree
# import csv

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name
#         with open(csv_filename) as file:
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name)
#             for row in rows:
#                 self.add(float(row[col_index]), row)
                
#     def _range_query(self, range_start, range_end, current_node, min_key, max_key):
#         if range_start > max_key or range_end < min_key:
#             return []
#         results = []
#         for i, key in enumerate(current_node.keys):
#             if range_start <= key and key <= range_end:
#                 results.append(current_node.values[i])
#         if not current_node.is_leaf():
#             for i, child in enumerate(current_node.children):
#                 new_min_key = current_node.keys[i - 1] if i > 0 else min_key
#                 new_max_key = current_node.keys[i] if i < len(current_node) else max_key
#                 results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
#         return results 
    
#     # Add method here
#     def range_query(self, range_start, range_end):
#         return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))


'''8.Complexity of Range Queries'''
# from btree import BTree
# import csv

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name
#         with open(csv_filename) as file:
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name)
#             for row in rows:
#                 self.add(float(row[col_index]), row)
                
#     def _range_query(self, range_start, range_end, current_node, min_key, max_key):
#         if range_start > max_key or range_end < min_key:
#             return []
#         results = []
#         for i, key in enumerate(current_node.keys):
#             if range_start <= key and key <= range_end:
#                 results.append(current_node.values[i])
#         if not current_node.is_leaf():
#             for i, child in enumerate(current_node.children):
#                 new_min_key = current_node.keys[i - 1] if i > 0 else min_key
#                 new_max_key = current_node.keys[i] if i < len(current_node) else max_key
#                 results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
#         return results 
    
#     # Add method here
#     def range_query(self, range_start, range_end):
#         return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))
    

# index = CSVIndex(2, "ratings.csv", "Rotten_Tomatoes")
# low_rating = index.range_query(0, 15)

# for result in low_rating:
#     print(result)

# high_rating = index.range_query(90, 100)
# for result in high_rating:
#     print(result)




'''9.Saving the Index'''
# from btree import BTree
# import csv
# import pickle

# class CSVIndex(BTree):

#     def __init__(self, split_threshold, csv_filename, col_name):
#         super().__init__(split_threshold)
#         self.col_name = col_name
#         with open(csv_filename) as file:
#             rows = list(csv.reader(file))
#             header = rows[0]
#             rows = rows[1:]
#             col_index = header.index(col_name)
#             for row in rows:
#                 self.add(float(row[col_index]), row)
                
#     def _range_query(self, range_start, range_end, current_node, min_key, max_key):
#         if range_start > max_key or range_end < min_key:
#             return []
#         results = []
#         for i, key in enumerate(current_node.keys):
#             if range_start <= key and key <= range_end:
#                 results.append(current_node.values[i])
#         if not current_node.is_leaf():
#             for i, child in enumerate(current_node.children):
#                 new_min_key = current_node.keys[i - 1] if i > 0 else min_key
#                 new_max_key = current_node.keys[i] if i < len(current_node) else max_key
#                 results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
#         return results 
    
#     # Add method here
#     def range_query(self, range_start, range_end):
#         return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))
    
#     def save(self, filename):
#         with open(filename + ".pickle", 'wb'):
#             with open('{}.pickle'.format(filename), 'wb') as f:
#                 pickle.dump(self, f)

# fandago_index = CSVIndex(10, "ratings.csv", "Fandango")
# fandago_index.save('fandango')
            



'''10.Loading the Index'''
from btree import BTree
import csv
import pickle

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)
                
    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_start > max_key or range_end < min_key:
            return []
        results = []
        for i, key in enumerate(current_node.keys):
            if range_start <= key and key <= range_end:
                results.append(current_node.values[i])
        if not current_node.is_leaf():
            for i, child in enumerate(current_node.children):
                new_min_key = current_node.keys[i - 1] if i > 0 else min_key
                new_max_key = current_node.keys[i] if i < len(current_node) else max_key
                results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
        return results 
    
    # Add method here
    def range_query(self, range_start, range_end):
        return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))
    
    def save(self, filename):
        with open(filename + ".pickle", 'wb'):
            with open('{}.pickle'.format(filename), 'wb') as f:
                pickle.dump(self, f)
    
    @staticmethod
    def load(filename):
        with open('{}.pickle'.format(filename), 'rb') as f:
            return pickle.load(f)


loaded_index = CSVIndex.load('fandango')
print(loaded_index.col_name)

    

