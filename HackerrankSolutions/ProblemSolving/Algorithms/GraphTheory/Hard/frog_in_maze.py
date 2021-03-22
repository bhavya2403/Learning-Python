# # denotes an obstacle.
# A denotes a free cell where Alef is initially in.
# * denotes a cell with a mine.
# % denotes a cell with an exit.
# O denotes a free cell (which may contain an entrance to a tunnel).

def prob(n, m, k, grid, tun1, tun2):
    pass

n, m, k = map(int, input().split())  # m, n = (1,20), k = (0, mn/2), k=no of tunnels, n=rows
grid = []
tun1 = {}
tun2 = {}
for _ in range(n):
    arr = list(input().rstrip())
    grid.append(arr)
for _ in range(k):
    tun = list(map(int, input().split()))
    tun1[(tun[0], tun[1])] = tun[2], tun[3]
    tun2[(tun[2], tun[3])] = tun[0], tun[1]
print(prob(n, m, k, grid, tun1, tun2))