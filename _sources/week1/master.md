# The Master equation

It has been very successful to base stochastic descriptions of molecules and cellular processes on continuous time Markov processes. These processes are memory-less and the most simple realization can be explained with a two-state system.

Let's consider a system that can be in two states: state $(1)$ and state $(2)$. The system stochastically jumps between these two states.

```{figure} 2states.png
---
height: 120px
name: 2states
---
```

The jump process is described by two transition rates $k_{12}$ and $k_{21}$, which can be determined in this simple example from the inverse mean waiting times in the states

$$
k_{12} = \mean{t_1}^{-1}
$$

The probability that the process jumps from $(1)$ to $(2)$ in the time interval between $t$ and $t+dt$ is given by

$$
k_{12} dt
$$

Let's assign time-dependent probabilities $P_1(t)$ and $P_2(t)$ to the states, respectively:

```{figure} 2statesP.png
---
height: 100px
name: 2statesP
---
```

Now, we consider a small time step $dt$

$$
P_1(t+dt) = P_1(t)*\mbox{prob. of staying in (1)} + P_2(t)* \mbox{prob. of leaving (2)}
$$

$$
P_1(t+dt) = P_1(t)(1 - k_{12}dt) + P_2(t) k_{21} dt
$$

$$
\frac{P_1(t+dt)-P_1(t)}{dt} = - k_{12}P_1(t) + k_{21} P_2(t)
$$

And in the limit for $dt \to 0$, we obtain the master equation

$$
\frac{d P_1}{dt} = - k_{12}P_1 + k_{21} P_2
$$

Similarily for

$$
\frac{d P_2}{dt} = - k_{21}P_2 + k_{12} P_1
$$

An important quantity is the probability current that represents the mean number of transitions per time.

$$
J_{12} = k_{12}P_1
$$

An example:

```{figure} ex.png
---
height: 200px
name: ex
---
```