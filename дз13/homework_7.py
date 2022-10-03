#7

def get_depth(start, end):
  return start + (end - start) / 2


def get_danger(depth):
  return depth**3 - 3 * depth**2 - 12 * depth + 10

depth_from = 0
depth_to = 4
max_danger = float(input("Введите максимально допустимый уровень опасности: "))
depth = get_depth(depth_from, depth_to)
danger = get_danger(depth)
if max_danger <= 0:
    print("ошибка")
else:
    while abs(danger) > max_danger:
        if danger > 0:
            depth_from = depth
        else:
            depth_to = depth
        depth = get_depth(depth_from, depth_to)
        danger = get_danger(depth)
print("Приблизительная глубина безопасной кладки: ", depth, "м")