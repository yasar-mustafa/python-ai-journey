# day16_mini2_append
# CSV’ye Satır Ekleme (Append Mantığı)
# 1️⃣ Dosya yoksa header yaz
# 2️⃣ Dosya varsa header yazma
# 3️⃣ Kullanıcıdan veri al
# 4️⃣ Satır ekle

import os
import csv

filename = "mini_file_day16_2.csv"
headers = ["name", "score"]

# eğer dosya yoksa oluştur ve header yaz
if not os.path.exists(filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
    print("File created with header.")
else:
    print("file already exists.")


# kullanicidan veri al
name = input("Enter name :").strip()
score = int(input("Enter Score :"))


# satır ekle
with open(filename, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([name, score])

print("Row appended successfully ✅")


# neden "a" kullandık?
    # Çünkü:
    # Dosyanın sonuna ekleme yapmak istiyoruz
    # Önceki kayıtları korumak istiyoruz
    # Programı her çalıştırdığımızda veri büyüsün istiyoruz
    # Append = birikim.


# "w" kullansaydık ne olurdu?
    # Dosya her seferinde sıfırlanırdı
    # Sadece son girilen veri kalırdı
    # Önceki tüm kayıtlar silinirdi
    # Bu veri kaybı demek.