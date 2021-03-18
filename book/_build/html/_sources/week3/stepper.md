# Stochastic Stepper


We assume that a molecular motor steps along its tracks with a fixed step size $d$. However, between the consecutive steps the motor has to wait for an ATP molecule to bind, inducing a complex process of hydrolysis and molecular rearrangements. Therefore the time between the steps is a stochastic quantity. As a first approximation, we assume that this waiting time is exponentially distributed with rate $k$ and the motor can only step forward. Our first question is: how many steps did the motor perform in a given time $t$. Because this number is different from realization to realization, we have to reformulate the question and ask:

What is the probability $P_N(t)$ that the motor performed $N$ steps during the time $t$?

```{figure} stepstate.png
---
height: 70px
name: stepstates
---
```

This state diagram has the following master equation

$$
\frac{d}{dt} P_0 (t) &= - k P_0 (t) \\
\frac{d}{dt} P_j (t) &= k P_{j-1} - k P_{j}  \quad \text{for } j>0\\
$$ (eq:states)

This set of equations is solved by the Poisson distribution (exercise):

$$
P_j(t) = \frac{(k t)^j}{j!} e^{-kt}
$$

This model is often called 'Poisson stepper'. 

We can write the position as a function of time as:

$$
x(t) = d N(t),
$$

in which $d$ is the step size, $N(t)$ the numbers of steps after time.

```{figure} meanx.png
---
height: 170px
name: meanx
---
```

What is the mean position of such a stepper?

$$
\mean{x(t)} = \mean{d N(t)} = d \mean{N(t)}
$$

$$
d \mean{N(t)} &= d \sum_{j=0}^{\infty} j P_j(t) = d \sum_{j=0}^{\infty} j \frac{(k t)^j}{j!} e^{-kt}
= d(0 + \sum_{j=1}^{\infty} j \frac{(k t)^j}{j!} e^{-kt})\\ &= d kt \sum_{j=1}^{\infty}  \frac{(k t)^{j-1}}{(j-1)!} e^{-kt}
\underset{n:= j-1}{=} d kt \underbrace{\sum_{n=0}^{\infty}  \frac{(k t)^{n}}{n!}}_{e^{kt}} e^{-kt} = dkt
$$ (eq:trick)

The variance of the position can be calculated (exersice):

$$
\mean{(x-\mean{x})^2} = \mean{d^2 N^2} - \mean{d N}^2 = d^2 \underbrace{\mean{N^2}}_{kt + (kt)^2} - (dkt)^2 = d^2 kt
$$ (eq:step)

Now we can make a very strong prediction from the model about the so-called randomness.

