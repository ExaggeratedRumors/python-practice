# 4. Wykorzystując moduł time i funkcję time
# obliczyć ile trwa pętla składająca się z 100000
# iteracji dla listy i dla typu tuple.

import time

size = 10000000

test_array = [0 for i in range(size)]
test_tuple = (0 for j in range(size))

start_time = time.time()
for element in test_array:
    pass
finish_time = time.time()

print("list: ", finish_time - start_time)

start_time = time.time()
for element in test_tuple:
    pass
finish_time = time.time()

print("tuple: ", finish_time - start_time)
