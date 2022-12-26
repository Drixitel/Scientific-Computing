import numpy as np 

x = 1.0 
y = 2.0 

#exponents and logarithms 
print(np.exp(x))
print(np.log(x))
print(np.log(x))
print(np.log10(x))
print(np.log2(x))


print(np.fabs(x))
print(np.fmin(x,y))
print(np.fmax(x,y))
print(np.fmax(x,y))

n = 100
z = np.arange(n,dtype=float)
z *= 2.0*np.pi/float(n-1)
sin_z = np.sin(z)

print(np.interp(0.75,z,sin_z))
print(np.sin(0.75))