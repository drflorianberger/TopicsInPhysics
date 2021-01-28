# Cargo under Force

### Force-dependency of single motors


IMAGE

Recall, we introduced the force-velocity relation and the force-dependent unbinding rate.


What happens if a cargo is under a constant load force $F$ and transported by two motors?

IMAGE

As a first approximation, we can assume that the force is equally shared between the two motors when they are bound to the filament, such that

$$
F_{\rm{mot}} = F/2. 
$$

Now, we can assign different velocities to our state diagram

IMAGE

in which

$$
v_i = v(F/i)
$$

The average velocity is now given by

$$
\mean{v} = \sum v_i P_i
$$

To account for the force-dependent unbinding behavior we make the same approximation and introduce an unbinding rate that depends on the force:

IMAGE

Now for our effective rates we obtain

$$
\e_i = i \e(F/i) = i \e_0 e^{F/i \Fd}
$$