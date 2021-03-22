
n, b = map(int, input().split()) # n can be 16,32,64,128
arrC = list(map(int, input().split())) # takes Ci*w ns to pop
arrD = list(map(int, input().split())) # takes Di*w ns to push
arrB = list(map(int, input().split())) # weights of block 1,2,3,4...
d = {} # weight of block: arrB[i]
pop_push_time = [] # [arrC, arrD]
wei_in_each_cont = []
for _ in range(n):
    arr = list(map(int, input().split()))
    wei_in_each_cont.append(arr)
# time should be minimum
