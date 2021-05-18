import numpy as np
import random

def printSoduko(soduko):
    for i in range (9):
        for j in range(9):
            print (int(soduko[i][j]), end = ",")
            if (j in [2,5]):
                print (" | ", end ="")
        print ("")
        if (i in [2,5]):
            print ("------------------------")

def inputSoduko(soduko):
    print ("Enter soduko: ")
    for i in range(9):
        x = [int(j) for j in input().split()]
        for j in range (9):
            soduko[i][j]= x[j]

def isValid(soduko, x, y, val):
    for i in range(9):
        if (soduko[i][y] == val):
            return False
    for j in range(9):
        if (soduko[x][j] == val):
            return False

    subi = 3 * (y//3)
    subj = 3 * (x//3)
    for i in range (3):
        for j in range(3):
            if (soduko[subi + i][subj + j] == val):
                return False

    return True

def solveSoduko(soduko, i, j):
    if (i == 9):
        printSoduko(soduko)
        return "yay"

    if (j == 8):
        nexti = i + 1
        nextj = 0
    else:
        nexti = i
        nextj = j + 1
    
    if (soduko[i][j] != 0.0):
        solveSoduko(soduko, nexti, nextj)
    else:
        for possibleVal in range (9):
            if (isValid(soduko, i, j, possibleVal) == True):
                soduko[i][j] = possibleVal
                solveSoduko(soduko, nexti, nextj)
                soduko[i][j] = 0.0
    print(nexti, nextj)



soduko = np.zeros((9,9))
inputSoduko(soduko)
printSoduko(soduko)
solveSoduko(soduko, 0, 0)
