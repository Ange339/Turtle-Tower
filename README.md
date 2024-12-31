# Turtle-Tower
There are $n$ turtles, the $i$-th of them weighs $w_i$ and can handle a total load of $l_i$ on its shell. The total weight of turtles above cannot exceed the maximum load. What is the largest number of turtles that can stand on each other, forming a tower?

## Solution

We denote turtles as $x_0, x_1, ..., x_{n-1}$. This problem can be approached with dynamic programming combined with greedy algorithms. The subproblems can be defined as follows: for any $j$ = 0, ..., $n-1$, find the feasible subset of turtles from the set { $x_0$, ... , $x_j$ } with the longest height and, ultimately, the lowest sum of weights (thus, the lightest). However, the recurrence relation can be a problem, as when considering  $x_{j+1}$, we don't precisely know where to allocate it (or if it should be allocated to other towers). To maintain the time complexity, we need to simplify our recurrence relation to only check if it's better to place $x_{j+1}$  at the bottom of a tower or to consider the current tallest tower. This can be achieved by initially sorting our turtles in a specific manner: by sorting them in non-decreasing order of the sum of weight and load. 

$Proposition$. Any feasible tower of turtles can be sorted in non-decreasing order by the sum of weight and load without reducing its height.

$Proof$. Suppose a feasible set of turtles $\{x_0, x_1, ... , x_i, x_j, ... x_{n-1}\}$ 
assuming that $w_i + l_i > w_j + l_j$, we want to show that 
```math
\{x_0, x_1, ... , x_j, x_i, ... x_{n-1}\}
```
where we swapped $x_i$ and $x_j$ is still feasible. Because the turtles $\{x_{j+1}, ... x_n\}$ won't affect the result, we can ignore them. Indeed, the original tower is feasible at the point $j$ if and only if
```math
\sum_{k=1}^{i-1} w_k + w_i \leq  l_j
```
Because of the assumption, this inequality becomes:
```math
\sum_{k=1}^{i-1} w_k + w_i <  w_i + l_i - w_j
```
Thus:
```math
\sum_{k=1}^{i-1} w_k + w_j <  l_i
```
which shows that the "swapped" tower is still a feasible set.

The intuition behind this claim is that if $w_i + l_i > w_j + l_j$, $x_i$ is better to be below of $x_j$ either because $w_i$ is too "large" thus overloading the whole tower, or that $l_i$ is so "high" that it is better to allocate it at the end of the tower where it can better support the weight. 

In any case, thanks to this property, we can first sort all turtles in non-decreasing order by the sum of weight and load, which requires $O(log(n))$, enabling us to establish the recurrence relation between subproblems effectively. Let's construct the classical matrix:

$D[i][j]$ = the longest tower (and the lightest) you can build considering $i$ turtles from the set $x_0, ... x_j$, where $i \in \{1, ... , n\}$, and $j \subseteq \{0, ..., j \}$.

Note that the optimal feasible tower built by turtles $x_0, ... x_j$ does not necessarily include $x_j$. 

By skipping the row 0 (i.e., tower built with no turtle), we start with the base case when $i = 1$, where, for every $j$, $D[1][j]$ = the lightest turtle from the subset $x_0, ... x_{j-1}$; another base case is when $j = 0$, where the subset is made up of $x_0$ alone, thus $D[i][0] = x_0$ for every $i$.

Let us denote $D[i-1][j-1]$ as $X$ (representing the optimal feasible tower using at most $i-1$ turtles from the subset), $D[i-1][j]$ as $Y$ (representing the previous optimal solution from the subset  using at most $i-1$ turtles), $D[i][j-1]$ as $Z$ (representing the optimal feasible tower using at most $i$ turtles from the subset). We need to check firstly whether $X\cup x_j$ is feasible (since we've already sorted the turtles, this represents the first possible feasible tower), and if $X \cup x_j$ is an optimal solution compared to $Y$ and $Z$. For simplicity, we denote $C$ as the optimal tower between $Y$ and $Z$ (which is the subset with the longest height, and if heights are equal, the subset with the smallest$W$). For $i = 2, ..., n$, for every $j$, $D[i][j]$ will be $|X \cup x_j|$ if and only if $W_X \leq l_j$ and $|X \cup x_j| \geq |C|$; in particular, if $|X \cup x_j| = |C|$, we will choose $|X \cup x_j|$ as solution only if $W_{X \cup x_j} < W_C$. Else, $D[i][j] = C$. The total running time of building this matrix is $O(n^2)$. For coding purposes, the algorithm of constructing the matrix can be implemented by storing in $D[i][j]$ a tuple containing $W_{OPT}$ and $H_{OPT}$ (where $OPT$ is the optimal turtle tower, $H$ is its height).

Finally, the solution is stored in $D[n][n-1]$. The total running time of the algorithm is $nlog(n) + n^2 \in O(n^2)$.
