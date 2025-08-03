# Combinatorial analysis of the coins problem.

## Problem statement

How many ways are there to make change for $1 using half dollar, quarters, dime, nickel, and penny coins?

## Analysis

Lets assume the following quantites of coins:

$$
\text{half dollar coins}:\  0 \leq h \leq 2\\
\text{quarters}:\ 0 \leq q \leq 4  \\
\text{dime}:\ 0 \leq d \leq 10  \\
\text{nickels}:\  0 \leq n \leq 20 \\
\text{pennies}:\  0 \leq p \leq 100 \\
$$

The answer to the problem is the number of non-negative, integer solutions to the equation:

$$
h\times\$0.50 + q\times\$0.25 + d\times\$0.10 + n\times\$0.05 + p\times\$0.01 = \$1
$$
Dropping the currency symbol and the decimal numbers (by multiplying both sides by 100) we get
$$
50h +25q +10d +5n + e = 100
$$

This equation can be solved by *brute force* as:
```python
def brute_force():
ways_count = 0
for h in range(3): # 2 half dollars
  for q in range(5): # 4 quarters
    for d in range(11): # 10 dimes
      for n in range(21): # 20 nickels
        for p in range(101): # 100 pennies
          amount = 50*h + 25*q + 10*d + 5*n + p
          if amount == 100:
            ways_count += 1
return ways_count
```
These nested loops require 160,000 steps  ($100\times 20\times 10\times 4\times 2$ steps) to explore *every* combination of half dollars, quarters, dimes, nickels, and pennies. This is inefficient. For example, when we use one half-dollar coin ($h=1$) the amount of change we can make with the remaining denominations is $0.50$. And when $h=2$, there is no change to make.

Therefore we can write the number of quarters available as a function of the number of half dollar coins used:

```python
for h in range(0,3):
  for q in range(0, (100-50*h)//25+1):
    # etc
```
Similarly, we can write the number of dimes available, as a function of how many half dollar coins and how many quarters have been used:

```python
for h in range(0,3):
  for q in range(0, (100-50*h)//25+1):
    for d in range(0, (100-50*h-25*q)//10+1):
      # etc
```
Prunig the brute force loops reduces the number of steps from 160,000 to 7,747. Using dynamic programming can reduce the number of steps further, to 414. This number of steps, in dynamic programming, can be broken down to:
* For coin = 1: amount goes from 1 to 100 → 100 iterations
* For coin = 5: amount goes from 5 to 100 → 96 iterations
* For coin = 10: amount from 10 to 100 → 91 iterations
* For coin = 25: amount from 25 to 100 → 76 iterations
* For coin = 50: amount from 50 to 100 → 51 iterations