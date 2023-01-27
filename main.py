import csv

f = open("C:/Users/Админ/Downloads/Telegram Desktop/books.csv", 'r')
reader = csv.DictReader(f, delimiter=';', quotechar='"')
maxy = sorted(reader, key=lambda x: int(x['Публикация']), reverse=True)[:10]

for row in maxy:
    print(row)


