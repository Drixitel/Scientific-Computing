# Homework 2

- 2-body Problem

## Overview and set-up

- numberically evolve a 2-body problem
- equations of motion:

> $$ m*1 \frac{d^2 \bm{x_1}}{dt^2} = \bm{F*{1,2}} \\ m*2 \frac{d^2 \bm{x_2}}{dt^2} = \bm{F*{2,1}} \\ $$

- Masses: $m_1, m_2$
- position vectors $\bm{x_1, x_2}$
- Force vectors $\bm{F_{1,2}, F_{2,1}}$

  - The forces are equal and opposite by the 3rd law
    > $\bm{F_{1,2}}= -\bm{F_{2,1}}$

- The force involved is the gravitational force

> $$ \bm{F} = G \frac{m_1\cdot m_2}{r^2} $$

- where $ r = ||\bm{x_2 - x_1}|| = \sqrt{\bm{x_2^2 - x_1^2}} = dist$ \
  the displacement

> "Inverse square law"

- We can rewrite this as,

> $$ \bm{F} = \bm{F\_{1,2}} = \frac{G m_1 m_2}{||\bm{x_2 - x_1}||^2} \cdot \frac{(\bm{x_2 -x_1})}{||\bm{x_2 - x_1}||} $$
> $$ = \frac{G m_1 m_2 (\bm{x_2 -x_1})}{||\bm{x_2 - x_1}||^3} $$
>
> > Notice: Force only depends on position! not on momentum.

> $$ F*1 = F*{1,2} \text{ and } F*2 = F*{2,1}\text{ with G=1}$$

> $$ F_1 = \frac{1\cdot m(1)\cdot m(2) \cdot (\bm{x_2 - x_1}) }{dist^3} $$
> $$ F_2 = - \frac{1\cdot m(1)\cdot m(2) \cdot (\bm{x_2 - x_1})}{dist^3} $$

## Simpilfy further

- let $G=1$ which is equivalent to making a change of variables.
- Create a set of first order equations
  - To do this we define the momentum of the $i^{th}$ particle
  - $\bm{p_i}
  - and velocity as the time derivative of the $i^{th}$ positon $\bm{x_i}$

> $$ \bm{p_i} = m_i \frac{d\bm{x_i}}{dt} = m_i\cdot \bm{v_i} $$

## Steps

Since $\bm{p_i}$ is defined this way then,

> $$ \dot{p*i} = \frac{d\bm{p_i}}{dt } = \bm{F*{1,2}} $$

Plugging this into our eqations we get the following 4,

(diving over any constants i.e. mass to isolate the differential)

## Main Equations

---

- These are the equations we will evolve

### Equations for particle 1

> $$ \frac{d\bm{x_2}}{dt} = \frac{\bm{p_2}}{m_2}\\ \frac{d\bm{p_1}}{dt} = \bm{F} \\ $$

### Equations for particle 2

> $$ \frac{d\bm{x_1}}{dt} = \frac{\bm{p_1}}{m_1} \\ \frac{d\bm{p_2}}{dt} = - \bm{F} $$

### Solving

- We will solve these eqations for motion in a plane i.e. 2 dimensions
- this means each vector $\bm{x_i, p_i, F, v_i}$ have 2 components
  - giveing: 2 components with 4 euations of motinon each give 8 eqations total

## Discretizing the problem

---

- We have a contnous problem and must change it into a discrete problem
- We consider descrete time steps denoted as

> $$ t^n = n\Delta t \quad , \text{ for }, n\in \mathbb{N} $$

- $\Delta t$ = time step
- Resources:
  - Verlet integration
  - Velocity Verlet method
  - sympletic integrators
  - Tied to dynamics of Hamiltonian systems

### Zero Total Momentum Case

---

$$
p_{b4} = p_{after}\\
p_1 + p_2 = 0 \\
\implies\\
p_1 = -p_2\\
m_1v_1 = -m_2v_2 \\
$$

Given, $m_1 = 1$ and $m_2 = 0.01$,so

$$
v_1 = -(0.01)v_2
$$

In x-dimension we have, $v_{x1}= 0$ and $v_{x2}= 1$, so we change the value of $$v_1 = -0.1 = -m_2$$ This is correct, but I was silly and didn't keep it as a vector i.e.,

```
    !! From
    mom(:,1,1) = mass(1)*(/0.0_fp,0.0_fp/)

    !! I tried - which isn't the correct dimension
    mom(:,1,1) != mass(1)*( -mass(2) )

    !! but the correct one is this obviously
    ! mom(:,1,1) = mass(1)*(/-0.01_fp,0.0_fp/)

```

### Deliverables for the report

---

Questions to answer:

2. Why can `real(fp)` be used throughtout the files?
   - The module utility holds the declaration of those variables and each other file imports that variable with the `use` command. This allows the processer to first locate the variable in utility an it then sees all instances of it in other files the same as it would if it was declared in that file.
3. Comment on the seperation of duties between `orbits.f90` and `timestep.f90`. Does the distinction make sense?
   - yes the distinciton makes perfect sense when regarding the contents of the files. In the `orbits.f90` file we find initial and end conditions/parameters along with key variable declarations necessary to the two body problem which result in orbits. The file additionally contains the code required to generate the trajectory i.e. the orbit of the two bodies. Whereas, in the `timestep.f90` file we find the actual model of our system which is needed to create a loop program that essentially incriments in discrete time i.e. a time step. The output of `timestep.f90` is then called into `orbits.f90` and exported to a `sol.dat` file.
4. What would you need to do to increase this system to evolve 3 particles? What about N particles?
5. The code evolves the dynamics in the plane. What would you need to do to raise this to dynamics in full 3D space? Would this be easier or harder than increasing the number of particles?
6. Talk about the graphs you made

```
 Present each of the three configurations discussed above. Present the initial conditions that give that solution and comment on what you see.

For the first and third configurations find the total momentum of the system. Comment on how this relates to the trajectories you observe.

If you adjusted the final time and/or number of time steps in the third configuration, be sure to comment on that as well.
```

7. What are the flags in the Makefile? What do they do?
   - FFlAGS:
     - -Wall : gievs warnings for common sources of error
     - -Wextra : gives more than what `-Wall` provides, specifially to subroutine arguements that are not used
     - -ffree-line-length-none : disables line length limit i.e. removes the need to include line continuation where it might be needed
     - -fPIC : no idea but -f would be for Fortran dialect
     - -g : generates extra debugging information for the GDB debugger or the GNU Project Debugger which debugs C, but in this case fortran.
     - -fcheck=all : slows the program but adds a check to note if array indicies are within thier bounds each time they are accessed. Basically a check to maintin arrays used.
     - -fbacktrace : tells if the program crashes and produces a back trace if possible showing which functions or subroutines may be calling the error.
8. Write a conclusion
