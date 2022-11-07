"""
/lectureNote/chapters/chapt03/codes/examples/dictionaries/fibonacci_dict.py

Fibonacci sequence using a dictionary "known" which keeps track of values that
have already been computed and stores them for reuse.

"""

from fibonacci import fibonacci

# initialize a dictionary, with the first two Fib. numbers
known = {0:0,1:1}

# Memoized call using full dictionary
def fibonacci_dict(n):
    if n in known:
        # n has been encoutered before, return it
        # base case slides up the series as more terms are queried
        return known[n]
    else:
        # otherwise, call back recursively and cache value
        known[n] = fibonacci_dict(n-1) + fibonacci_dict(n-2)
        return known[n]

# Initialize empty dictionary
sparse = {}
    
def fibonacci_dict_sparse(n):
    if n in sparse:
        # n has been queried before, return value
        return sparse[n]
    else:
        # otherwise, call naive method and cache
        sparse[n] = fibonacci(n)
        return sparse[n]
    
if __name__ == "__main__":
    print(fibonacci_dict(12))
    print(known)
    print(fibonacci_dict_sparse(12))
    print(sparse)
