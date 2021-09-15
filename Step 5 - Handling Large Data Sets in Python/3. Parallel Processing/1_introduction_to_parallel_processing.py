'''1.Introduction'''
# import multiprocessing


'''2.Creating a Process'''
# import multiprocessing
# import time
# def wait():
#     time.sleep(0.5)
#     print("Done waiting")

# if __name__ == "__main__":
#     process = multiprocessing.Process(target=wait)
#     process.start()
#     print('Finished')
#     process.join()

'''3.Parallel Execution'''
# import multiprocessing
# import time
# def wait():
#     time.sleep(0.5)
#     print("Done waiting")

# if __name__ == "__main__":
#     process = multiprocessing.Process(target=wait)
#     process.start()
#     process.join()
#     print("Finished")


'''4.Running Two Processes'''
# from multiprocessing import process
# import time
# def wait():
#     time.sleep(0.5)
#     print("Done waiting")

# if __name__ == "__main__":
#     start = time.time()
#     p1 = multiprocessing.Process(target=wait)
#     p2 = multiprocessing.Process(target=wait)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     elapsed = end - start
#     print(elapsed)


'''5.Running Multiple Processes'''
# from multiprocessing import process
# import time

# def wait():
#     time.sleep(0.5)
#     print("Done waiting")

# if __name__ == "__main__":
#     start = time.time()
#     processes = [multiprocessing.Process(target=wait) for _ in range(6)]

#     for p in processes:
#         p.start()

#     for p in processes:
#         p.join()

#     end = time.time()
#     elapsed = end - start

#     print(elapsed)

'''6.Process Function Arguments'''
# import multiprocessing


# def sum3(x, y, z):
#     print(x + y + z)

# def list_average(values):
#     print(sum(values) / len(values))

# # Add code below
# if __name__ == "__main__":
#     sum3_process = multiprocessing.Process(target=sum3, args=[3,2,5])
#     list_average_process = multiprocessing.Process(target=list_average, args=[[1,2,3,4,5]])
#     sum3_process.start()
#     list_average_process.start()
#     sum3_process.join()
#     list_average_process.join()

'''7.Sharing Memory'''
# import multiprocessing


# def sum3(x, y, z, shared_value):
#     shared_value.value = x + y + z

# # Add code below
# if __name__ == "__main__":
#     float_value = multiprocessing.Value("f")
#     process = multiprocessing.Process(target=sum3, args=[5,7,4, float_value])
#     process.start()
#     process.join()
#     print(float_value.value)



'''8.Sharing Memory Caveats'''
# import multiprocessing

# def sum_values(first, last, shared_value):
#     for i in range(first, last):
#         shared_value.value += i

# def sum_with_two_processes():
#     N = 10000

#     shared_value = multiprocessing.Value("i")
#     process1 = multiprocessing.Process(target=sum_values, args=(1, N // 2, shared_value))
#     process2 = multiprocessing.Process(target=sum_values, args=(N // 2, N, shared_value))

#     process1.start()
#     process2.start()

#     process1.join()
#     process2.join()
#     return shared_value.value

# # Add code below
# if __name__ == "__main__":
#     results = []
#     for i in range(10):
#         results.append(sum_with_two_processes())
#     print(results)

'''9.Using a Lock'''
import multiprocessing
import time

def sum_values(first, last, shared_value):
    for i in range(first, last):
        with shared_value.get_lock():
            shared_value.value += i

def measure_runtime(function_to_measure):
    N = 10000
    shared_value = multiprocessing.Value("i")
    process1 = multiprocessing.Process(target=function_to_measure, args=(1, N // 2, shared_value))
    process2 = multiprocessing.Process(target=function_to_measure, args=(N // 2, N, shared_value))
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    return end - start
    
# Add code below
def sum_values_improved(first, last, shared_value):
    value_sum = 0
    for i in range(first, last):
        value_sum += i
    with shared_value.get_lock():
        shared_value.value += value_sum

if __name__ == "__main__":
    time_sum_values = measure_runtime(sum_values)
    time_sum_values_improved = measure_runtime(sum_values_improved)
    print(time_sum_values, time_sum_values_improved)
