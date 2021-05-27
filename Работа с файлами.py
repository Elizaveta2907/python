# Вывести на экран первые пять строк содержимого (включая заголовки) с помощью цикла for

with open('tour_de_france.csv') as f:
    counter = 0
    for line in f:
        if counter < 5:
            print(line)
            counter += 1