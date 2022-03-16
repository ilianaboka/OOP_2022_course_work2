n, k = map(int,input().split())
A = [0]*n
A = [int(a) for a in input().split()]
max = max(A)
min = min(A)
print(max - min)