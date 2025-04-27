# Dynamic Programming

## Motivation

Technically, all problems can be brute forced. Unfortunately, brute forcing requires too much effort.

Suppose we want to find the $6^{th}$ fibonacci number. If we use the recursion-based algorithm, we will have to perform computations as follows:

```python
               f(6)
          _______|_________
          |               |
        f(5)            f(4)
      ____|____       ____|____
      |       |       |       |
    f(4)    f(3)    f(3)    f(2)
  ____|____           .       .
  |       |           .       .
f(3)    f(2)
  .       .
  .       .
```

Notice that `f(3)` has to be recomputed 3 times, and `f(4)` has to be recomputed 4 times. These recomputations of the same inputs contribute to the high complexity of naive fibonnaci, as we are doing the same thing over and over again.

## Core idea of DP

To solve a problem by way of dynamic programming is to solve a problem by:

1. Breaking it into smaller subproblems
2. Combining the solutions of those subproblems into a solution to the greater problem.

A problem that can be solved via dynamic programming must exhibit **two** key properties:

### Overlapping Subproblems

A problem has **overlapping subproblems** if it the same subproblems are solved multiple times during the computation of the greater problem.

For example: in the computation of the $6^{th}$ fibonnaci number, `f(6)` with the naive algorithm, `f(4)` has to be computed twice, `f(3)` has to be computed 3 times, and so on.

#### Memoization

**Memoization** is the process of remembering the solutions to previously computed subproblems, and storing them in a table for later lookup.

Instead of computing the same subproblem repeatedly, it is only computed once and stored in the table. After that, the same subproblem can be subsequently looked up from the table at *no additional cost*.

For example, the DP solution to calculate fibonacci numbers:

```python
def fib_aux(n, memo):
    if n <= 1:
        return n
    if memo[n] is not None:
        return memo[n]
    
    memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)

    return memo[n]

def fib_dp(n):
    memo = [None] * n
    return fib_aux(n, memo)
```

The fibonacci numbers that have been computed are stored in the `memo` table, and we return straight from the table whenever a problem with an already computed solution is encountered.

### Optimal Substructure

A problem has **optimal substructure** if the solution to the subproblems can be combined to form the solution of the greater problem.

For example: to compute the $n^{th}$ fibonacci number, `f(n)`, we need solutions to `f(n - 1)` and `f(n - 2)`, since `f(n) = f(n - 1) + f(n - 2)`.

> Note: Optimal substructure is also used in divide and conquer algorithms.

## Top-down vs Bottom-up Approach

Both approaches of dynamic programming still use the memoisation table to store solutions to subproblems.

### Top-down

In the top-down approach, we start from the main problem, breaking it into smaller subproblems (recursively) until the base case.

The memoisation table is filled on demand as the particular subproblems that are required are computed.

The pros of the top down approach are:

- No need to know the topoligcal ordering of the subproblem dependencies
- Avoids computing the solution to subproblems that are not needed

### Bottom-up

In the bttom up approach, we start from a base case, solving larger and larger problems (iteratively) until we reach the solution for the greater problem.

The memoisation table is filled in such a way that any dependent subproblems have already been computed before they are needed.
> The order in which the table is filled is the *reverse topological order* of the dependency graph of the subproblems.

The pros of the bottom-up approach are:

- Avoids recursion (no call stack, use less space)
- Allows for clever optimisations (space-saving trick)

## Reconstructing Optimal Solutions

Frequently we not only need to know that an optimal solution exists, we also require the solution itself. Dynamic programming algorithms can be extended to produce the optimal solution itself.

There are two main methods we can do this:

### Backtracking through the subproblems

This method involves backtracking through the subproblems to figure out which choices were made that lead to the given solution, by using the solutions stored in the memoisation table.

### Decision Table

This method involves keeping a second table in addition to the memoisation table, which is used to remember the optimal decisions that were made by each subproblem.

Once the optimal value is found, the solution can be reconstructed by lookup of the decision table.

## Classical DP Problems

### Coin Change

### Knapsack

### Edit Distance