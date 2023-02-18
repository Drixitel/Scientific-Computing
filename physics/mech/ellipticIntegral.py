#%%
from scipy import integrate
import math

# Complete elliptic integral of the first kind
# Note: for a square root use math.sqrt(x); for a square, multiply by itself, or use math.pow(x,2)
#       Use +, -, *, / for addition, subtraction, multiplication, and division
#  *** replace everything in these parentheses by the expression for the integrand of K(u) in terms of u and k ***
def K(k):
    f = lambda x, k: (1 / (math.sqrt((1 - x * x) * (1 - k * k * x * x))))
    y, err = integrate.quad(f, 0, 1, args=(k))
    return y, err


# To use this to find the period of a simple pendulum, the value of k should be the sine of half the amplitude
print("Evaluation of K(k), the complete elliptic integral of the first kind.")
print("Enter a value for k")
k = float(input())
r, e = K(k)
print("K(", k, ") = ", r, " +- ", e)

# Asymptotic approximation to the complete elliptic integral of the first kind
def Ka(k):
    a = (
        math.pi / 2.0
        + math.pi * k * k / 8.0 / (1.0 - k * k)
        - math.pi * k * k * k * k / 16.0 / (1.0 - k * k)
    )
    return a


print("An asymptotic approximation to K(k) is ", Ka(k))
# %%
