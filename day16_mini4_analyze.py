# Mini Proje 4: Okuma + Dönüşüm + Basit Analiz.

# Hedef: mini_test.csv dosyasındaki skorları okuyup aşağıdaki değerleri bulacağız...:
#     toplam kayıt sayısı
#     en yüksek skor
#     en düşük skor
#     ortalama skor
#     en iyi kişiyi

import csv

filename = "mini_file_day16_2.csv"

scores = []
rows = []

with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)       # csv dosyamızın başlıklarını okuyoruz.

    for row in reader:
        name = row["name"].strip()
        score_text = row["score"].strip()

        # score boş ise atla
        if score_text == "":
            continue

        score = int(score_text)

        rows.append({"name" : name, "score": score})
        scores.append(score)
    
    if not rows:
        print("No Valid data to analyze.")
    else:
        best_row = max(rows, key=lambda r: r["score"])

        print("\n--- Analysis ---")
        print(f"rows :{rows}")
        print(f"Scores : {scores}")
        print(f"Total Records : {len(rows)}")
        print(f"Max Score :{max(scores)}")
        print(f"Min Score :{min(scores)}")
        print(f"Average Score :{sum(scores) / len(scores):.2f}")
        print(f"Top Performer :{best_row["name"]} ({best_row["score"]})")