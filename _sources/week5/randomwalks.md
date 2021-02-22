# Random Walks

Random walks are emergent behavior of paths that take successive steps in random directions. The precise nature of the microscopic stepping dynamics is not relevant and random walks can be used to describe a large class of different systems.

### Random unit stepper

Consider a stepper that steps with equal probability into the plus direction and into the minus direction, such that the step $l = \pm 1$.

What is the sum of steps after $N$ steps?

$$
s_N = \sum_{i=1}^N l_i
$$

For $N>1$, we expect $s_N = 0$ and on average $\mean{s_N} = 0$. Thus, the average is not a good characteristic measure. Therefore, we will consider the mean squared distance

$$
\mean{s_N^2}
$$

How does the MSD scale with $N$? (Think about flipping a coin. After each coin flip, you add $\pm 1$.)

```{figure} tree.png
---
height: 200px
name: tree
---
```


$$
\mean{s_1^2} &= \frac{1}{2}(-1)^2 + \frac{1}{2} (1)^2 = 1\\
\mean{s_2^2} &= \frac{1}{4}(-2)^2 + \frac{1}{2} (0)^2 + \frac{1}{4} (2)^2 = 2\\
\mean{s_3^2} &= \frac{1}{8}(-3)^2 + \frac{3}{8} (-1)^2 + \frac{3}{8} (1)^2 + \frac{1}{8} (3)^3 = 3
$$

So there is a pattern here and we suspect that $\mean{s_N^2} = N$

Let's consider an iterative approach

$$
\mean{s_N^2} = \mean{(s_{N-1} + l_N)^2} = \mean{s^2_{N-1}} + 2\mean{s_{N-1} l_N} + \mean{l^2_N}
$$

Because $l_N$ is independent of $s_{N-1}$ and equally likely to be $\pm 1$, we have

$$
\mean{s_{N-1} l_N} = 1/2 s_{N-1}(+1) + 1/2 s_{N-1}(-1) = 0
$$

and

$$
\mean{s_N^2} = \mean{s_{N-1}^2} + 1
$$

If we now assume that $\mean{s_{N-1}^2} = N-1$, we have shown that $\mean{s_N^2} = N$. The formal proof will be done as an exersice.

With the step size $L$ we get (check the units):

$$
\sigma_s^2 = \mean{s^2_N} = L^2 N
$$

If we introduce the total time $t$ and the stepping rate $1/\Delta t$, we can rewrite this equation to

$$
\mean{s^2} = \frac{L^2}{\Delta t} t
$$

Defining a diffusion coeficient $D = \frac{L^2}{2 \Delta t}$, we arrive at the mean squared displacement

$$
\mean{s^2} = 2 D t
$$

```{figure} msd.png
---
height: 200px
name: msd
---
```