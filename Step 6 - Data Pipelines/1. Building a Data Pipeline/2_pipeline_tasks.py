'''2.Generators in Python'''
# def squares(N):
#     i = 0
#     while True:
#         if i >= N:
#             return
#         yield i * i
#         i+= 1

# squared_values = [i for i in squares(20)]

# print(squared_values)


'''3.Generator Comprehension'''
# squared_list = [i * i for i in range(20)]
# squared_gen = (i * i for i in range(20))
# num_to_square = {}
# for idx, i in enumerate(squared_list):
#     num_to_square[idx] = i
# print(num_to_square)

# for i in squared_list:
#     print(i)

# for i in squared_gen:
#     print(i)

'''4.Manipulating Generators in Tasks'''
# log = open('example_log.txt')

# def parse_log(log):
#     for line in log:
#         split_line = line.split()
#         remote_addr = split_line[0]
#         time_local = split_line[3] + " " + split_line[4]
#         request_type = split_line[5]
#         request_path = split_line[6]
#         status = split_line[8]
#         body_bytes_sent = split_line[9]
#         http_referrer = split_line[10]
#         http_user_agent = " ".join(split_line[11:])
#         yield(
#             remote_addr, time_local, request_type, request_path, status, body_bytes_sent, http_referrer, http_user_agent
#         )

# first_line = next(parse_log(log))
# print(first_line)



'''5.Data Cleaning in Parse Log'''
# from datetime import datetime

# log = open('example_log.txt')

# def parse_time(time_str):
#     """
#     Parses time in the format [30/Nov/2017:11:59:54 +0000]
#     to a datetime object.
#     """
#     time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
#     return time_obj

# def strip_quotes(s):
#     return s.replace('"', '')

# def parse_log(log):
#     for line in log:
#         split_line = line.split()
#         remote_addr = split_line[0]
#         time_local = parse_time(split_line[3] + " " + split_line[4])
#         request_type = strip_quotes(split_line[5])
#         request_path = split_line[6]
#         status = int(split_line[8])
#         body_bytes_sent = int(split_line[9])
#         http_referrer = strip_quotes(split_line[10])
#         http_user_agent = strip_quotes(" ".join(split_line[11:]))
#         yield (
#             remote_addr, time_local, request_type, request_path,
#             status, body_bytes_sent, http_referrer, http_user_agent
#         )

# first_line = next(parse_log(log))
# print(first_line)

'''6.Write to CSV'''
# from datetime import datetime
# import csv


# log = open('example_log.txt')

# def parse_time(time_str):
#     """
#     Parses time in the format [30/Nov/2017:11:59:54 +0000]
#     to a datetime object.
#     """
#     time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
#     return time_obj

# def strip_quotes(s):
#     return s.replace('"', '')

# def parse_log(log):
#     for line in log:
#         split_line = line.split()
#         remote_addr = split_line[0]
#         time_local = parse_time(split_line[3] + " " + split_line[4])
#         request_type = strip_quotes(split_line[5])
#         request_path = split_line[6]
#         status = int(split_line[8])
#         body_bytes_sent = int(split_line[9])
#         http_referrer = strip_quotes(split_line[10])
#         http_user_agent = strip_quotes(" ".join(split_line[11:]))
#         yield (
#             remote_addr, time_local, request_type, request_path,
#             status, body_bytes_sent, http_referrer, http_user_agent
#         )

# first_line = next(parse_log(log))
# parsed = parse_log(log)

# def build_csv(lines, file, header=None):
#     if header:
#         lines = [header] + [l for l in lines]
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(lines)
#     file.seek(0)
#     return file

# file = open('temporary.csv', 'r+')

# csv_file = build_csv(parsed, file, header=[
#     'ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent'
# ] )

# contents = csv_file.readlines()
# print(contents[:5])

'''7.Chaining Iterators'''
# from datetime import datetime
# import csv
# import itertools


# log = open('example_log.txt')

# def parse_time(time_str):
#     """
#     Parses time in the format [30/Nov/2017:11:59:54 +0000]
#     to a datetime object.
#     """
#     time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
#     return time_obj

# def strip_quotes(s):
#     return s.replace('"', '')

# def parse_log(log):
#     for line in log:
#         split_line = line.split()
#         remote_addr = split_line[0]
#         time_local = parse_time(split_line[3] + " " + split_line[4])
#         request_type = strip_quotes(split_line[5])
#         request_path = split_line[6]
#         status = int(split_line[8])
#         body_bytes_sent = int(split_line[9])
#         http_referrer = strip_quotes(split_line[10])
#         http_user_agent = strip_quotes(" ".join(split_line[11:]))
#         yield (
#             remote_addr, time_local, request_type, request_path,
#             status, body_bytes_sent, http_referrer, http_user_agent
#         )

# first_line = next(parse_log(log))
# parsed = parse_log(log)

# def build_csv(lines, file, header=None):
#     if header:
#         lines = itertools.chain([header], lines)
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(lines)
#     file.seek(0)
#     return file

# file = open('temporary.csv', 'r+')

# csv_file = build_csv(parsed, file, header=[
#     'ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent'
# ] )

# contents = csv_file.readlines()
# print(contents[:5])

'''8.Counting Unique Request Types'''
# from datetime import datetime
# import csv
# import itertools


# log = open('example_log.txt')

# def parse_time(time_str):
#     """
#     Parses time in the format [30/Nov/2017:11:59:54 +0000]
#     to a datetime object.
#     """
#     time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
#     return time_obj

# def strip_quotes(s):
#     return s.replace('"', '')

# def parse_log(log):
#     for line in log:
#         split_line = line.split()
#         remote_addr = split_line[0]
#         time_local = parse_time(split_line[3] + " " + split_line[4])
#         request_type = strip_quotes(split_line[5])
#         request_path = split_line[6]
#         status = int(split_line[8])
#         body_bytes_sent = int(split_line[9])
#         http_referrer = strip_quotes(split_line[10])
#         http_user_agent = strip_quotes(" ".join(split_line[11:]))
#         yield (
#             remote_addr, time_local, request_type, request_path,
#             status, body_bytes_sent, http_referrer, http_user_agent
#         )

# first_line = next(parse_log(log))
# parsed = parse_log(log)

# def build_csv(lines, file, header=None):
#     if header:
#         lines = itertools.chain([header], lines)
#     writer = csv.writer(file, delimiter=',')
#     writer.writerows(lines)
#     file.seek(0)
#     return file

# file = open('temporary.csv', 'r+')

# csv_file = build_csv(parsed, file, header=[
#     'ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent'
# ] )

# def count_unique_request(csv_file):
#     reader = csv.reader(csv_file)
#     header = next(reader)
#     idx = header.index('request_type')
#     uniques = {}
#     for line in reader:
#         if not uniques.get(line[idx]):
#             uniques[line[idx]] = 0
#         uniques[line[idx]] += 1
#     return uniques

# uniques = count_unique_request(csv_file)
# print(uniques)


'''9.Task Reusability'''
from datetime import datetime
import csv
import itertools


log = open('example_log.txt')

def parse_time(time_str):
    """
    Parses time in the format [30/Nov/2017:11:59:54 +0000]
    to a datetime object.
    """
    time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
    return time_obj

def strip_quotes(s):
    return s.replace('"', '')

def parse_log(log):
    for line in log:
        split_line = line.split()
        remote_addr = split_line[0]
        time_local = parse_time(split_line[3] + " " + split_line[4])
        request_type = strip_quotes(split_line[5])
        request_path = split_line[6]
        status = int(split_line[8])
        body_bytes_sent = int(split_line[9])
        http_referrer = strip_quotes(split_line[10])
        http_user_agent = strip_quotes(" ".join(split_line[11:]))
        yield (
            remote_addr, time_local, request_type, request_path,
            status, body_bytes_sent, http_referrer, http_user_agent
        )

first_line = next(parse_log(log))
parsed = parse_log(log)

def build_csv(lines, file, header=None):
    if header:
        lines = itertools.chain([header], lines)
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)
    file.seek(0)
    return file

file = open('temporary.csv', 'r+')

csv_file = build_csv(parsed, file, header=[
    'ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent'
] )

def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index('request_type')
    uniques = {}
    for line in reader:
        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return ((k,v) for k,v in uniques.items())

uniques = count_unique_request(csv_file)
print(uniques)
summarized_file = open('summarized.csv', 'r+')
summarized_csv = build_csv(uniques, summarized_file, header=['request_type', 'count'])
print(summarized_file.readlines())