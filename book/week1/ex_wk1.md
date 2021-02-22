Week 1: Exercises
=======================


1.1) **1 Point:** Calculate the integral

$$
\int_{-\infty}^{+\infty} e^{-x^2} dx
$$
<br />
<br />

1.2) **1 Point:** Show that the probability density function

$$
p(x) = \frac{1}{s \sqrt{\pi}} e^{(x-m)^2/s^2}    
$$ (eq:gpdf)

is normalized. 
<br />
<br />

1.3) **1 Point:** Determine the mean value $\mean{x}$ and the variance $\sigma^2(x)$ of a random variable that is distributed according to the probability density function given in equation {eq}`eq:gpdf` 
<br />
<br />

1.4) **2 Points:** Suppose you have two identical dice with 6-faces with numbers 1 to 6. Tossing the dice together, what is the combined mean value and the combined variance? Can you guess a rule for the mean and the variance of a system of independent events?
<br />
<br />
1.5) Write down the master equation for the following diagram:

```{figure} ex1.png
---
height: 70px
name: 2s
---
```
<br />
<br />
1.6) Solve the master equation from 1.5 with the initial condition $P_0(0) = 1$
<br />
<br />
1.7) You are waiting for the bus. The average waiting time is $\tau = 5$ minutes and the waiting times are distributed according to an exponential distribution with the density

$$
p(t) = \frac{1}{\tau} e^{-t/\tau}
$$

What is the probability of waiting longer than 10 minutes? If you have already waited for 5 minutes, what is the probability of waiting longer than another 10 minutes? (Difficult question! here, you should consider normalizing the probability again. Think about constructing a histogram). Does the result make sense? The exponential function is memoryless.
