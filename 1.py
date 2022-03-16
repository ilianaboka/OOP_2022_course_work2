carsperminute, minute = map(int, input().split())
massiv = input().split()
jam = len(massiv)
car = 0
for i in range(jam):
  car = car - carsperminute + int(massiv[i])
  if car < 0:
    car = 0
print(car)