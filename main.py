import random as rd
import numpy as np


#print(reduce(lambda x,y : zip(x,y), [1,2,3]))
N = 3
#zero is the empty box
board = np.array(rd.sample(list(range(N**2)),N**2)).reshape((N,N))
goal = np.array(list(range(1,N**2))+[0]).reshape((N,N))

def mixing(node):
    curr = node
    rest = []
    for i in range(rd.randint(1,N**2)):
        step = rd.choices(curr.tonext(), k = 1)
        curr = curr.move(step)
        rest = rest + step
    return curr, rest

def isin(a): return a[0] in range(N) and a[1] in range(N)
def add(a,b): return tuple(map(lambda x,y: x+y, a,b))

class Node:
    def __init__(self, board_, path = []):
        self.b = board_
        self.p = path
        print(board_)
        self.e = tuple(map(lambda x:int(x),np.where(board_ == 0)))
        #self.h =hhh(board_)
        self.h = hash(np.array2string(board_, precision=2, separator=',', suppress_small=True))
        self.step = [[0,1],[1,0],[-1,0],[0,-1]]
    def tonext(self):return list(filter(isin,(map(lambda x: add(self.e,x),self.step))))
    def move(self, step):
        rest = np.array(self.b)
        empty = self.e
        for s in step:
            rest[empty] =  rest[s]
            rest[s] = 0
            empty = s
        print(self.p + step)
        return Node(rest, self.p + step)
def hhh(ls):
    return sum(map(lambda x,y: x*y, ls.flatten()+1, range(1,N**2+1)))


def bfs(src, tar):
    q = [src]
    e = []
    while q!= []:
        currnode = q.pop(0)
        if currnode.h not in e:
            e.append(currnode.h)
            for s in currnode.tonext():
                nextnode = currnode.move([s])
                if nextnode.h == tar.h:
                    return nextnode.p
                q.append(nextnode)
    return None

leaf = Node(goal)
root, solution = mixing(leaf)
print()
print(solution)
print(root.move(solution).b)

sol = bfs(root, leaf)



print(root.b)
print(leaf.b)

print(solution)
print(sol)
print()
print(root.move(solution).b)
print(root.move(sol).b)