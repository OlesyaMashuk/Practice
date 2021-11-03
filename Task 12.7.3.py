per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("money = "))
lst = list(per_cent.values())
lst[0] = int((lst[0] * money) / 100)
lst[1] = int((lst[1] * money) / 100)
lst[2] = int((lst[2] * money) / 100)
lst[3] = int((lst[3] * money) / 100)
print("depozit =",lst)
print("Максимальная сумма, которую вы можете заработать —", max(lst))