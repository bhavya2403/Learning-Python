# k - 1 and n - k each as INDIVIDUAL TREE should already be calculated previously according to the table,
# so you just have to find where those are on the table which is at c[0, k - 1] and c[k, n]
# Look now we have the rank of 2 trees and 1 single root, to push the left or right tree into a sub tree you
# need add one level on each of their node therefore add the entire weight of the tree
# The combined tree with k as root have:
# Rank(k) = Rank(left) + Rank(right) + weight(left) + weight(right) + weight(root) = Rank(left) + Rank(right) + weight(0 - n)
# c[0, n] = c[0, k-1] + c[k, n] + w(0, n) (k is the root)

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def formingTree(n, keys, roots):
    def solve(l, r):
        if l==r:
            return

        node = TreeNode(keys[roots[l][r]-1])
        node.left = solve(l, roots[l][r]-1)
        node.right = solve(roots[l][r], r)

        return node

    return solve(0, n)


def optimalBST(keys, p, q):
    n = len(keys)
    c = [[0 for _ in range(n+1)] for _ in range(n+1)]
    w = [[0 for _ in range(n+1)] for _ in range(n+1)]
    r = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        w[i][i] = q[i]

    for diff in range(1, n+1):
        for i in range(n-diff+1):
            j = i+diff
            w[i][j] = w[i][j-1] + p[j] + q[j]
            minCost, root = 10000, 0
            for k in range(i+1, j+1):
                if c[i][k-1]+c[k][j] < minCost:
                    minCost = c[i][k-1]+c[k][j]
                    root = k
            c[i][j] = minCost + w[i][j]
            r[i][j] = root

    return c[0][n], formingTree(n, keys, r)

# print(optimalBST([10, 20, 30, 40], [None, 3,3,1,1], [2,3,1,1,1]))
print(optimalBST([10, 12, 20], [None, 34, 8, 50], [0,0,0,0]))