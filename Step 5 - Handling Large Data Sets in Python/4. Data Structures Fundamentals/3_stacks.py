'''1. Introduction'''
# import linked_list

# class Stack(linked_list.LinkedList):
#     pass

# stack = Stack()
# print(stack.length)

'''2.Push Method'''
# import linked_list

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)

# stack = Stack()
# for i in range(1,4):
#     stack.push(i)

# print(stack)


'''3.Peeking a Stack'''
# import linked_list

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

# stack = Stack()
# for i in range(1,4):
#     stack.push(i)

# print(stack.peek())

'''4.Removing the Top Element'''
# import linked_list

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

#     def pop(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = 0
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# stack = Stack()
# for i in range(1,4):
#     stack.push(i)

# top = stack.pop()

# print(stack.peek())


'''5.LCFS Process Scheduling'''

# import linked_list
# import pandas as pd

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

#     def pop(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = 0
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")
# print(processes.shape)

'''6.Initializing the LCFS Algorithm'''
# import linked_list
# import pandas as pd

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

#     def pop(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = 0
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0
# wait_stack = Stack()
# cur_pid = None


'''7.LCSC Implementation'''
# import linked_list
# import pandas as pd

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

#     def pop(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = 0
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0
# wait_stack = Stack()
# cur_pid = None

# while num_processes_done < processes.shape[0]:
#     # Step 1 goes here
#     if cur_pid is not None:
#         if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
#             processes.loc[cur_pid, "End"] = cur_time
#             cur_pid = None
#             num_processes_done += 1

#     # Step 2 goes here
#     ready_processes = processes[processes["Arrival"] == cur_time]
#     for pid, _ in ready_processes.iterrows():
#         wait_stack.push(pid)

#     # Step 3 goes here
#     if cur_pid is None and len(wait_stack) > 0:
#         cur_pid = wait_stack.pop()
#         processes.loc[cur_pid, "Start"] = cur_time

#     cur_time += 1
# print(processes.head())

'''8.Calculating Wait Times'''

# import linked_list
# import pandas as pd

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

#     def pop(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = 0
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0
# wait_stack = Stack()
# cur_pid = None

# while num_processes_done < processes.shape[0]:
#     # Step 1 goes here
#     if cur_pid is not None:
#         if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
#             processes.loc[cur_pid, "End"] = cur_time
#             cur_pid = None
#             num_processes_done += 1

#     # Step 2 goes here
#     ready_processes = processes[processes["Arrival"] == cur_time]
#     for pid, _ in ready_processes.iterrows():
#         wait_stack.push(pid)

#     # Step 3 goes here
#     if cur_pid is None and len(wait_stack) > 0:
#         cur_pid = wait_stack.pop()
#         processes.loc[cur_pid, "Start"] = cur_time

#     cur_time += 1

# processes["Wait"] = processes["Start"] - processes["Arrival"]
# average_wait_time = processes["Wait"].mean()
# print(average_wait_time)


'''9.Maximum Wait Time'''
# import linked_list
# import pandas as pd

# class Stack(linked_list.LinkedList):
#     def push(self, data):
#         self.append(data)
    
#     def peek(self):
#         return self.tail.data

#     def pop(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = 0
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0
# wait_stack = Stack()
# cur_pid = None

# while num_processes_done < processes.shape[0]:
#     # Step 1 goes here
#     if cur_pid is not None:
#         if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
#             processes.loc[cur_pid, "End"] = cur_time
#             cur_pid = None
#             num_processes_done += 1

#     # Step 2 goes here
#     ready_processes = processes[processes["Arrival"] == cur_time]
#     for pid, _ in ready_processes.iterrows():
#         wait_stack.push(pid)

#     # Step 3 goes here
#     if cur_pid is None and len(wait_stack) > 0:
#         cur_pid = wait_stack.pop()
#         processes.loc[cur_pid, "Start"] = cur_time

#     cur_time += 1

# processes["Wait"] = processes["Start"] - processes["Arrival"]
# average_wait_time = processes["Wait"].mean()
# fcfs_max_wait = processes["FCFS Wait"].max()
# lcfs_max_wait = processes["Wait"].max()
# print(fcfs_max_wait, lcfs_max_wait)


'''10.Calculating Turnaround Times'''

import linked_list
import pandas as pd

class Stack(linked_list.LinkedList):
    def push(self, data):
        self.append(data)
    
    def peek(self):
        return self.tail.data

    def pop(self):
        ret = self.tail.data
        if self.length == 1:
            self.tail = self.head = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret

processes = pd.read_csv("processes.csv", index_col="Pid")

cur_time = 0
num_processes_done = 0
wait_stack = Stack()
cur_pid = None

while num_processes_done < processes.shape[0]:
    # Step 1 goes here
    if cur_pid is not None:
        if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
            processes.loc[cur_pid, "End"] = cur_time
            cur_pid = None
            num_processes_done += 1

    # Step 2 goes here
    ready_processes = processes[processes["Arrival"] == cur_time]
    for pid, _ in ready_processes.iterrows():
        wait_stack.push(pid)

    # Step 3 goes here
    if cur_pid is None and len(wait_stack) > 0:
        cur_pid = wait_stack.pop()
        processes.loc[cur_pid, "Start"] = cur_time

    cur_time += 1

processes["Turnaround"] = processes["End"] - processes["Arrival"]
average_turnaround_time = processes["Turnaround"].mean()
print(average_turnaround_time)