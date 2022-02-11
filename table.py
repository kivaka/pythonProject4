import json
import sqlite3
from movi_json import json_f
conn = sqlite3.connect("viva.db")
cursor = conn.cursor()
json_f()
# conn.execute("""CREATE TABLE mov (
#         id integer,
#         name_film text,
#         mark integer,
#         year integer,
#         genre text,
#         countries text)
#     """)
with open("movi.json", "r", encoding="utf-8") as movi:
    x = json.load(movi)
    for i in x:

        print(type((i["countries"])))
        cursor.execute("INSERT INTO mov VALUES (?,?,?,?,?,?)", (i["id"],i["name_film"],i["mark"],i["year"],(''.join(i["genre"])),''.join(i["countries"])))
        print("record added")












movi.close()
conn.commit()
conn.close()