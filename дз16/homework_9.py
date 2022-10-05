#9

n = int(input("количество друзей: "))
k = int(input("количество долговых расписок: "))
list_duty = [0] * n
for i in range(k):
    print(f"\n{i + 1}-я расписка")
    index_took = int(input("Кому: "))
    index_gave = int(input("От кого:  "))
    duty = int(input("Сколько: "))
    list_duty[index_took - 1] -= duty
    list_duty[index_gave - 1] += duty
print("\nБаланс друзей:")
for i in range(n):
    print(i + 1, ":", list_duty[i])