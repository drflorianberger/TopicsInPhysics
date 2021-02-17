# Fluctuation analysis of voltage-gated ion channels


Consider our main result,

$$
\sigma^2(I) = i_{\rm{o}} I - \frac{I^2}{N}.
$$ (eq:mr)

We need to find a way to change $I$ without changing $N$ or $i_{\rm{o}}$. Changing $N$ is not very likely because it is a parameter of the cell.

For voltage-gated channels, we know that

$$
I = I(V), 
$$

however, we also know that

$$
i_{\rm{o}} = \gamma (V-V_{\rm{rest}})
$$

and, therefore, we cannot just gradually change $V$ and obtain a parabola from equation {eq}`eq:mr` .

The solution is to realize that $\Po$ is a function of time

$$
I = N \mean{i} = N i_{\rm{o}}(V) \Po(V,t) 
$$

For a step in $V$ we expect


```{figure} step.png
---
height: 200px
name: bol
---
```

With this reasoning, we can determine a mean current and the variance from many repetitive experiments, in which we apply a step in the membrane voltage


```{figure} Isigma.png
---
height: 200px
name: bol
---
```