import sys
import threading
import numpy

def compute_height(n, parents):

    max_height = 0

    node = np.array(list(map(int,parents.split())))
    currentNode = np.where(node==-1)[0][0]
    parentNodes = [-1]
    visited = [-1]
    def first_un_child(childAr,visitAr):
        for a in childAr:
            if a not in visitAr:
                return a
        return 0

def main():
    impMethod = input()

    if "F" in impMethod:
        fileName = input()
        if "a" in fileName:
            return
        with open("./test/" + fileName, "r") as f:
            nodeCount = int(f.readline())
            node = f.readline()
    
    elif "I" in impMethod:
        nodeCount = input()
        node = input()

    height = compute_height(nodeCount,node)
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
