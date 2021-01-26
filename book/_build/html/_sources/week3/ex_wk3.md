Week 3: Exercises
=======================
 
1. Show that the solution 

$$
P_j(t) = \frac{(k t)^j}{j!} e^{-kt}
$$ (eq:solution)

for the poisson stepper is a solution for the following master equation

$$
\frac{d}{dt} P_0 (t) &= - k P_0 (t) \\
\frac{d}{dt} P_j (t) &= k P_{j-1} - k P_{j}  \quad \text{for } j>0\\
$$ (eq:states)

Show that the solution {eq}`eq:solution` is normalized.

2. Use Taylor's theorem to show that

$$
e^{kt} = \sum_{n=0}^{\infty}  \frac{(k t)^{n}}{n!}
$$

3. Derive the variance $\mean{(x-\mean{x})^2}$ for a poisson stepper with step size $d$,

$$
x(t) = d N(t)
$$

4. Consider a two-step Markov process on the following network:
IMAGE$
The process starts in state $(0)$. The distribution of arrival times into the absorbing state $(2)$ is given by 

$$
\frac{d}{dt}P_2(t)$
$$

Show that this distribution of arrival times is not a simple exponential function.