import csv

db_file = "./db/mobile_db.csv"

fields = []
rows = []

with open(db_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    fields = next(reader)
    for i in reader:
        rows.append(i)
    print("Total rows in db: ", reader.line_num)
