# Problem Statement

One day, Mary wanted to give a present to her friend, and she decided to give her a beautiful bouquet of flowers. She started collecting the flowers for the bouquet, and she exactly needed 2 types of flowers. The total number of flowers should be `t`. Now she starts collecting them from her garden. In her garden, there are `N` types of flowers, and each type of flower is arranged in a queue in non-decreasing order, e.g., 1, 3, 6, 15, and so on.

Now she wants your help to find which indexes of flowers she should collect.

## Input Format

Each test case consists of two lines. The first line contains integers `N` and `t` — `N` is the total types of flowers and `t` is the total number of flowers needed.

The second line contains `N` integers `a1, a2, ..., an` — elements of the array `a`.

## Output Format

Print a single line containing the indexes of flowers.

## Constraints

- `2 <= N <= 10^4`
- `1 <= a[i] <= 1000`
- `2 <= t <= 2000`
- Here, exactly one solution exists.

## Sample Testcase 0

### Testcase Input
7 5 
1 2 2 4 5 7 10

### Testcase Output
0 3


### Explanation
Flowers at 0th and 3rd indexes sum up to the target only, i.e., 1 + 4 = 5.

## Sample Testcase 1

### Testcase Input
5 2 
1 1 2 3 4

### Testcase Output
0 1


### Explanation
Flowers at 0th and 1st indexes sum up to the target only, i.e., 1 + 1 = 2.
