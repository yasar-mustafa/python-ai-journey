# day16_mini3_read
# DictReader’ı Görmek

import csv

filename = "mini_file_day16_2.csv"

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print("Field name (headers) :",reader.fieldnames)
    print("----- Rows -----")

    for row in reader:
        print(row)
        print("Name :", row["name"])
        print("Score:", row["score"])
        print("--------")


# özetle
# 1️⃣ os → dosya var mı
# 2️⃣ writerow → satır yaz
# 3️⃣ append modu
# 4️⃣ DictReader → sözlük üret
# 5️⃣ int/float dönüşümü
