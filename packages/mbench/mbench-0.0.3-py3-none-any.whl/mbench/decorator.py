# import functools
# import logging
# import time

# import pynvml
# import psutil
# from memory_profiler import memory_usage


# def performance_monitor(enabled=True):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if not enabled:
#                 return func(*args, **kwargs)

#             # Measure start time
#             start_time = time.time()

#             # Measure CPU and memory usage before function call
#             cpu_usage_start = psutil.cpu_percent(interval=None)
#             memory_usage_start = memory_usage(-1, interval=0.1, timeout=None)

#             # Measure GPU usage before function call
#             gpu_usage_start = {gpu.id: gpu.memoryUtil for gpu in GPUtil.getGPUs()}

#             # Measure I/O counters before function call
#             io_counters_start = psutil.disk_io_counters()

#             # Execute the function
#             result = func(*args, **kwargs)

#             # Measure end time
#             end_time = time.time()

#             # Measure CPU and memory usage after function call
#             cpu_usage_end = psutil.cpu_percent(interval=None)
#             memory_usage_end = memory_usage(-1, interval=0.1, timeout=None)

#             # Measure GPU usage after function call
#             gpu_usage_end = {gpu.id: gpu.memoryUtil for gpu in GPUtil.getGPUs()}

#             # Measure I/O counters after function call
#             io_counters_end = psutil.disk_io_counters()

#             # Calculate metrics
#             execution_time = end_time - start_time
#             cpu_usage = cpu_usage_end - cpu_usage_start
#             memory_usage_diff = max(memory_usage_end) - min(memory_usage_start)
#             gpu_usage_diff = {gpu: gpu_usage_end[gpu] - gpu_usage_start[gpu] for gpu in gpu_usage_start}
#             io_usage = {
#                 'read_bytes': io_counters_end.read_bytes - io_counters_start.read_bytes,
#                 'write_bytes': io_counters_end.write_bytes - io_counters_start.write_bytes
#             }

#             # Print report
#             logging.debug(f"Execution time: {execution_time:.4f} seconds")
#             logging.debug(f"CPU usage: {cpu_usage:.2f}%")
#             logging.debug(f"Memory usage: {memory_usage_diff:.2f} MiB")
#             for gpu, usage in gpu_usage_diff.items():
#                 logging.debug(f"GPU {gpu} usage: {usage:.2f}%")
#             logging.debug(f"I/O usage: Read {io_usage['read_bytes']} bytes, Write {io_usage['write_bytes']} bytes")

#             return result
#         return wrapper
#     return decorator



# @performance_monitor(enabled=True)
# def my_function():
#     # Your function implementation here
#     return sum(i * i for i in range(1000))

# def test_my_function(benchmark):
#     result = benchmark(my_function)
#     assert result == sum(i * i for i in range(1000))

# if __name__ == "__main__":
#     my_function()
#     # test_my_function(my_function)