# Fortran Example: Mathieu functions and characteristics

Video example 10-14-22

> $$\begin{cases} (2q\cos(2x)-\frac{d^2}{dx^2})y = ay \\ y(0) = y(2\pi)\end{cases}$$

- Hamiltonian = $2q\cos(2x)-\frac{d^2}{dx^2}$
  - Kinetic energy KE: $\frac{d^2}{dx^2}$
  - Potential Energy PE: $2q\cos(2x)$

Equivalent to:

> $$ [\bm{V} - \bm{T^{-1}}\bm{D_k}\bm{T}]\bm{y} =a\bm{y} $$
>
> > $$ [\bm{H}]\bm{y} =a\bm{y} $$

- $\bm{V}$ : diagonal matrix
  - entries: $\{\cos(2x_1), \cos(2x_2),...\}$
  - i.e.: $2q\cos(2x)$ on the grid
- $\bm{D_k}$: Diagonal matrix with the square of the wave numbers as entries
  - $\{0,1,1,4,4,9,9,\dots\}$
- $\bm{T, T^{-1}}$:
- $\bm{T^{-1}}\bm{D_k}\bm{T}$: discrete second derivative
  - i.e.: $\frac{d^2}{dx^2}$

## HW Relevance

- See file `diffop.f90`
