Week 3: Exercises
=======================

3.1) **1 Point:** Use Taylor's theorem to show that

$$
e^{kt} = \sum_{n=0}^{\infty}  \frac{(k t)^{n}}{n!}
$$ (eq:exp)

<br />
<br />

3.2) **2 Points:** Show that the solution 

$$
P_j(t) = \frac{(k t)^j}{j!} e^{-kt}
$$ (eq:solution)

for the Poisson stepper is a solution for the following master equation

$$
\frac{d}{dt} P_0 (t) &= - k P_0 (t) \\
\frac{d}{dt} P_j (t) &= k P_{j-1} - k P_{j}  \quad \text{for } j>0\\
$$ (eq:states)

Show that the solution {eq}`eq:solution` is normalized, i.e. $\sum_j P_j(t) = 1$ (Hint use equation {eq}`eq:exp`)
<br />
<br />


3.3) **2 Points** Derive the variance $\mean{(x-\mean{x})^2}$ for a poisson stepper with step size $d$,

$$
x(t) = d N(t)
$$


(Hint: most of the calculation and the tricks have been introduced in equations {eq}`eq:trick` and {eq}`eq:step`)  

<br />
<br />

3.4) Consider a Markov process on the following network:

```{figure} ex1.png
---
height: 70px
name: 2ss
---
```

The process starts in state $(0)$. The distribution of arrival times into the absorbing state $(2)$ is given by 

$$
\frac{d}{dt}P_2(t)
$$

Show that this distribution of arrival times is not a simple exponential function.