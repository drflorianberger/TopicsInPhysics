# Random Variables

We cannot predict the value of a random variable in the future from the information that we have at the present.

However, we can make probabilistic statements about the future.

Example coin flipping:

What is the probability $P(H)$ to flip heads?

$$
P(H) = \frac{\mbox{number of heads}}{\mbox{number of all flips}}
$$

This approach implies that

$$
0 \le P \le 1
$$

and with the probability P(T) of flipping tails

$$
P(H) + P(T) = 1
$$

What is the probability P(T) of tails?

$$
P(T) = 1-P(H)
$$


Let's consider two independent events: two coins. What is the probability of flipping both coins to heads

$$
P(H \mbox{ and } H) = P(H)P(H)
$$

Coming back to our initial definition,

$$
P(H) = \frac{\mbox{number of heads}}{\mbox{number of all flips}}.
$$

Is there a difference between tossing 100 coins at the same time and evaluate how many display heads, and flipping one coin a 100 times?


### The mean value

If we cannot predict the future value of a random variable, maybe we can say something about the expected mean?

Let's consider a fair die. What is the probability to toss a $1$?

$$
P(1)=\frac{1}{6}
$$

Because it is a fair die, this is also true for the other values. 

What is the mean number you expect after 6000 tosses?

Remember,

$$
\mean{x} = \frac{1}{N}\sum x_i
$$

and therefore we have

$$
\mean{x} = \frac{1*1000 + 2*1000....+ 6*1000}{6000} = \frac{21000}{6000} = 3.5 
$$

or

$$
\mean{x} = \sum_{i}^{6} i * \frac{\mbox{number of i}}{\mbox{number of all tosses}} = \sum_{i}^{6} i * P(i)  
$$

Let's consider a die with 4 faces and with the numbers 2 to 5. What is the mean?

$$
\mean{x} = \sum_{i=2}^5 i * \frac{1}{4} = 3.5
$$

Is there a way to distinguish the two systems?

### The variance

```{figure} width.png
---
height: 170px
name: width
---
```

The variance is the mean squared distance from the mean:

$$
\sigma^2 = \mean{(x-\mean{x})^2} = \mean{x^2} - \mean{x}^2
$$

For the 6 faces die, we obtain

$$
\sigma^2 = \sum_i^6 i^2 \frac{1}{6} - 3.5^2 = 2.9
$$

and for the 4-faces die, we obtain

$$
\sigma^2 = \sum_{i=2}^5 i^2 \frac{1}{4} - 3.5^2 = 1.25
$$


### Continuous random variable

A continuous random variable can have infinitely many values. Let's describe the random variable with $X$ and its value with $x$. Counting is not that straightforward compared to a discrete random number. Therefore, we need to introduce the concept of a probability density function $p(X)$. Now, we can define the probability of $X$ taking a value between $x$ and $x+dx$:

$$
P(x \le X \le x + dx) = p(x)dx
$$

Let's consider $M$ identical systems that have the random variable $X$ as an output, which can have values between $0$ and $10$. Now, I have a list of $M$ different values between $0$ and $10$. To determine the probability density function, I construct a histogram and count how many systems' outputs fall into each box with bin width $dx$.  

```{figure} histo.png
---
height: 350px
name: histo
---
```

Formally, the probability density function is then given by

$$
p(x) = \lim_{M \to \infty, dx \to 0} \frac{\mbox{number of systems with } x \le X \le x + dx}{M dx}
$$

It follows directly that

$$
p(x) \ge 0,
$$

and the normalization

$$
\int p(x)dx = 1
$$


The probability that $a\le X \le b$

$$
P(a\le X \le b) = \int_a^b p(x)dx
$$

The mean of a continuous random variable is then given by

$$
\mean{x} = \int x p(x) dx
$$

The variance is

$$
\sigma^2 = \mean{x^2} - \mean{x}^2 = \int x^2 p(x)dx - \mean{x}^2
$$