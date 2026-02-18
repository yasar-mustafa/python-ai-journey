# csv_read
# CSV Reading & Analysis
# Yesterday we wrote to a CSV.
# Today we will read the CSV.
# This is now a mini data analysis.

import csv

def read_csv_data():
    data = []
    try:
        with open("study_hours.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                name = row[0]
                total = float(row[1])
                average = float(row[2])
                data.append((name, total, average))
    except FileNotFoundError:
        print("No CSV file found !")
    return data

records = read_csv_data()

if not records:
    print("No data to analyze !")
else:
    print("\n--- CSV Analysis ---")

    totals   = [record[1] for record in records]
    averages = [record[2] for record in records]

    print(f"Number of records :{len(records)}")
    print(f"Best Total Hours  :{max(totals)}")
    print(f"Highest Average   :{max(averages)}")

    best_student = max(records, key=lambda x: x[2])
    print(f"Top Performer : {best_student[0]} with avg {best_student[2]:.2f}")


# What We Learned Today
    # csv.reader
    # row[0], row[1], row[2]
    # list comprehension
    # lambda
    # key parameter
    # real data analysis