import time

start_time = time.time()

print("Task started...")
time.sleep(2)  
print("Task completed after 2 seconds!")

end_time = time.time()

execution_time = end_time - start_time
print(f"The task took {execution_time:.2f} seconds to complete.")
