import openpyxl as xls
import pymongo
import json

with open('static/datafile.json', encoding='utf-8') as f:
    datavars = json.load(f)

wb = xls.load_workbook(datavars['workbook'])
ws = wb[datavars['worksheet']]
con = pymongo.MongoClient(host='localhost', port=27017)
db = con.db
collection = db.trashers
r = []
for row in ws.iter_rows(min_row=2):
    adress = row[0].value.replace('\n', ' ')
    d = {
        'address': row[0].value,
        'coords': row[1].value
    }
    c = []
    for i in range(3, 16):
        if row[i].value == 1:
            c.append(i - 2)
    d['types'] = c
    r.append(pymongo.InsertOne(d))
res = collection.bulk_write(r)
con.close()
