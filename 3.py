n = int(input())
spisok_n = input().split()
m = int(input())
spisok_m = input().split()
k = int(input())
spisok_k = input().split()
massiv_n = [0]*n
for i in range(n):
    massiv_n[i] = int(spisok_n[i])
massiv_m = [0]*m
for i in range(m):
    massiv_m[i] = int(spisok_m[i])
massiv_k = [0]*k
for i in range(k):
    massiv_k[i] = int(spisok_k[i])

def sortirovka(mass):
    length = len(mass)
    swaps = True
    while length > 1 or swaps:
        length = max(1, int(length / 1.25))
        swaps = False
        for i in range(len(mass) - length):
            j = i + length
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]
                swaps = True
    return mass

sortirovka(massiv_n)
sortirovka(massiv_m)
sortirovka(massiv_k)
premass = []
for i in massiv_n:
    for j in massiv_m:
        for h in massiv_k:
         if i == j == h:
            premass.append(i)

print(len(premass))