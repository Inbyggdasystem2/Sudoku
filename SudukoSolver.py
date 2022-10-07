#!/usr/bin/python3

import csv #importerar typ av fil
import sys
suduko = 9 #bestämmer antal rutor som är grunden till varje sudukoruta som betår av 9 delrutor

def problem(a):
    for i in range(suduko):
        for j in range(suduko):
            print(a[i][j],end = " ")
        print()
def solve(grid, rad, kol, num):
    for x in range(9):
        if grid[rad][x] == num:
            return False
             
    for x in range(9):
        if grid[x][kol] == num:
            return False
 
 
    startRad = rad - rad % 3 
    startKol = kol - kol % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRad][j + startKol] == num:
                return False
    return True

def Suduko(grid, rad, kol):
 
    if (rad == suduko - 1 and kol == suduko):
        return True
    if kol == suduko:
        rad += 1
        kol = 0
    if grid[rad][kol] > 0:
        return Suduko(grid, rad, kol + 1)
    for num in range(1, suduko + 1, 1):
     
        if solve(grid, rad, kol, num):
         
            grid[rad][kol] = num
            if Suduko(grid, rad, kol + 1):
                return True
        grid[rad][kol] = 0
    return False
 
'''0 means the cells where no value is assigned'''

grid =[]
with open(sys.argv[1], newline='') as puzzle:
     reader = csv.reader(puzzle, delimiter=',')
     for rad in reader:
        for i in range(len(rad)):
            rad[i]=int(rad[i])#omvandla till int
        grid.append(rad)
            
 
if (Suduko(grid, 0, 0)):
    problem(grid)

else:
   print("Solution doesn't exist")

with open('solved.csv', 'w', newline = '') as solved:
      writer = csv.writer(solved)
      for line in range(9):
         p = grid[line]
         writer.writerow(p)
