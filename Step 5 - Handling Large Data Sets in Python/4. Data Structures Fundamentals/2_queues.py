'''1.Introduction'''
# import linked_list

# class Queue(linked_list.LinkedList):
#     pass

# queue = Queue()
# print(queue.length)



'''2.Enqueue Method'''
# import linked_list

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print(queue)

'''3.Getting the Front Element'''

# import linked_list

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)
    
#     def get_front(self):
#         return self.tail.data

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue.get_front())


'''4.Removing the Front Element'''

# import linked_list

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)
    
#     def get_front(self):
#         return self.tail.data
    
#     def dequeue(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.head = self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# front = queue.dequeue()
# print(queue.get_front())


'''5.FCFS Process Scheduling'''
# import linked_list
# import pandas as pd

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)
    
#     def get_front(self):
#         return self.tail.data
    
#     def dequeue(self):
#         ret = self.tail.data
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# process = pd.read_csv("processes.csv", index_col="Pid")
# print(process.shape)


'''6.Initializing the FCFS Algorithm'''
# import linked_list
# import pandas as pd

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)
    
#     def get_front(self):
#         return self.tail.data
    
#     def dequeue(self):
#         ret = self.tail.data
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# process = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0

# wait_queue = Queue()
# cur_pid = None


'''7.FCSC Implementation'''
# import linked_list
# import pandas as pd

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)
    
#     def get_front(self):
#         return self.tail.data
    
#     def dequeue(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0

# wait_queue = Queue()
# cur_pid = None


# # Copy and paste tempalte code here
# while num_processes_done < processes.shape[0]:
#     # Check if current process finished
#     if cur_pid is not None:
#         if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
#             # Step 1 code goes here
#             processes.loc[cur_pid, "End"] = cur_time
#             cur_pid = None
#             num_processes_done += 1
#     # Handle arriving processes
#     # Step 2 code goes here
#     ready_processes = processes[processes["Arrival"] == cur_time]
#     for pid, _ in ready_processes.iterrows():
#         wait_queue.enqueue(pid)
#     # Assign a process to the processor
#     if cur_pid is None and len(wait_queue) > 0:
#         # Step 3 code goes here
#         cur_pid = wait_queue.dequeue()
#         processes.loc[cur_pid, "Start"] = cur_time 
#     cur_time += 1
    
# print(processes.head())


'''8.Calculating Wait Times'''

# import linked_list
# import pandas as pd

# class Queue(linked_list.LinkedList):
#     def enqueue(self, data):
#         self.prepend(data)
    
#     def get_front(self):
#         return self.tail.data
    
#     def dequeue(self):
#         ret = self.tail.data
#         if self.length == 1:
#             self.tail = self.head = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         self.length -= 1
#         return ret

# processes = pd.read_csv("processes.csv", index_col="Pid")

# cur_time = 0
# num_processes_done = 0

# wait_queue = Queue()
# cur_pid = None


# # Copy and paste tempalte code here
# while num_processes_done < processes.shape[0]:
#     # Check if current process finished
#     if cur_pid is not None:
#         if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
#             # Step 1 code goes here
#             processes.loc[cur_pid, "End"] = cur_time
#             cur_pid = None
#             num_processes_done += 1
#     # Handle arriving processes
#     # Step 2 code goes here
#     ready_processes = processes[processes["Arrival"] == cur_time]
#     for pid, _ in ready_processes.iterrows():
#         wait_queue.enqueue(pid)
#     # Assign a process to the processor
#     if cur_pid is None and len(wait_queue) > 0:
#         # Step 3 code goes here
#         cur_pid = wait_queue.dequeue()
#         processes.loc[cur_pid, "Start"] = cur_time 
#     cur_time += 1

# processes["Wait"] = processes["Start"] - processes["Arrival"]
# average_wait_time = processes["Wait"].mean()



'''9.Calculating Turnaround Times'''
import linked_list
import pandas as pd

class Queue(linked_list.LinkedList):
    def enqueue(self, data):
        self.prepend(data)
    
    def get_front(self):
        return self.tail.data
    
    def dequeue(self):
        ret = self.tail.data
        if self.length == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret

processes = pd.read_csv("processes.csv", index_col="Pid")

cur_time = 0
num_processes_done = 0

wait_queue = Queue()
cur_pid = None


# Copy and paste tempalte code here
while num_processes_done < processes.shape[0]:
    # Check if current process finished
    if cur_pid is not None:
        if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
            # Step 1 code goes here
            processes.loc[cur_pid, "End"] = cur_time
            cur_pid = None
            num_processes_done += 1
    # Handle arriving processes
    # Step 2 code goes here
    ready_processes = processes[processes["Arrival"] == cur_time]
    for pid, _ in ready_processes.iterrows():
        wait_queue.enqueue(pid)
    # Assign a process to the processor
    if cur_pid is None and len(wait_queue) > 0:
        # Step 3 code goes here
        cur_pid = wait_queue.dequeue()
        processes.loc[cur_pid, "Start"] = cur_time 
    cur_time += 1


processes["Turnaround"] = processes["End"] - processes["Arrival"]
average_turnaround_time = processes["Turnaround"].mean()
print(average_turnaround_time)