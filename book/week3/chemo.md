# Chemomechanical Cycle

```{admonition} You will learn
the concept of chemomechanical cycles.
```
Next, we consider a more accurate descriptions of a molecular motor. A motor uses the free energy from the hydrolysis of ATP

$$
ATP \rightarrow P_i + ADP
$$

to perform a step. The chemical cycle involves the binding of ATP to an empty motor head, the release of $P_i$, and the release of $ADP$. The mechanical cycle consists of a sequence of conformational changes, which result in a step.


```{figure} chem.png
---
height: 170px
name: chem
---
```

It is possible to calculate the waiting time distribution and other quantities such as the thermodynamical efficiency for these chemomechanical cycles. However the real chllange is to connect them to experimental data.

In the following, we consider a very simple cycle with one state.


```{figure} schem.png
---
height: 170px
name: schem
---
```

Next, we want determine the randomness of such a motor.

By renaming the states we can use our result from the poisson stepper

```{figure} rnstates.png
---
height: 170px
name: rnstates
---
```

$$
A_n \approx P_{2n},
$$

here we cannot use an equal sign, because the normalization is not correct. We can calculate ther nurmalization by

$$
\sum_{n=0}^{\infty} P_{2n} = \cosh(k t) e^{-k t}.
$$

The normalized solution is then

$$
A_n = \frac{P_{2 n}}{\cosh(k t) e^{-k t}} = \frac{(k t)^{2j}}{(2j)!\cosh(k t)}
$$

Let's determine the randomness!

$$
x(t) = d n(t)
$$


$$
\mean{x} = d \sum_n n A_n = \frac{d}{2} k t \tanh(kt)
$$

$$
\mean{x^2} = d^2 \sum_n n^2 A_n = \frac{d^2}{4} kt (k t + \tanh(kt)),
$$

with $\tanh(x) = \frac{e^{2x}-1}{e^{2x} + 1}$. Let's consider solutions for $kt \gg 1$, then $\tanh(k t) \approx 1$ and

$$
\mean{x^2} - \mean{x}^2 \approx  \frac{d^2}{4} kt (k t + 1) - (\frac{d}{2} k t)^2 = \frac{1}{4} d^2 k t 
$$

and the randomness:

$$
r = \frac{\mean{x^2} - \mean{x}^2}{d \mean{x}} = \frac{1}{2}
$$

For a one-step poission stepper we have

$$
r = 1,
$$

and for a two-step poisson stepper we have

$$
r = \frac{1}{2}.
$$

It is possible to show that for an m-step poisson stepper we get

$$
r = \frac{1}{m}
$$



```{figure} energy.png
---
height: 90px
name: en
---
```