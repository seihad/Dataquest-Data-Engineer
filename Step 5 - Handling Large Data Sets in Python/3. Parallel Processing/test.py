import os
file_names = os.listdir("wiki")
for i in range(3):
    print(file_names[i])

num_files = len(file_names)
print(num_files)

folder_name = "wiki"
file_name_first = file_names[0]
with open(os.path.join(folder_name, file_name_first)) as f:
    lines = [line for line in f.readlines()]
print(lines[1])

import math
import functools
from multiprocessing import Pool

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    pool = Pool(num_processes)
    chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

def map_line_count(file_names):
    total = 0
    for fn in file_names:
        with open(os.path.join("wiki", fn)) as f:
            total += len(f.readlines())
    return total
    
def reduce_line_count(count1, count2):
    return count1 + count2

if __name__ == "__main__":

    results = map_reduce(file_names, 8, map_line_count, reduce_line_count)
    print(results)