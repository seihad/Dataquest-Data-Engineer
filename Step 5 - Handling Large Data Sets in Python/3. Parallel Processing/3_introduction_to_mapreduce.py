'''1.Introduction'''
# import math

# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# chunks = make_chunks([1,2,3,4,5,6], 3)

# print(chunks)

'''2.The Map Function'''
# import concurrent.futures
# import math

# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# def map_parallel(mapper, data, num_processes):
#     chunks = make_chunks(data, num_processes)
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = [executor.submit(mapper, chunk) for chunk in chunks]
#     return [future.result() for future in futures]

# values = [1, 4, 5, 2, 7, 21,     \
#           31, 41, 3, 40, 5, 14,  \
#           9, 32, 12, 18, 1, 30,  \
#           6, 19, 23, 35, 12, 13, \
#           0, 12, 42, 41, 11, 9]

# # Write code here

# if __name__ == '__main__':
#     results = map_parallel(max, values, 5)
#     print(results)


'''3.Using a Pool'''
# import math
# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# values = [1, 4, 5, 2, 7, 21,     \
#           31, 41, 3, 40, 5, 14,  \
#           9, 32, 12, 18, 1, 30,  \
#           6, 19, 23, 35, 12, 13, \
#           0, 12, 42, 41, 11, 9]

# chunks = make_chunks(values, 6)

# from multiprocessing import Pool

# if __name__ == '__main__':
#     pool = Pool(6)
#     results = pool.map(max, chunks)
#     pool.close()
#     pool.join()
#     print(results)


'''4.Pools with Context Manager'''
# import math
# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# values = [1, 4, 5, 2, 7, 21,     \
#           31, 41, 3, 40, 5, 14,  \
#           9, 32, 12, 18, 1, 30,  \
#           6, 19, 23, 35, 12, 13, \
#           0, 12, 42, 41, 11, 9]

# chunks = make_chunks(values, 6)

# from multiprocessing import Pool

# if __name__ == '__main__':
#     with Pool(6) as pool:
#         results = pool.map(max, chunks)
#     print(results)


'''5.The Reduce Function'''
# values = [1, 4, 5, 2, 7, 21,     \
#           31, 41, 3, 40, 5, 14,  \
#           9, 32, 12, 18, 1, 30,  \
#           6, 19, 23, 35, 12, 13, \
#           0, 12, 42, 41, 11, 9]

# # Write code here
# import functools

# if __name__ == '__main__':
#     max_value = functools.reduce(max, values)
#     print(max_value)


'''6.Putting it Together'''
# import math
# from multiprocessing import Pool
# import functools

# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# data = [1, 4, 5, 2, 7, 21,     \
#         31, 41, 3, 40, 5, 14,  \
#         9, 32, 12, 18, 1, 30,  \
#         6, 19, 23, 35, 12, 13, \
#         0, 12, 42, 41, 11, 9]

# num_processes = 5

# # Write code here

# #split
# chunks = make_chunks(data, num_processes)
# if __name__ == '__main__':
#     #map
#     with Pool(num_processes) as pool:
#         chunk_results = pool.map(max, chunks)

#     #reduce
#     overall_result = functools.reduce(max, chunk_results)
#     print(overall_result)

'''7.The MapReduce Function'''
# import math
# from multiprocessing import Pool
# import functools

# data = [1, 4, 5, 2, 7, 21,     \
#         31, 41, 3, 40, 5, 14,  \
#         9, 32, 12, 18, 1, 30,  \
#         6, 19, 23, 35, 12, 13, \
#         0, 12, 43, 41, 11, 9]

# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# def map_reduce(data, num_processes, mapper, reducer):
#     chunks = make_chunks(data, num_processes)
#     with Pool(num_processes) as pool:
#         chunk_results = pool.map(mapper, chunks)
#     return functools.reduce(reducer, chunk_results)

# # Write code here
# if __name__ == '__main__':
#     max_value = map_reduce(data, 4, max, max)
#     print(max_value)


'''8.Applying MapReduce to Job Postings'''
# import pandas as pd
# import math
# from multiprocessing import Pool
# import functools

# def make_chunks(data, num_chunks):
#     chunk_size = math.ceil(len(data) / num_chunks)
#     return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# def map_reduce(data, num_processes, mapper, reducer):
#     chunks = make_chunks(data, num_processes)
#     with Pool(num_processes) as pool:
#         chunk_results = pool.map(mapper, chunks)
#     return functools.reduce(reducer, chunk_results)

# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# skills = pd.read_csv("Skills.csv")

# # Write code here
# def mapper(skill_chunk):
#     frequency = {}
#     for skill_name in skill_chunk["Name"]:
#         frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
#     return frequency

# def reducer(freq_chunk1, freq_chunk2):
#     merged = {}
#     merged.update(freq_chunk1)
#     merged.update(freq_chunk2)
#     return merged

# if __name__ == '__main__':
#     skill_freq = map_reduce(skills, 4, mapper, reducer)
#     print(skill_freq)

'''9.Applying MapReduce to Job Postings'''
import pandas as pd
import math
from multiprocessing import Pool
import functools

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

job_postings = pd.read_csv("DataEngineer.csv")
job_postings["Job Description"] = job_postings["Job Description"].str.lower()
skills = pd.read_csv("Skills.csv")

# Write code here
def mapper(jobs_chunk):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = jobs_chunk["Job Description"].str.count(skill_name).sum()
    return frequency

def reducer(freq_chunk1, freq_chunk2):
    merged = {}
    for skill in freq_chunk1:
        merged[skill] = freq_chunk1[skill] + freq_chunk2[skill]
    return merged

if __name__ == '__main__':
    skill_freq = map_reduce(job_postings, 4, mapper, reducer)
    print(skill_freq)
