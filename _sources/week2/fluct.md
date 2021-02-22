# Fluctuation analysis

Let's consider a single ion channel. The current through a single channel, which is open, is given by 

$$
i_{\rm{o}}.
$$

Obviously, there is no current when the channel is closed

$$
i_{\rm{c}} = 0
$$

What is the mean current through a single ion channel?

$$
\mean{i} = \sum_{j\in \{\rm{c},\rm{o}\}} i_j P_j = i_{\rm{o}} \Po + i_{\rm{c}} \Pc = i_{\rm{o}} \Po
$$

What is the variance of this current?

$$
\sigma^2 (i) = \mean{i^2} - \mean{i} ^2 = \sum_{j\in \{\rm{c},\rm{o}\}} i_j^2 P_j - \mean{i}^2 = i_{\rm{o}}^2 \Po (1-\Po) 
$$

Let's consider a cell or a cluster with $N$ channels. Because the mean and the variance are additive, we derive

$$
I = N \mean{i} = N i_{\rm{o}} \Po 
$$

$$
\sigma^2(I) = N \sigma^2(i) = N i_{\rm{o}}^2 \Po (1-\Po) 
$$

Expressing the variance as a function of the mean results in

$$
\sigma^2(I) = i_{\rm{o}} I - \frac{I^2}{N}
$$

This result is a remarkable equation because:
- This equation is independent of the open probability $\Po$. Which can be a complicated function, difficult to measure and, therefore, in most cases unknown.
- It relates the single-molecule current $i_{\rm{o}}$ to the macroscopic current $I$ that is easier to measure.

From a measurement of the variance of the current as a function of the mean current, we can deduce the single-channel current and the number of involved channels:

```{figure} var.png
---
height: 200px
name: bol
---
```