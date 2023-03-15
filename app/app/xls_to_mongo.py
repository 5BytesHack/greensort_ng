import openpyxl as xls
import pymongo


def main():
    wb = xls.load_workbook("app/finishe(8).xlsm")
    ws = wb["Лист1"]
    con = pymongo.MongoClient(host='mongo', port=27017)
    db = con.db
    collection = db.trashers
    r = []
    for row in ws.iter_rows(min_row=2):
        address = row[0].value.replace('\n', ' ')
        d = {
            'address': address,
            'coords': row[1].value
        }
        c = []
        for i in range(3, 16):
            if row[i].value == 1:
                c.append(i - 2)
        d['types'] = c
        r.append(pymongo.InsertOne(d))
    collection.bulk_write(r)
    con.close()


if __name__ == '__main__':
    main()
