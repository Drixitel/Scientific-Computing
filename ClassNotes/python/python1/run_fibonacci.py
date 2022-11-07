"""
/lectureNote/chapters/chapt03/codes/examples/dictionaries/run_fibonacci.py

Runtime comparison of three fibonacci implementations

"""

import time
from fibonacci import fibonacci
from fibonacci_dict import fibonacci_dict, fibonacci_dict_sparse

id_set = [4,12,15,30,32]

start_time1 = time.time()
for i in id_set:
    fibonacci(i)
elapsed_time1 = time.time() - start_time1

start_time2 = time.time()
for i in id_set:
    fibonacci_dict(i)
elapsed_time2 = time.time() - start_time2

start_time3 = time.time()
for i in id_set:
    fibonacci_dict_sparse(i)
elapsed_time3 = time.time() - start_time3

print('First runs through (sec):')
print( '  fibonacci             = ', elapsed_time1 )
print( '  fibonacci_dict        = ', elapsed_time2 )
print( '  fibonacci_dict_sparse = ', elapsed_time3 )

start_time1 = time.time()
for i in id_set:
    fibonacci(i)
elapsed_time1 = time.time() - start_time1

start_time2 = time.time()
for i in id_set:
    fibonacci_dict(i)
elapsed_time2 = time.time() - start_time2

start_time3 = time.time()
for i in id_set:
    fibonacci_dict_sparse(i)
elapsed_time3 = time.time() - start_time3

print('Second runs through (sec):')
print( '  fibonacci             = ', elapsed_time1 )
print( '  fibonacci_dict        = ', elapsed_time2 )
print( '  fibonacci_dict_sparse = ', elapsed_time3 )

