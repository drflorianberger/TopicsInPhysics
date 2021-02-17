# Diffusion Equation

An alternative derivation of the MSD is by starting with the diffusion equation. 

We assume that a particle takes a $\pm L$ step each time step $\Delta t$.

```{figure} jump.png
---
height: 70px
name: jump
---
```

Let's consider time:

```{figure} plattice.png
---
height: 200px
name: plattice
---
```

Because of the discretization, we can write

$$
P(x,t+\Delta t) = 1/2 P(x-L,t) + 1/2 P(x+L,t)
$$

Let's assume that $\Delta t$ and $L$ are very small then we can Taylor expand to

$$
P + \Delta t \frac{\del P}{\del t} = \frac{1}{2} (P - \Delta L \frac{\del P}{\del x} + \frac{1}{2} L^2 \frac{\del^2 P}{\del x^2}) + \frac{1}{2}(P + L \frac{\del P}{\del x} + \frac{1}{2} L^2 \frac{\del^2 P}{\del x^2})
$$

We determine the diffusion equation

$$
\frac{\del P}{\del t} = \frac{L^2}{2 \Delta t} \frac{\del^2 P}{\del x^2}
$$

With the diffusion coefficient $D = \frac{L^2}{2 \Delta t} $,

$$
\frac{\del P}{\del t} = D \frac{\del^2 P}{\del x^2}
$$

To solve this equation uniquely, we need one initial condition and two boundary conditions: $P(x,0) = \delta(x)$, and $P(+\infty,t) = P(-\infty,t) = 0$.

The solution is the Gaussian distribution:

$$
P(x,t) = \frac{1}{\sqrt{4 \pi D t}}e^{-x^2/4Dt}
$$

we can check that

$$
\int_{-\infty}^{+\infty} P(x,t) dx = 1
$$

$$
\mean{x} = \int_{-\infty}^{+\infty} x P(x,t) dx = 0
$$

$$
\mean{x^2} = \int_{-\infty}^{+\infty} x^2 P(x,t) dx = 2 D t
$$