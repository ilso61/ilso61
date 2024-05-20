import argparse
import csv
import re

file = input('ВВЕДИТЕ ИМЯ TXT ФАЙЛА\t')
with open(file, 'r', encoding='UTF-8', newline='') as f:
        rows = list(csv.reader(f, delimiter=';'))
for i in range(10):
    print(rows[i])

for i in range(len(rows)):

    rows[i][1] = re.sub('\<[^>]+\>','',rows[i][1])
    rows[i][1] = re.sub("'",'',rows[i][1])
    rows[i][2] = re.sub('\<[^>]+\>','',rows[i][2])
    rows[i][2] = re.sub("'",'',rows[i][2])
for i in range(10):
    print(rows[i])
inserts = list()
for i in range(len(rows)):
    insert = "INSERT INTO [dbo].[Morphemes]([id],[morphs],[morphs_tags])VALUES("+rows[i][0]+",N'"+rows[i][1]+"',N'"+rows[i][2]+"')\nGO\n"
    inserts.append(insert)

f = open("Morphemes.SQL", "w", encoding='UTF-8')
for insert in inserts :
    f.write(insert)
f.close()
