# Drift Diffusion Equation

Let's consider a drift in the diffusion process. 

IMAGE 2D lattice

Because of the discretization, we can write

$$
P(x,t+\Delta t) = q P(x-L,t) + (1-q) P(x+L,t)
$$

Let's assume that $\Delta t$ and $L$ are very small, than we can Taylor expand and determine the diffusion equation with drift

$$
\frac{\del p}{\del t} = -(2q-1)\frac{L}{\Delta t} \frac{\del p}{\del x} + \frac{L^2}{2 \Delta t} \frac{\del^2 p}{\del p^2}
$$

with $D = \frac{L^2}{2 \Delta t}$ and $v=(2q-1)\frac{L}{\Delta t}$, derive the Fokker-Planck equation:

$$
\frac{\del p}{\del t} = - v \frac{\del p}{\del x} + D \frac{\del^2 p}{\del p^2}
$$
