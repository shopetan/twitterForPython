import csv
import sys
import sqlite3

db = sqlite3.connect("tweet.db")
db.text_factory = str
cur = db.cursor()


cur.execute(""" create table tweet (
                id integer,
                name text,
                tweet text)""")


fp = open("timeline.csv")

timeline = csv.reader(fp)

i = 0
for row in timeline:
    i += 1
    t = (i, row[0],row[1])
    cur.execute("insert into tweet values(?,?,?)",t)

db.commit()
db.close()
