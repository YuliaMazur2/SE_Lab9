with open("data.csv", 'r') as file:
    total = 0
    under_30 = 0
    over_60 = 0

    for line in file:
        row = line.split(",")

        # проверяем каждую строку с возрастом
        if row[1] == 'Survived' or row[1] == '1' or row[6] == '':
            continue

        total += 1
        age = float(row[6])
        if age < 30:
            under_30 += 1
        elif age > 60:
            over_60 += 1

print(f'Общее количество погибших пассажиров, у которых указан возраст: {total} (100.0%)')
print(f'Погибшиих пассажиров младше 30 лет: {under_30} ({under_30 / total * 100:0.1f}%)')
print(f'Погибших пассажиров старше 60 лет: {over_60} ({over_60 / total * 100:0.1f}%)')
