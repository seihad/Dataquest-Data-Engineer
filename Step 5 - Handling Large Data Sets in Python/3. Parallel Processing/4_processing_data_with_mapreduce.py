'''1.Introduction'''
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

# values = [98, 63, 55, 80, 45, 51, 91, 64, 65, 48, 48, 92, 76, 99, 57, 42, 79, 61, 63, 49]

# if __name__ == '__main__':
#     min_value = map_reduce(values, 4, min, min)
#     print(min_value)

'''2.Length of Longest English Word'''
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

# def map_max_length(words_chunk):
#     return max([len(word) for word in words_chunk])


# with open("english_words.txt") as f:
#     words = [word.strip() for word in f.readlines()]

# if __name__ == '__main__':
#     max_len = map_reduce(words, 4, map_max_length, max)
#     print(max_len)


'''3.Longest English Word'''
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



# with open("english_words.txt") as f:
#     words = [word.strip() for word in f.readlines()]

# def map_max_len_str(words_chunk):
#     return max(words_chunk, key=len)

# def reduce_max_len_str(word1, word2):
#     return map_max_len_str([word1, word2])


# if __name__ == '__main__':
#     max_len_str = map_reduce(words, 4, map_max_len_str, reduce_max_len_str)
#     print(max_len_str)



'''4.Searching with MapReduce'''
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


# with open("english_words.txt") as f:
#     words = [word.strip() for word in f.readlines()]

# target = "pneumonoultramicroscopicsilicovolcanoconiosis"

# def map_contains(words_chunk):
#     if target in words_chunk:
#         return True
#     else:
#         return False

# def reduce_contains(contains1, contains2):
#     if contains1 or contains2:
#         return True
#     else:
#         return False
# if __name__ == '__main__':
#     is_contained = map_reduce(words, 4, map_contains, reduce_contains)
#     print(is_contained)


'''5.Counting Character Frequencies'''
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


# with open("english_words.txt") as f:
#     words = [word.strip() for word in f.readlines()]

# def map_char_count(words_chunk):
#     char_freq = {}
#     for word in words_chunk:
#         for c in word:
#             if c not in char_freq:
#                 char_freq[c] = 0
#             char_freq[c] += 1
#     return char_freq


# def reduce_char_count(freq1, freq2):
#     for c in freq2:
#         if c in freq1:
#             freq1[c] += freq2[c]
#         else:
#             freq1[c] = freq2[c]
#     return freq1

# if __name__ == '__main__':
#     char_freq = map_reduce(words, 4, map_char_count, reduce_char_count)
#     print(char_freq)


'''6.Average Word Length'''

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


# with open("english_words.txt") as f:
#     words = [word.strip() for word in f.readlines()]

# def map_average(words_chunk):
#     return sum([len(word) for word in words_chunk]) / len(words)

# def reduce_average(res1, res2):
#     return res1 + res2

# if __name__ == '__main__':
#     average_word_len = map_reduce(words, 4, map_average, reduce_average)
#     print(average_word_len)

'''7.Rare Adjacent Characters'''
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


with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]



def map_adjacent(words_chunk):
    adj_freq = {}
    for word in words_chunk:
        for i in range(len(word) - 1):
            seq = word[i] + word[i + 1]
            if seq not in adj_freq:
                adj_freq[seq] = 0
            adj_freq[seq] += 1
    return adj_freq

def reduce_adjacent(freq1, freq2):
    for seq in freq2:
        if seq in freq1:
            freq1[seq] += freq2[seq]
        else:
            freq1[seq] = freq2[seq]
    return freq1

if __name__ == '__main__':
    pair_freq = map_reduce(words, 4, map_adjacent, reduce_adjacent)
    unique_pairs = [seq for seq in pair_freq if pair_freq[seq] == 1]
    print(unique_pairs)
