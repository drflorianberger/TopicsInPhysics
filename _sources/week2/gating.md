# Gating of Ion Channels


The opening and closing of ion channels can be induced by different stimuli. This mechanism is called gating. Ion channels can be categorized depending on their gating mechanism:
- Voltage-gated channels
- Tension-gated channels
- Ligand-gated channels
- Temperature-gated channels
- Light-gated channels

In our simple description of the channel dynamics, a gating mechanism with stimulus S changes the energy difference between the closed and the open state

$$
\Delta E = \Delta E(S)
$$ 

To linear order, we can assume that the energy difference decreases linearly with the stimulus, thus increasing the probability that the channel is open:

$$
\frac{\Po}{\Pc} = e^{-\Delta E(S)/kT}
$$

```{figure} ensep.png
---
height: 150px
name: ense
---
```

Voltage-gated ion channel increase their open probability by an increasing membrane voltage V. In our description, we assume a linear dependence: $\Delta E(V) = -\alpha V + \beta$, with the two free parameters $\alpha$ and $\beta$. Together with $\Po + \Pc = 1$ and

$$
\frac{\Po}{\Pc} = e^{-\Delta E(V)/kT}, 
$$

we derive the steady-state probability

$$
\Po(V) = \frac{1}{1+e^{(\beta - \alpha V)/kT}}
$$


```{figure} bol.png
---
height: 150px
name: bol
---
```

In experiments, the voltage is changed instantaneously with a step. We expect from {eq}`eq:2state` that there is a transient behavior of the open probability and, therefore, it depends on time and voltage:

$$
\Po = \Po(V,t).
$$

```{figure} vg.png
---
height: 150px
name: vg
---
```