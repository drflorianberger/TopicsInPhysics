# Seperating Electrical Charges

```{admonition} You will learn
How ion channels can seperate charges betweeen compartments
```



## Separating charges is fundamental for neural communication
Cells seperate ions between compartments to store energy and information. These compartments are seperated by membranes with a protein machinery of pumps and channels. These pumps and channels regulate the trans-membrane ion flow, keep charge imbalances from equilibrating and thus generate and maintaine a voltage potential across the membrane. This membrane potential can be altered by chemical, electrical, or mechanical stimulation and the resulting disturbance can progagate along the cell membrane as action potentials. Action potentials are fundamental for neural communcation and travel at a rate of $10-100\, \rm{m/s}$.

## The basics of seperating charges

Imagen you have two containers, one filled with particles and the other one empty. The containers are connected by a channel which is initially blocked.

```{figure} sc1.png
---
height: 150px
name: sc1
---
Particles are in the left container and the channel is blocked.
```
How does the eqilibrated system looks like after we open the channel and let the system relax to its equilibrium state? Click below right to see the answer.
```{toggle}
In the initial system there is a concentration gradient: high concentration in the left container and low concentration in the right container. Diffusion will reduce the concentration gradient untill the concentration is the same in both containers. 
```{figure} sc1u.png
---
height: 150px
name: sc1u
---
After opening the channel the system reaches the equilibrium state without an concentration gradient.  
```

Imagen you have two containers filled with the same number of particles, but opositely charged in each containter. The containers are connected by a channel which is initially blocked.
```{figure} sc2.png
---
height: 150px
name: sc2
---
Opposietly charged particles are in the seperate containers.
```
How does the eqilibrated system looks like after we open the channel and let the system relax to its equilibrium state? Click below right to see the answer.
```{toggle}
In the initial system there is an electrical gradient: negatevly charged particles in the left container and positively charged particles in the right container, creating an electrical potential between the containers. Particles will rearange in such a way that electrical potential is neutralized.  
```{figure} sc2u.png
---
height: 150px
name: sc2u
---
After opening the channel the electrical gradient is neutralized by mixing of the particles.
```

If in equilibrium, concentration and electrical gradients are canceled out, how can we establish an electrical potential? Nature uses specific channels. These channels olny allow specific particles to go through their pores. Let's see how that works!

Imagen, we have a channel that is specific for the blue particles. Now, we consider the following system

```{figure} sc3.png
---
height: 150px
name: sc3
---
Particle are initally in the right container.
```
What happens if we open the channel?
```{toggle}
The concentration gradient will disapear!
```{figure} sc3u.png
---
height: 150px
name: sc3u
---
Particles distribute equally in both containers.
```

Imagen, we have an intially electrical neutral system with negatively and positively charged particles in the left container. Now, the channel is specific for the blue particles and only let them through to the other container.

```{figure} sc4.png
---
height: 150px
name: sc4
---
Initally electrical neutral system with plus and minus ions in the left container.
```
What happens if we open the channel?
```{toggle}
The blue particles with diffuse to the empty container in order to reduce the concentration gradient, but at the same time they will generate an electrical potential because they carry a negative charge. The system will find a compromise between the concentration gradient and the electrical gradient and a voltage potential is generated between the containers. 

```{figure} sc4u.png
---
height: 150px
name: sc4u
---
Because only the blue particles can go through the channel, some of them will diffuse to the empty container to reduce the concentration gradient. In they way they seperate from the positively charged ions and a electrical potential is generated.
```
With ion-specific channels and different ion concentrations, a membrane potential can be established even in thermodynamic equilibrium. This potential is the Nernst potential, also called equilbirum potential.

## EXTRA: The Nernst Equation

The Nerst potential can be derived from thermodynamical considerations and is given by:

$$
V_{\rm{eq}} = \frac{RT}{z F}\log\frac{[C]_{\rm{out}}}{[C]_{\rm{in}}},
$$

in which RT is the universal gas constant times the temperature, z is the valence of the ionic species, F is Faraday's constant, and $[C]_{\rm{out}}$, $[C]_{\rm{in}}$ are the concentration of the ion outside and inside, respectevely. 





## Key Concepts
```{admonition} Now, you should know
How an elctrical potential can be generated between compartments and why ion channels must be specifc and cannot be just wholes in the seperating membrane.
```

## Additional material

#Open jupyter notebook from command line, go to cell tools and edit meta tag to hide input!
from IPython.display import YouTubeVideo
YouTubeVideo('Ba02v7eoVWQ')

# Terms and concepts used in the paper

- Membrane with channels

In biology, different compartments are separated by membranes. Different ionic solutions in these compartments result in different potentials (voltages) between these compartments. Proteins in the membrane can regulate the flow of ions, either by pumping or open pores for specific ions.  Channels are proteins in a membrane that allow ions to traverse through their pores. Channels can be gated with different mechanisms, here we consider voltage-gated ion channels. The current through a single channel when its open is called the single-channel current.  
- Electrophysiology

Experimental techniques to measure currents and voltages in cells and tissue.

- Channel conductance
- Dwelling times
- Open probability
- ensemble average / time average
- depolarization



membrane potential:
https://www.physiologyweb.com/lecture_notes/resting_membrane_potential/resting_membrane_potential_membrane_ionic_current_equations.html

# Notation in the paper

- $i$ single channel current
- $N$ number of channels 
- $P_0$ open probability
- $\gamma$ single channel conductance