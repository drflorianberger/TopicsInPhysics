Week 4: Exercises
=======================
 
Cargo transported by two molecular motors 

Let's consider the following state space:

```{figure} cargo2motstatesRates.png
---
height: 170px
name: cargo2staterates
---
```

4.1) **3 Points:** Calculate the state probabilities $P_i$ in terms of the rates given in the diagram and show that they are normalized.

4.2) **1 Point:** Calculate the average time that the cargo is bound to the filament

4.3) **1 Point:** Calculate the average run length of the cargo, assuming that the velocity of the cargo in state (1) and (2) are the same.

<br />
<br />
<br />

We assume that the motors are identical and the single-motor force-velocity relation is given by

$$
v(F) = v_0(1-\frac{F}{\Fs})
$$

and the unbinding rate by

$$
\e(F) = \e_0 e^{F/\Fd}
$$

Let's assume that the cargo is exposed to a constant load force $F$ and this force is equally shared between the motors.

4.4) What are the force-dependent rates between the states?

4.5) Calculate the average run length as a function of force.