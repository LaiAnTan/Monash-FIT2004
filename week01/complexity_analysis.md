# Complexity Analysis

## Measures of Complexity

### Best-case complexity

The *best-case* complexity of an algorithm is the fewest possible instructions that the algorithm will execute over any possible input, as a function of the input size.

$$
t_{\text{best}}(n)=\min\limits_{I \in \mathbb{I}(n)}{T_A(I)}
$$

Note: A common mistake is thinking that the best-case complexity of an algorithm is determined by its behavior for small (or no imput).

### Worst-case complexity

The *worst-case* complexity of an algorithm is the most instructions that the algorithm will execute over any possible input, as a function of the input size.

$$
t_{\text{worst}}(n)=\max\limits_{I \in \mathbb{I}(n)}{T_A(I)}
$$

> In FIT2004, when *complexity* is mentioned without further specification, assume it means the **worst-case** complexity.

### Average-case complexity

The *average-case* complexity of an algorithm is the average number of instructions that the algorithm will execute, averaged over all possible inputs of a given size, as a function of the input size.

$$
t_{\text{average}}(n)=\underset{I \in \mathbb{I}(n)}{\mathbb{E}}T_A(I)
$$

## Asysmptotic Notation

Complexities are expressed in terms of *asymptotic notation*.

### Big-O Notation

Denotes an **upper bound** on the size of the function. \

Formally,
$$f(n) = O(g(n))$$
as $n \to \infty$ if there are constants $c$ and $n_0$ such that
$$f(n) \leq c \cdot g(n)$$
for all $n \geq n_0$.

> For all values of $n$ above a threshold $n_0$, $f$ is always no bigger than some constant multiple of $g$.

Note that big-O bounds can be overestimates. \
For example, $2n+1$ could be bounded as $O(n)$ or $O(n^3)$, where both are correct, just that the former is a tighter bound than the latter.

### Big-$\Omega$ Notation

Denotes a **lower bound** on the size of the function.

Formally,
$$f(n) = \Omega(g(n))$$
as $n \to \infty$ if there are constants $c$ and $n_0$ such that
$$f(n) \leq c \cdot g(n)$$
for all $n \geq n_0$.

> $f(n)$ is at least as big as the order of magnitude of $g(n)$.

Note that big-$\Omega$ bounds can be underestimates. \
For example, $n^5$ can be bounded as $\Omega(n^2)$ or $\Omega(n^5)$, where the latter is a tighter bound than the former.

### Big-$\Theta$ Notation

Denotes both an upper bound and a lower bound, i.e. big-O and big-$\Omega$ at the same time.

Formally,
$$f(n) = \Theta(g(n))$$
as $n \to \infty$ if
$$f(n) = O(g(n)) \land f(n) = \Omega(g(n))$$
as $n \to \infty$.

Big-$\Theta$ notation implies the bound given is precise (neither an overestimate nor an underestimate).

## Space Complexity

*Space complexity* is the total amount of space used by an algorithm as a function of the input size.

$$
\text{Space complexity} = O(\text{input}) + O(\text{auxiliary})
$$

**Auxiliary** space complexity is the amount of space excluding the space taken by the input (extra space).

### In-place Algorithm

An algorithm is **in-place** is an algorithm that has $O(1)$ auxiliary space complexity, i.e. only requires constant space in addition to the space taken by its input.

Note: Recursive algorithms are **not** in-place, as the recursive stack also counts as auxiliary space used.

## Recurrence Relations

A **Recurrence relation** is an equation that recursively defines a sequence of values, and one or more base cases are given.

### Common recurrence relations

Recurrence relations for common complexities are as follows:

#### Logarithmic Complexity

$$
T(n)=\begin{cases}
T(\frac{n}{2})+a &\text{if}\;n > 1 \\
b &\text{if}\;n=1
\end{cases}
$$

with the solution:

$$T(n)=a\log_2(n)+b$$

Example of algorithms with logarithmic complexity:

- Binary search

#### Linear Complexity

$$
T(n)=\begin{cases}
T(n-1)+a &\text{if}\;n > 0 \\
b &\text{if}\;n=0
\end{cases}
$$

with the solution:

$$T(n)=an+b$$

Example of algorithms with linear complexity:

- Linear search

#### Superlinear Complexity

$$
T(n)=\begin{cases}
2T(\frac{n}{2})+an &\text{if}\;n > 1 \\
b &\text{if}\;n=1
\end{cases}
$$

with the solution:

$$T(n)=an\log(n)+bn$$

Example of algorithms with superlinear complexity:

- Merge sort

#### Quadratic Complexity

$$
T(n)=\begin{cases}
T(n-1)+cn &\text{if}\;n > 0 \\
b &\text{if}\;n=0
\end{cases}
$$

with the solution:

$$T(n)=c\left(\frac{n(n + 1)}{2}\right)+b$$

Example of algorithms with quadratic complexity:

- Worst-case Quicksort

#### Exponential Complexity

$$
T(n)=\begin{cases}
2T(n-1)+a &\text{if}\;n > 0 \\
b &\text{if}\;n=0
\end{cases}
$$

with the solution:

$$T(n)=(a+b)\times 2^n - a$$

### Solving Recurrence Relations

We can solve recurrence relations using the following steps:

1. Find cost when input is base case
2. Find cost when input is general case through telescoping

    > Telescoping is defining the general case in terms of smaller n values

3. Reduce general case cost to be in terms of base case cost
4. Simplify and find time complexity

Observe the following function:

```python
def power(x, n)
    if n == 0
        return 1
    elif n == 1
        return x
    else
        return x * power(x, n - 1)
```

Cost when $n = 1$:
> $T(1) = b$

Perform telescoping to see patterns in recurrence relation:

> $T(n) = T(n - 1) + c$ \
> $T(n) = T(n - 2) + c + c$, since $T(n - 1) = T(n - 2) + c$ \
> $T(n) = T(n - 3) + c + c + c$, since $T(n - 2) = T(n - 3) + c$

We can see that the number subtracted from $n$ is the number of $c$'s in the equation.

Construct general case based on patterns observed:

> Generally, $T(n) = T(n - k) + ck$ where $k > 1$

Define general case in terms of base case and find complexity:

> $$\begin{align*} n - k &= 1 \\ -k &= 1 - n \\ k &= n - 1\end{align*}$$
> $$\begin{align*} T(n) &= T(n - (n - 1)) + c(n - 1) \\ T(n) &= T(1) + cn - c \\ T(n) &= b + cn - c \\ T(n) &= O(n)\end{align*}$$
