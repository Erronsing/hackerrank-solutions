#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
position_list = []
for grid_i in xrange(n):
   grid_t = [int(ch) for ch in str(raw_input().strip())]
   grid.append(grid_t)
for grid_i in xrange(1,n-1):
    for j in xrange(1,n-1):
        if grid[grid_i][j] > grid[grid_i-1][j]:
            if grid[grid_i][j] > grid[grid_i][j-1]:
                if grid[grid_i][j] > grid[grid_i+1][j]:
                    if grid[grid_i][j] > grid[grid_i][j+1]:
                        position_list.append((grid_i, j))
for item in position_list:
    grid[item[0]][item[1]] = 'X'
for line in grid:  
    print ''.join(str(x) for x in line)