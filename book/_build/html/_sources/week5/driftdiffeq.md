# Drift Diffusion Equation

Let's consider a drift in the diffusion process. 

```{figure} drift.png
---
height: 200px
name: drift
---
```

Because of the discretization, we can write

$$
P(x,t+\Delta t) = q P(x-L,t) + (1-q) P(x+L,t)
$$

Let's assume that $\Delta t$ and $L$ are very small then we can Taylor expand and determine the diffusion equation with drift

$$
\frac{\del p}{\del t} = -(2q-1)\frac{L}{\Delta t} \frac{\del p}{\del x} + \frac{L^2}{2 \Delta t} \frac{\del^2 p}{\del p^2}
$$

with $D = \frac{L^2}{2 \Delta t}$ and $v=(2q-1)\frac{L}{\Delta t}$, we derive the Fokker-Planck equation:

$$
\frac{\del p}{\del t} = - v \frac{\del p}{\del x} + D \frac{\del^2 p}{\del p^2}
$$

If we assume that the velocity is a result of a constant force applied to a particle with mobility $\gamma$ ($F = v/\gamma$), we can rewrite

$$
\frac{\del p}{\del t} = - \gamma F \frac{\del p}{\del x} + D \frac{\del^2 p}{\del p^2}
$$

### Single particle description

How can we describe the change of the position of a single particle?

$$
x(t + \Delta t) = x(t) + \gamma F \Delta t + l(t)
$$

If we assume a dilute system, we can describe the net motion between collisions as

$$
\frac{1}{2} \frac{F}{m} \Delta t^2 = F \Delta t \frac{\Delta t}{2 m}.
$$

Therefore, we identify

$$
\gamma = \frac{\Delta t}{2 m} = \frac{\Delta t}{2 m} (D \frac{2 \Delta t}{L^2}) = \frac{D}{m(L/\Delta t)^2} = \frac{D}{m \mean{v}^2} 
$$

Important result

$$
\gamma = \frac{D}{m \mean{v}^2}
$$
