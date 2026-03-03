# Mini Project 1 — Is There Just a File? + Write a Header
# Sadece Dosya Var mı? + Header Yaz

import os
import csv

filename = "mini_file_day16_1.csv"

# Dosya var mı ? kontrol et. 
if not os.path.exists(filename):
    print("File doesn't exist. Creating file...")

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score"])

    print("File created with header.")
else:
    print("File already exists.")


# import os' yi neden kullandık ? 
    # özetle ; Dosya sistemini kontrol etmek için. çünkü os modlü python'a işletim sistemi ilek onuşmayı sağlar.
    # çünkü dosya var mı yok mu kontrol etmek istedik. bunun için kullandık. aslıdda şu satır için:  os.path.exists(filename)
        # burada ne yaptık. işletim sistemine sorduk.  "Bu isimde bir dosya fiziksel olarak var mı?"
        # işletim sistemi bize True / False döndü.
    # peki neden önce dosyayı var mı diye kontrol ettik. 
        # çünkü "w" modu çok tehlikeli.   with open(filename, "w"
        # eğer dosya varsa içeriğini siler. 
        # peki biz ne istedik ? dosya yoksa oluştur ama varsa silme. bu yüzden önce şu konutla sorduk. if not os.path.exists(filename):

#  os.path.exists(filename)  ==> mini_file_day16_1.csv  isimli dosya var mı yok mu kontrol etti. 
#  "w"  modu :  Dosya yoksa oluşturur. dosya varsa içini siler tekrar yazar. 

#  dosya modlarını yazalım
    # "w"  Var olanı siler, baştan yazar.
    # "a"  Var olanın sonuna ekler.
    # "r"  Sadece okur
    # "x"  Dosya varsa hata verir. (“Ben sadece yeni dosya oluştururum. Var olan dosyaya dokunmam.”)


# writerow  ne yapar ? 
    # Listenin elemanlarını alır
    # Aralarına virgül koyar
    # Özel karakter varsa (örneğin virgül içeriyorsa) otomatik tırnaklar
    # Satır sonuna \n ekler

# writerows() → liste içinde birden fazla satır
    # writer.writerows([ ["Ali", 80], ["Veli", 90] ])