# File: sweEigs.py
# Author: Ian May
# Purpose: Symbolically compute flux Jacobian for 2D shallow
#          water equations and look at eigendecomposition

import sympy as sym

# Shallow water equations depend on:
# h: height, strictly positive
# hu: x-direction momentum
# hv: y-direction momentum
# g: gravitational acc. (constant, positive)
def sweVars():
    h = sym.Symbol("h", positive=True)
    hu = sym.Symbol("hu")
    hv = sym.Symbol("hv")
    g = sym.Symbol("g", positive=True)
    return h, hu, hv, g


# Flux of conserved quantities in x-direction
def fluxX(h, hu, hv, g):
    return sym.Matrix([hu, hu**2 / h + g * h**2 / 2, hu * hv / h])


# Flux of conserved quantities in y-direction
def fluxY(h, hu, hv, g):
    return sym.Matrix([hv, hu * hv / h, hv**2 / h + g * h**2 / 2])


# Jacobian of x-flux wrt. conserved variables
def fluxJacX(h, hu, hv, g):
    return fluxX(h, hu, hv, g).jacobian([h, hu, hv])


# x-direction wavespeeds are e-vals of flux Jacobian
def wavespeedX(h, hu, hv, g):
    return tuple(fluxJacX(h, hu, hv, g).eigenvals().keys())


# Final results can be simplified by using primitive variables
def relations(h, hu, hv, g):
    u = sym.Symbol("u")
    v = sym.Symbol("v")
    rels = {hu / h: u, hv / h: v}
    return rels


if __name__ == "__main__":
    # Setup SWE variables as symbols
    h, hu, hv, g = sweVars()
    # Get wavespeeds as e-vals of flux Jacobian
    wvX = wavespeedX(h, hu, hv, g)
    # Get dictionary of conservative -> primitive vars
    rels = relations(h, hu, hv, g)
    # Try to simplify wavespeeds
    print("Found x-direction wavespeeds as:")
    for w in wvX:
        print(w.subs(rels))

    dfdu = fluxJacX(h, hu, hv, g)
    # print(dfdu)
    ev = dfdu.eigenvects()
    print("\nEigen value 1: ")
    print(ev[0][0])
    print("Multiplicity: ")
    print(ev[0][1])
    print("Eigen vector 1: ")
    print(ev[0][2])
    print("\nEigen value 2: ")
    print(ev[1][0])
    print("Multiplicity: ")
    print(ev[1][1])
    print("Eigen vector 2: ")
    print(ev[1][2])
    print("\nEigen value 3: ")
    print(ev[2][0])
    print("Multiplicity: ")
    print(ev[2][1])
    print("Eigen vector 3: ")
    print(ev[2][2])
