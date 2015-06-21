import csv
import sys
import sqlite3

db = sqlite3.connect("tweet.db")
db.text_factory = str
cur = db.cursor()


cur.execute(""" create table timeline (
                id integer,
                name text,
                tweet text)""")


fp = open("timeline.csv")

timeline = csv.reader(fp)

i = 0
for row in timeline:
    i += 1
    t = (i, row[1],row[0])
    cur.execute("insert into timeline values(?,?,?)",t)

db.commit()
db.close()
