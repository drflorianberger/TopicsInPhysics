# From Single Motors to Multiple Motors

### Characteristics of a single motor

What motors can do:
- Walk along a filament (velocity)
- Bind to a filament (binding rate)
- Unbinding from a filament (unbinding rate)

In principle, this can depend on several quantities:
- Fule (free energy, ATP)
- Force


The force-dependent behavior of single molecular motors has been studied with optical traps

### Force-velocity relation

The velocity of a motor decreases with an opposing force

```{figure} forcevelo.png
---
height: 170px
name: forcevelo
---
```


- Force-free velocity $v_0$
- The Stall force $\Fs$

### Binding and unbinding

The binding process is complicated. As an approximation, we effectively describe it with a single rate

$$
\pi
$$

The unbinding process depends on the external force. It is intuitive to consider that this rate increases with the force on the molecular bond.

```{figure} unbinding.png
---
height: 170px
name: unbinding
---
```


The most accepted model is an exponential force-dependence of the unbinding rate

$$
\e = \e_0 e^{F/\Fd},
$$

in which $\e_0$ is the force-free unbinding rate and $\Fd$ is the detachment force, a characteristic force scale. 