#5
import math

volumeEarth = 10.8321 * 10**11
radius = float(input("Введите радиус случайной планеты: "))
volume = (4/3) * math.pi * radius**3
print("Объём планеты Земля", "больше" if volumeEarth >= volume else "меньше",
      round(volumeEarth / volume if volumeEarth >= volume else volume / volumeEarth, 3), "раз")