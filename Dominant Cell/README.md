# Dominant Cells in a Grid

## Problem Statement:

You are given a grid (matrix) of integers, and your task is to count the number of **dominant cells** in the grid. A cell is considered *dominant* if its value is strictly greater than all of its neighbors.

A **neighbor** is defined as any cell that shares an edge or corner with the current cell. This includes the top, bottom, left, right, and diagonal neighbors. If a cell has no neighbors (i.e., it's on the border or in a corner of the grid), it is compared only with the neighbors that exist.

## Input Format:
- The first line contains an integer `grid_rows` – the number of rows in the grid.
- The second line contains an integer `grid_columns` – the number of columns in the grid.
- The next `grid_rows` lines contain `grid_columns` space-separated integers, representing the grid.

## Output Format:
- Print the number of dominant cells in the grid.

## Example Input:
3 
3 
1 2 3 
4 5 6 
7 8 9

## Example Output:
1

## Explanation:

In the given 3x3 grid, only the center cell `9` is greater than all its neighbors:  
- Neighbors of `9` are `6,5,8`.
- All other cells have at least one neighbor with a value greater than or equal to their own.
