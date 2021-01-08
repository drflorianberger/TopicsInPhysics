# The Current Through Ion Channels

```{admonition} You will learn
How electrical currents are related to the electrical potentials
```


## Ohm's law
The movement of ions generates electric currents. Ohm's law relates the current $I$ with the resistance $R$ and the voltage $V$, as

$$
I = \frac{V}{R}
$$

Introducing the conductance $G=1/R$ Ohm's law can be written as

$$
I = G V
$$ (eq:ohm)

## Ohm's laws for cells

To apply Ohm's laws for cells, we have to consider that the membrane potential of cells may not be zero at rest. This resting potential is largely a result of the equilibrium potentials of different ions, as we discussed earlier in {ref}`sec:sep`. In short for physicists, the reference point for a cell's membrane potential is outside of the cell.     

To account for the resting potential we have to extent equation {eq}`eq:ohm` with the resting potential $V_{\rm{rest}}$,

$$
I = G(V - V_{\rm{rest}})
$$

```{figure} current.png
---
height: 150px
name: sc1
---
```
## Measuring currents
By using the patch clamp tecnique, we can measure the membrane potential $V$: A glass pipette filled with the intracellular ion solution accesses the interior of the cell. Now the potential between the interior of the pipette and the bath can be measured and controlled, which is the membrane potential.

```{figure} amp.png
---
height: 150px
name: sc1
---
```