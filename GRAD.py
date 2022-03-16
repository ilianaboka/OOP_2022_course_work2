import math
n, h = map(float, input().split())                          #Ввод количества вершин n и высоты забора h
n = int(n)
massparkx = [0]*n                                           #Создание массива для хранения Х координат парковки
massparky = [0]*n                                           #Создание массива для хранения Y координат парковки

for i in range(n):                                          #Заполнение массивов
    massparkx[i], massparky[i] = input().split()

d, xl, yl = map(float, input().split())                     #Ввод мощности лазера d и координат лазера
k = int(input())                                            #Ввод количества градин
gradX = [0]*k                                               #Создание массива для хранения Х координат падения града
gradY = [0]*k                                               #Создание массива для хранения Y координат падения града

for i in range(k):                                          #Заполнение массивов
    gradX[i], gradY[i] = input().split()


#Определение местоположения точки падения
crosscountn = 0
crosscount = 0
gradcount = 0
Cn = (float(massparky[n-1]) - float(massparky[0]))/(float(massparkx[n-1]) - float(massparkx[0]))
Bn = (float(massparky[n-1]) * float(massparkx[0]) - float(massparky[0]) * float(massparkx[n-1])) / (float(massparkx[0]) - float(massparkx[n-1]))
for i in range(k):
    C1 = (float(gradY[i]))/(float(gradX[i]) - 1001)
    B1 = (float(gradY[i])*1001)/(1001 - float(gradX[i]))
    CrossXn = (Bn - B1) / (C1 - Cn)
    CrossYn = (B1 * Cn - Bn * C1) / (Cn - C1)
    if min(float(gradX[i]), 1001) <= CrossXn <= max(float(gradX[i]), 1001) and min(float(massparkx[n-1]), float(massparkx[0])) <= CrossXn <= max(float(massparkx[n-1]), float(massparkx[0])) and min(float(gradY[i]), 0) <= CrossYn <= max(float(gradY[i]), 0) and min(float(massparky[n-1]), float(massparky[0])) <= CrossYn <= max(float(massparky[n-1]),float(massparky[0])):
        crosscount += 1
        crosscountn += 1
    for j in range(n-1):
       C2 = (float(massparky[j]) - float(massparky[j+1]))/(float(massparkx[j]) - float(massparkx[j+1]))
       B2 = (float(massparky[j])*float(massparkx[j+1]) - float(massparky[j+1])*float(massparkx[j]))/(float(massparkx[j+1]) - float(massparkx[j]))
       CrossX = (B2 - B1)/(C1 - C2)
       CrossY = (B1*C2 - B2*C1)/(C2 - C1)
       if min(float(gradX[i]),1001)<=CrossX<=max(float(gradX[i]),1001) and min(float(massparkx[j]),float(massparkx[j+1]))<=CrossX<=max(float(massparkx[j]),float(massparkx[j+1])) and min(float(gradY[i]),0)<=CrossY<=max(float(gradY[i]),0) and min(float(massparky[j]),float(massparky[j+1]))<=CrossY<=max(float(massparky[j]),float(massparky[j+1])):
           crosscount += 1
    if crosscount % 2 == 0 and xl != float(gradX[i]) and yl != float(gradY[i]):
        Ax = float(gradX[i]) - xl
        Ay = float(gradY[i]) - yl
        A = math.sqrt(Ax * Ax + Ay * Ay)
        if A < d:
            B = math.sqrt(d*d - A*A)
            if B > h:
               CA = (yl - float(gradY[i]))/(xl - float(gradX[i]))
               BA = (yl * float(gradX[i]) - float(gradY[i]) * xl)/(float(gradX[i]) - xl)
               if crosscountn > 0:
                   Vx = CrossXn - xl
                   Vy = CrossYn - yl
                   V = math.sqrt(Vx * Vx + Vy * Vy)
                   Cd = B/V
                   R = Cd * V
                   if R > h:
                       gradcount += 1
               else:
                   for j in range(n - 1):
                       C2 = (float(massparky[j]) - float(massparky[j + 1])) / (float(massparkx[j]) - float(massparkx[j + 1]))
                       B2 = (float(massparky[j]) * float(massparkx[j + 1]) - float(massparky[j + 1]) * float(massparkx[j])) / (float(massparkx[j + 1]) - float(massparkx[j]))
                       CrossX = (B2 - BA) / (CA - C2)
                       CrossY = (BA * C2 - B2 * CA) / (C2 - CA)
                       if (min(xl,float(gradX[i])) <= CrossX <= max(xl,float(gradX[i]))) & (min((float(massparkx[j]),float(massparkx[j+1]))<=CrossX<=max(float(massparkx[j]),float(massparkx[j+1])))) & (min(yl,float(gradY[i])) <= CrossY <= max(yl,float(gradY[i]))) & (min(float(massparky[j]),float(massparky[j+1]))<=CrossY<=max(float(massparky[j]),float(massparky[j+1]))):
                           Vx = CrossX - xl
                           Vy = CrossY - yl
                           V = math.sqrt(Vx * Vx + Vy * Vy)
                           Cd = B / V
                           R = Cd * V
                           if R > h:
                               gradcount += 1
                           else:
                               continue
            else:
                continue
        else:
            continue
    else:
        gradcount += 1
print(gradcount)

