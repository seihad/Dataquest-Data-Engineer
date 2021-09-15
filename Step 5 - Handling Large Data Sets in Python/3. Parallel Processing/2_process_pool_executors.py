'''1.Introduction'''
# import pandas as pd
# job_postings = pd.read_csv("DataEngineer.csv")
# num_rows = job_postings.shape[0]
# num_cols = job_postings.shape[1]

'''2.Counting Word Occurrences'''
# import pandas as pd
# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# frequency = {}
# frequency["postgres"] = job_postings["Job Description"].str.count("postgres").sum()
# frequency["sql"] = job_postings["Job Description"].str.count("sql").sum()
# print(frequency)

'''3.Counting All Skills'''
# import pandas as pd
# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# skills = pd.read_csv("Skills.csv")
# frequency = {}
# for skill_name in skills["Name"]:
#     frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
# print(frequency["programming"])

'''4.Functionize the Code'''
# import time
# import pandas as pd

# def count_skills(job_postings, skills):
#     frequency = {}
#     for skill_name in skills["Name"]:
#         frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
#     return frequency

# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# skills = pd.read_csv("Skills.csv")

# start = time.time()
# count_skills(job_postings, skills)
# end = time.time()
# runtime = end - start
# print(runtime)

'''5.Splitting a DataFrame into Chunks'''
# import pandas as pd
# import math

# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# skills = pd.read_csv("Skills.csv")

# def make_chunks(df, num_chunks):
#     num_rows = df.shape[0]
#     chunk_size = math.ceil(num_rows / num_chunks)
#     chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
#     return chunks

# skill_chunks = make_chunks(skills, 8)
# print(skill_chunks)


'''6.Process Pool Executor'''
# import concurrent.futures

# def increment(value):
#     return value + 1

# values = [1, 2, 3, 4, 5, 6, 7, 8]

# # Add code here
# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = [executor.submit(increment, value) for value in values]

#     results = [future.result() for future in futures]
#     print(results)

'''7.Multiprocessing Job Posting Analysis'''
# import pandas as pd
# import concurrent.futures
# import math

# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# skills = pd.read_csv("Skills.csv")


# def make_chunks(df, num_chunks):
#     num_rows = df.shape[0]
#     chunk_size = math.ceil(num_rows / num_chunks)
#     chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
#     return chunks

# def count_skills(job_postings, skills):
#     frequency = {}
#     for skill_name in skills["Name"]:
#         frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
#     return frequency



# if __name__ == '__main__':
#     skill_chunks = make_chunks(skills, 8)
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    
#     results = [future.result() for future in futures]
#     print(results[0])

'''8.Merging Results'''
# import pandas as pd
# import concurrent.futures
# import math

# job_postings = pd.read_csv("DataEngineer.csv")
# job_postings["Job Description"] = job_postings["Job Description"].str.lower()
# skills = pd.read_csv("Skills.csv")


# def make_chunks(df, num_chunks):
#     num_rows = df.shape[0]
#     chunk_size = math.ceil(num_rows / num_chunks)
#     chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
#     return chunks

# def count_skills(job_postings, skills):
#     frequency = {}
#     for skill_name in skills["Name"]:
#         frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
#     return frequency



# if __name__ == '__main__':
#     skill_chunks = make_chunks(skills, 8)
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    
#     results = [future.result() for future in futures]

#     merged_results = {}
#     for result in results:
#         merged_results.update(result)
    
#     print(merged_results)



'''9.Performance Improvement'''
import pandas as pd
import concurrent.futures
import math
import time

job_postings = pd.read_csv("DataEngineer.csv")
job_postings["Job Description"] = job_postings["Job Description"].str.lower()
skills = pd.read_csv("Skills.csv")


def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
    return chunks

def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

def count_skills_parallel(job_postings, skills, num_processes=4):
    # Calculate results using paralleld processing
    skill_chunks = make_chunks(skills, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    results = [future.result() for future in futures]
    # Merge results
    merged_results = {}
    for result in results:
        merged_results.update(result)
    return merged_results



if __name__ == '__main__':
    start = time.time()
    count_skills(job_postings, skills)
    end = time.time()
    time_normal = end - start
    
    start = time.time()
    count_skills_parallel(job_postings, skills)
    end = time.time()
    time_parallel = end - start 

    print(time_normal / time_parallel)

