
import time

start_time = time.time()

for i in range(100000000):
    pass

end_time = time.time()

execution_time = end_time - start_time

print('Execution Time:', execution_time)

