with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(increment, value) for value in values]

results = [future.result() for future in futures]
print(results)
