#### 1
# file = open('dialog.txt')
# lines = list(file)
# file.close()

#### 2
# with open("dialog.txt") as file:
#     lines = list(file)

#### 3
# import csv
# with open("kyoto_restaurants.csv") as file:
#     rows = list(csv.reader(file))
#     print(len(rows))

#### 4
# import csv
# import chardet

# with open("kyoto_restaurants.csv", mode="rb") as file:
#     raw_bytes = file.read()
#     detected_encoding = chardet.detect(raw_bytes)

#### 5
# import csv
# with open("kyoto_restaurants.csv", encoding="utf16") as file:
#     rows = list(csv.reader(file))
#     num_rows = len(rows)
#     first_row = rows[1]
#     print(first_row)

#### 6
# import csv, chardet
# with open("kyoto_restaurants.csv", mode="rb") as file:
#     raw_bytes = file.read(32)
#     encoding_name = chardet.detect(raw_bytes)["encoding"]

# with open("kyoto_restaurants.csv", encoding=encoding_name) as file:
#     rows = list(csv.reader(file))

#### 7
# with open("my_file.txt", mode="w") as file:
#     file.write("first line \n")
#     file.write("second line \n")

#### 8
# with open("append.txt", mode="a") as file:
#     file.write("my line \n")

# with open("append.txt",encoding="UTF-8") as file:
#     lines_appended = list(file)
#     print(lines_appended)

#### 9
import csv
with open("kyoto_restaurants.csv", mode="r", encoding="UTF-16")as file:
    rows = list(csv.reader(file))

with open("kyoto_restaurants_utf8.csv", mode="w", encoding="UTF-8") as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)