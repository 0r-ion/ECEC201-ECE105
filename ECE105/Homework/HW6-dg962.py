import numpy as np

"""
Daniel Goulding
14511512

ASSIGNMENT: COMPLETE function h below
"""

"""
ECE 105: Programming for Engineers 2
Created May 1, 2022
Steven Weber

Modified May 10, 2023
Naga Kandasamy

butterfly puzzle starter code

This code solves the butterfly puzzle
"""

"""
Puzzle picture to label correspondence:
* Letters A, B, C, D denote butterfies with heads showing
* Letters a, b, c, d denote butterflies without heads showing
* Letters (A,a): Orange and black (Monarch) butterfly
* Letters (B,b): Blue butterfly
* Letters (C,c): Orange and gray butterfly
* Letters (D,d): Yellow and black butterfly
"""

"""
solve(T, R, I, X, E): partial placement (T,R) with pool I of puzzle (X,E)
T: 2-dim array with non-zero entries holding tile indices indicating placement
R: 2-dim array with non-zero entries holding rotation indices for placed tile
I: unplaced tiles
X: dictionary of tiles
E: dictionary indicating edge alignments
"""
def solve(T, R, I, X, E):
    # if no tiles in I to place then puzzle is complete
    if not I: return True
    # p holds location of first empty position in T
    p = np.array(np.where(T == 0)).T[0]
    # iterate over all unplaced tiles i in I
    for i in I:
        # iterate over all four rotations
        for j in range(1, 5):
            # check if position p holds tile i with rotation j
            if check(p, i, j, T, R, X, E):
                # place tile i with rotation j in position p, remove from I
                T[p[0],p[1]], R[p[0],p[1]] = i, j
                I.remove(i)
                # return True if this placement leads to a solution
                if solve(T, R, I, X, E): return True
                # dead end: place tile back in pool I
                T[p[0],p[1]], R[p[0],p[1]] = 0, 0
                I.append(i)
    return False

# dictionaries of four rotations of a tile x
def g(x):
    return {
        1 : { 1: x[0], 2: x[1], 3: x[2], 4: x[3] },
        2 : { 1: x[3], 2: x[0], 3: x[1], 4: x[2] },
        3 : { 1: x[2], 2: x[3], 3: x[0], 4: x[1] },
        4 : { 1: x[1], 2: x[2], 3: x[3], 4: x[0] }
    }

# check if tile index i with rotation index j may be placed in position p
# i.e., check the positions neighboring p to see if the tile (if any) aligns
def check(p, i, j, T, R, X, E):
    # tile index i in rotation index j
    x = g(X[i])[j]
    # T side length
    n = T.shape[0]

    # edges of tile x are interpreted as follows:
    # 1: north, 2: east, 3: south, 4: west

    # north edge exists and a tile is present and doesn't match its south edge
    if p[0]>0 and T[p[0]-1,p[1]]:
        # tile index and rotation index for tile north of p
        i_n, j_n = T[p[0]-1,p[1]], R[p[0]-1,p[1]]
        # fail if placed tile's north edge mismatches north tile's south edge
        if E[x[1]] != g(X[i_n])[j_n][3]: return False

    # east edge exists and a tile is present and doesn't match its west edge
    if p[1] < n-1 and T[p[0],p[1]+1]:
        # tile index and rotation index for tile east of p
        i_n, j_n = T[p[0], p[1]+1], R[p[0], p[1]+1]
        # fail if placed tile's east edge mismatches east tile's west edge
        if E[x[2]] != g(X[i_n])[j_n][4]:
            return False

    # south edge exists and a tile is present and doesn't match its north edge
    if p[0] < n-1 and T[p[0]+1,p[1]]:
        # tile index and rotation index for tile south of p
        i_n, j_n = T[p[0]+1, p[1]], R[p[0]+1, p[1]]
        # fail if placed tile's south edge mismatches south tile's north edge
        if E[x[3]] != g(X[i_n])[j_n][1]:
            return False

    # west edge exists and a tile is present and doesn't match its south edge
    if p[1] > 0 and T[p[0],p[1]-1]:
        # tile index and rotation index for tile north of p
        i_n, j_n = T[p[0], p[1]-1], R[p[0], p[1]-1]
        # fail if placed tile's west edge mismatches west tile's east edge
        if E[x[4]] != g(X[i_n])[j_n][2]:
            return False

    # no edge misalignments are present
    return True

# print_puzzle(T, R, X): print the puzzle in readable format
# Todo: generalize this code to print n x n puzzles
def print_puzzle(T, R, X):
    n = T.shape[0]
    print('-'*13)
    for i in range(n):
        print('| ', end='')
        for j in range(n):
            eN = g(X[T[i,j]])[R[i,j]][1]
            print('{} |'.format(eN),end='')
            print(' ', end='') if j < n-1 else print('')
        print('|', end='')
        for j in range(n):
            eW = g(X[T[i,j]])[R[i,j]][4]
            ti = T[i,j]
            eE = g(X[T[i,j]])[R[i,j]][2]
            print('{}{}{}|'.format(eW, ti, eE),end='')
            print('', end='') if j < n-1 else print('')
        print('| ', end='')
        for j in range(n):
            eS = g(X[T[i,j]])[R[i,j]][3]
            print('{} |'.format(eS),end='')
            print(' ', end='') if j < n-1 else print('')
        print('-'*13)

if __name__ == "__main__":
    # Five quantities for solution: T, R, I, X, E
    # T: tiles: 3x3 numpy array, initalized to zero, holds tile indices
    # R: rotations: 3x3 numpy arra, initialized to zero, holds rotation indices
    # I: indices: list of tile indices not yet placed in board
    # X: tile dictionary with indices as keys and sides as values (from puzzle)
    # E: edge dictionary indicating compatible edge pairs

    # Initializations
    n = 3
    T = np.zeros((n,n), dtype=int)
    R = np.zeros((n,n), dtype=int)
    I = list(range(1, n**2+1))

    # Tile dictionary
    X = {
        1: ['a','B','C','d'],
        2: ['a','d','C','B'],
        3: ['a','D','A','b'],
        4: ['A','B','c','D'],
        5: ['A','D','c','b'],
        6: ['d','c','B','D'],
        7: ['A','b','c','D'],
        8: ['A','C','b','C'],
        9: ['a','d','b','c']
    }

    # edge alignment dictionary
    E = {
        'a': 'A',
        'A': 'a',
        'b': 'B',
        'B': 'b',
        'c': 'C',
        'C': 'c',
        'd': 'D',
        'D': 'd'
    }

    if solve(T, R, I, X, E):
        print("Solution:")
        print_puzzle(T, R, X)
    else: print("No solution found")
