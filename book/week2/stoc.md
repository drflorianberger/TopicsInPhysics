# Stochastic Dynamics of Ion Channels

Ion channels are proteins embedded in membranes. When their pore is open, ions can diffuse through. The opening and closing of the pore are associated with a conformational change of the protein: a change in its shape. Because proteins display fluctuations in a thermal environment, the opening and closing dynamics of ion channels are best represented by a stochastic description.

The simplest approach is to assign an open state $(o)$ and a closed state (c) to the channel, and describe the transition between the open and closed states with the rate $\koc$ and the reverse transition with $\kco$.

```{figure} channel.png
---
height: 150px
name: chan
---
```

Now, we can write down the Master equation for the time evolution of the probabilities:

$$
\frac{d}{dt} \Po = - \koc \Po + \kco \Pc \\
\frac{d}{dt} \Pc = - \kco \Pc + \koc \Po \\
$$ (eq:2state)

With the normalization requirement $\Po + \Pc = 1$, we can solve this equations, see EXERSICES.

$$
\frac{\Po}{\Pc} = \frac{\kco}{\koc} = e^{-\Delta E/kT}
$$

The last equation relates the state probabilities to the energy difference of these states (Boltzmann).

```{figure} energy.png
---
height: 90px
name: en
---
```