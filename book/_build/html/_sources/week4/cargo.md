# Cargo Transport by Multiple Motors

### Cargo Transport by Two Motors

Consider the case of a cargo transported by two motors

```{figure} cargo2mot.png
---
height: 100px
name: cargo2
---
```

We can formalize this behavior by assigning discrete states

```{figure} cargo2motstates.png
---
height: 170px
name: cargo2state
---
```

Next, we introduce rates between these states


```{figure} cargo2motstatesRates.png
---
height: 170px
name: cargo2staterates
---
```

How are these rates related to the single motor rates? For simplicity, we assume a load-free case, $F=0$. Because the motors are independent and identical, the rates add up. The effective rate for two unbound motors to bind is

$$
\pi_{0} = 2\pi,
$$ (eq:r1)

and the rate for two bound motors to unbind is

$$
\e_{2} = 2\e.
$$ (eq:r2)

The master equation reads:

$$
\frac{d}{dt} P_0 &= -\pi_0 P_0 + \e_1 P_1\\ 
\frac{d}{dt} P_1 &= \pi_0 P_0 -(\e_1 + \pi_1) P_1 + \e_2 P_2\\
\frac{d}{dt} P_2 &= \pi_1 P_1 - \e_2 P_2
$$

With the normalization $P_0 + P_1 + P_2 = 1$, we can solve for the steady state:

$$
P_0 &= \frac{ \e_1 \e_2 }{A}\\
P_1 &= \frac{\pi_0 \e_2}{A}\\
P_2 &= \frac{\pi_0 \pi_1}{A}
$$

with $A = \e_1 \e_2 + \pi_0 \e_2 + \pi_0 \pi_1 $

Using the definitions of the single-motor rates from equation {eq}`eq:r1` and {eq}`eq:r1`, we derive:

$$
P_0 &= \frac{\e^2}{a}\\
P_1 &= \frac{2 \e \pi}{a}\\
P_2 &= \frac{\pi^2}{a}\\
$$

with $a = (\e + \pi)^2 $

Does this make sense?

What is the run length of a cargo transported by two motors? If the cargo is transported with velocity $v$, we only need to determine the average time $\mean{t}$ the cargo is bound, to obtain the average run length $\mean{x} = v \mean{t}$.

There are several methods to calculate $\mean{t}$. We can modify the graph such that it only accounts for the case when the motor is bound and promote the unbound state to an absorbing state

```{figure} absorbing2mot.png
---
height: 70px
name: absorbing2mot
---
```

Now we redirect the arrow going into the absorbing state to the starting state and close the network. 

```{figure} closed2mot.png
---
height: 70px
name: closed2mot
---
```

The inverse probability current $J$ to go along this pathway is the average time the motor is bound.

$$
J = \e S_1
$$

$S_1$ can be determined from the two-state system as

$$
S_1 = \frac{2\e}{ 2\e + \pi}
$$

Then we have:

$$
\mean{t} = J^{-1} = \frac{ 2\e + \pi}{2\e^2}
$$

An alternative way would be to consider the probability current out of the state, in which the cargo is bound to the filament and only by one motor.

Here, we need to find the conditional probability that the motor is bound and that the motor is bound in state $(1)$, which is given by

$$
S_1 = \frac{P_1}{1-P_0}
$$

Note that the term $1-P_0$ is the probability of finding a motor bound. With this result we can define an effective unbinding rate:

$$
\e_{\rm{eff}} = \e S_1 = \e \frac{P_1}{1-P_0}
$$

leading to the same average binding time (exersice):

$$
\mean{t} = \e_{\rm{eff}}^{-1} = \frac{ 2\e + \pi}{2\e^2}
$$


Now, the run length of a cargo transported by two motors is given by

$$
\mean{x}_2 = v J^{-1} = v \frac{ 2\e + \pi}{2\e^2} = \frac{v}{\e} \left(1 + \frac{\pi}{2\e}\right) = \mean{x}_1 \left(1 + \frac{1}{2} w \right)
$$


```{figure} scaling1.png
---
height: 170px
name: scale1
---
```

How does that scale with the number of motors?


### Cargo transport by multiple motors

Let's consider the case of $N$ identical motors transporting a common cargo.

```{figure} multimotor.png
---
height: 50px
name: multi
---
```

$$
\frac{d}{dt} P_0 &= -\pi_0 P_0 + \e_1 P_1\\ 
\frac{d}{dt} P_1 &= \pi_0 P_0 -(\e_1 + \pi_1) P_1 + \e_2 P_2\\
\frac{d}{dt} P_2 &= \pi_1 P_1 -(\e_2 + \pi_2) P_2 + \e_3 P_3\\
...\\
\frac{d}{dt} P_i &= \pi_{i-1} P_{i-1} -(\e_i + \pi_i) P_i + \e_{i+1} P_{i+1}\\
...\\
\frac{d}{dt} P_N &= \pi_{N-1} P_{N-1} -\e_N P_N
$$

The solution can be derived as

$$
P_n = P_0 \sum_{i=0}^{n-1} \frac{\pi_i}{\e_{i+1}}
$$
from the normalization $\sum P_n = 1$, we get

$$
P_0 = \left(1+ \sum_{n=0}^{N-1} \prod_{i=0}^{n} \frac{\pi_i}{\e_{i+1}} \right)^{-1}
$$

To calculate the run length we can use the same argument as in the case of transport by two motors and determine the conditional probability that the cargo is bound and only by one motor:

$$
S = \frac{P_1}{1-P_0}
$$

Using this result, we find the run length as

$$
\mean{x} = v\mean{t} = v \e_{\rm{eff}}^{-1} = v \e S = \frac{v}{N\pi} \left( (1+\frac{\pi}{\e})^N - 1\right)
$$

Exponential increase with $N$

Some numbers: $v = 1 \mu m/s$, $\e=1/s$, $\pi=1/s$, $N=10$

$$
\mean{x} = 0.1 \mu m (2^{10} -1) = 0.1 (1024 -1) \approx 100 \mu m
$$

```{figure} scaling2.png
---
height: 170px
name: scaling2
---
```

