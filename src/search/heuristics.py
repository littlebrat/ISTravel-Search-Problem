import numpy

class Heuristic:

    def __init__(self, matrix):
        self.mat = matrix

    def make_optimal(matrix):
        h = Heuristic(matrix)
        for x in range(len(h.mat)):
            h.mat[x,x] = 0
        for k in range(len(h.mat)):
            for i in range(len(h.mat)):
                for j in range(len(h.mat)):
                    if h.mat[i,j] > h.mat[i,k] + h.mat[k,j]:
                        h.mat[i,j] = h.mat[i,k] + h.mat[k,j]
        return h

    def get_heuristic(self,i,j):
        return self.mat[i,j]



