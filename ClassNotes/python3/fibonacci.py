"""
/lectureNote/chapters/chapt03/codes/examples/dictionaries/fibonacci.py

Fibonaci sequence using recursion

"""

def fibonacci(n):
    if n == 0:
        # First base case
        return 0
    elif n == 1:
        # Second base case
        return 1
    else:
        # Otherwise, call backwards in sequence recursively
        res = fibonacci(n-1) + fibonacci(n-2)
        return res
    
if __name__ == "__main__":
    fib_numb = fibonacci(12)
