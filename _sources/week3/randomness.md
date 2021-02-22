# Randomness

The randomness of the stochastic process can be defined as

$$
r = \frac{\mean{(x-\mean{x})^2}}{d \mean{x(t)}}
$$

For the Poisson stepper, we obtain

$$
r = \frac{d^2kt}{d dkt} = 1
$$

```{figure} rand.png
---
height: 170px
name: rand
---
```

Recall that the Poisson stepper performs directed steps with exponentially distributed waiting times.

In general, there could be several transitions of the system involved between the step.

```{figure} comprand.png
---
height: 170px
name: crand
---
```

In such a system, the randomness may be different from $1$. A measurement of the randomness provides insight into the transitions that cannot be directly seen in the experiment. This conclusion is highly relevant to elucidate the inner working mechanism of molecular motors.






