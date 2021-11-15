tickets = int(input('Введите количество билетов: '))
result = 0
for i in range(1, tickets+1):
    age = int(input(f'Введите возраст участника № {i}: '))
    if 18 <= age < 25:
        result += 990
    elif age >= 25:
        result += 1390
if tickets > 3:
    result *= 0.9
print(f'Общая стоимость билетов составляет {result} рублей')

