import multiprocessing
import os

def parallel_file_operation(operation, file_list, num_processes=None):
    if num_processes is None:
        num_processes = os.cpu_count()
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(operation, file_list)
    
    return results
