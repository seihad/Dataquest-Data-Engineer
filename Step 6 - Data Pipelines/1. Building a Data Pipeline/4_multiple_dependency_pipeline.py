'''2.Intro to DAGs'''
# cycle = [4,6,7]


'''3.The DAG Class'''
# class DAG():
#     def __init__(self):
#         self.graph = {}
    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)

# dag = DAG()
# dag.add(1)
# dag.add(1, 2)
# dag.add(1, 3)
# dag.add(1, 4)
# dag.add(3, 5)
# dag.add(2, 6)
# dag.add(4, 7)
# dag.add(5, 7)
# dag.add(6, 7)

# print(dag.graph)


'''4.Sorting the DAG'''



'''5.Finding Number of In Degrees'''
# class BaseDAG():
#     def __init__(self):
#         self.graph = {}
    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)

# class DAG(BaseDAG):
#     def in_degrees(self):
#         self.degrees = {}
#         for node in self.graph:
#             if node not in self.degrees:
#                 self.degrees[node] = 0
#             for pointed in self.graph[node]:
#                 if pointed not in self.degrees:
#                     self.degrees[pointed] = 0
#                 self.degrees[pointed] += 1

# dag = DAG()
# dag.add(1)
# dag.add(1, 2)
# dag.add(1, 3)
# dag.add(1, 4)
# dag.add(3, 5)
# dag.add(2, 6)
# dag.add(4, 7)
# dag.add(5, 7)
# dag.add(6, 7)
# dag.in_degrees()
# print(dag.graph)
# print(dag.degrees)




'''6.Challenge: Sorting Dependencies'''
# from collections import deque

# class BaseDAG():
#     def __init__(self):
#         self.graph = {}
    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)

# class DAG(BaseDAG):
#     def in_degrees(self):
#         self.degrees = {}
#         for node in self.graph:
#             if node not in self.degrees:
#                 self.degrees[node] = 0
#             for pointed in self.graph[node]:
#                 if pointed not in self.degrees:
#                     self.degrees[pointed] = 0
#                 self.degrees[pointed] += 1

#     def sort(self):
#         self.in_degrees()
#         to_visit = deque()
#         for node in self.graph:
#             if self.degrees[node] == 0:
#                 to_visit.append(node)
        
#         searched = []
#         while to_visit:
#             node = to_visit.popleft()
#             for pointer in self.graph[node]:
#                 self.degrees[pointer] -= 1
#                 if self.degrees[pointer] == 0:
#                     to_visit.append(pointer)
#             searched.append(node)
#         return searched

# dag = DAG()
# dag.add(1)
# dag.add(1, 2)
# dag.add(1, 3)
# dag.add(1, 4)
# dag.add(3, 5)
# dag.add(2, 6)
# dag.add(4, 7)
# dag.add(5, 7)
# dag.add(6, 7)
# dependencies = dag.sort()
# print(dependencies)



'''7.Enhance the Add Method'''
# from collections import deque

# class BaseDAG():
#     def __init__(self):
#         self.graph = {}
    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)

# class DAG(BaseDAG):
#     def in_degrees(self):
#         self.degrees = {}
#         for node in self.graph:
#             if node not in self.degrees:
#                 self.degrees[node] = 0
#             for pointed in self.graph[node]:
#                 if pointed not in self.degrees:
#                     self.degrees[pointed] = 0
#                 self.degrees[pointed] += 1

#     def sort(self):
#         self.in_degrees()
#         to_visit = deque()
#         for node in self.graph:
#             if self.degrees[node] == 0:
#                 to_visit.append(node)
        
#         searched = []
#         while to_visit:
#             node = to_visit.popleft()
#             for pointer in self.graph[node]:
#                 self.degrees[pointer] -= 1
#                 if self.degrees[pointer] == 0:
#                     to_visit.append(pointer)
#             searched.append(node)
#         return searched

    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)
#         # Add validity check.
#         if len(self.sort()) != len(self.graph):
#             raise Exception

# dag = DAG()
# dag.add(1)
# dag.add(1, 2)
# dag.add(1, 3)
# dag.add(1, 4)
# dag.add(3, 5)
# dag.add(2, 6)
# dag.add(4, 7)
# dag.add(5, 7)
# dag.add(6, 7)
# # Add a pointer from 7 to 4, causing a cycle.
# dag.add(7, 4)
# dependencies = dag.sort()
# print(dependencies)

'''8.Adding DAG to the Pipeline'''
# from collections import deque

# class BaseDAG():
#     def __init__(self):
#         self.graph = {}
    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)

# class DAG(BaseDAG):
#     def in_degrees(self):
#         self.degrees = {}
#         for node in self.graph:
#             if node not in self.degrees:
#                 self.degrees[node] = 0
#             for pointed in self.graph[node]:
#                 if pointed not in self.degrees:
#                     self.degrees[pointed] = 0
#                 self.degrees[pointed] += 1

#     def sort(self):
#         self.in_degrees()
#         to_visit = deque()
#         for node in self.graph:
#             if self.degrees[node] == 0:
#                 to_visit.append(node)
        
#         searched = []
#         while to_visit:
#             node = to_visit.popleft()
#             for pointer in self.graph[node]:
#                 self.degrees[pointer] -= 1
#                 if self.degrees[pointer] == 0:
#                     to_visit.append(pointer)
#             searched.append(node)
#         return searched

    
#     def add(self, node, to=None):
#         if not node in self.graph:
#             self.graph[node] = []
#         if to:
#             if not to in self.graph:
#                 self.graph[to] = []
#             self.graph[node].append(to)
#         # Add validity check.
#         if len(self.sort()) != len(self.graph):
#             raise Exception

# class Pipeline():
#     def __init__(self):
#         self.tasks = DAG()
        
#     def task(self, depends_on=None):
#         def inner(f):
#             self.tasks.add(f)
#             if depends_on:
#                 self.tasks.add(depends_on, f)
#             return f
#         return inner

# pipeline = Pipeline()

# pipeline = Pipeline()
# @pipeline.task()
# def first():
#     return 20

# @pipeline.task(depends_on=first)
# def second(x):
#     return x * 2

# @pipeline.task(depends_on=second)
# def third(x):
#     return x // 3

# @pipeline.task(depends_on=second)
# def fourth(x):
#     return x // 4

# graph = pipeline.tasks.graph



'''9.Challenge: Running the Pipeline'''
from collections import deque

class BaseDAG():
    def __init__(self):
        self.graph = {}
    
    def add(self, node, to=None):
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)

class DAG(BaseDAG):
    def in_degrees(self):
        self.degrees = {}
        for node in self.graph:
            if node not in self.degrees:
                self.degrees[node] = 0
            for pointed in self.graph[node]:
                if pointed not in self.degrees:
                    self.degrees[pointed] = 0
                self.degrees[pointed] += 1

    def sort(self):
        self.in_degrees()
        to_visit = deque()
        for node in self.graph:
            if self.degrees[node] == 0:
                to_visit.append(node)
        
        searched = []
        while to_visit:
            node = to_visit.popleft()
            for pointer in self.graph[node]:
                self.degrees[pointer] -= 1
                if self.degrees[pointer] == 0:
                    to_visit.append(pointer)
            searched.append(node)
        return searched

    
    def add(self, node, to=None):
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)
        # Add validity check.
        if len(self.sort()) != len(self.graph):
            raise Exception

class Pipeline():
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner
    
    def run(self):
        scheduled = self.tasks.sort()
        completed = {}
        
        for task in scheduled:
            for node, values in self.tasks.graph.items():
                if task in values:
                    completed[task] = task(completed[node])
            if task not in completed:
                completed[task] = task()
        return completed

pipeline = Pipeline()

pipeline = Pipeline()
@pipeline.task()
def first():
    return 20

@pipeline.task(depends_on=first)
def second(x):
    return x * 2

@pipeline.task(depends_on=second)
def third(x):
    return x // 3

@pipeline.task(depends_on=second)
def fourth(x):
    return x // 4

outputs = pipeline.run()