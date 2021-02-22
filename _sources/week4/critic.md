# Critique of the Model

### What are the underlying assumptions?


```{figure} 2cargoful.png
---
height: 170px
name: 2cargofull
---
```

- Single motor behavior
- Force sharing
- Identical motors
- Interaction between the motors

### Experimental validation

It is extremely difficult to control the number of functioning motor proteins in an experiment. Experimentalists successfully developed DNA origami techniques to couple precisely motor proteins.

```{figure} diehl.png
---
height: 170px
name: diehl
---
```

In the load-free case, what would we expect from our model?

The average time that both motors are bound to the filament should be half the average binding time of a single motor:

$$
\mean{t}_2 = 0.5*\mean{t}_1,
$$

but the velocity should be the same (load-free case)

$$
v_2 = v
$$

However, these experiments suggested that

$$
\mean{t} = 0.15*\mean{t}_1
$$

and

$$
v_2 = v_1
$$

Possible explanation:

- Negative interference between the motors

[Experimental study](https://doi.org/10.1039/B900964G)

[Theoretical study](https://doi.org/10.1103/PhysRevLett.108.208101)