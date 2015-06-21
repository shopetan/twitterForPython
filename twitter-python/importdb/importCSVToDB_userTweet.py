import csv
import sys
import sqlite3

db = sqlite3.connect("tweet.db")
db.text_factory = str
cur = db.cursor()


cur.execute(""" create table usertweet (
                id integer,
                name text,
                tweet text)""")


fp = open("usertimeline.csv")

timeline = csv.reader(fp)

i = 0
for row in timeline:
    i += 1
    t = (i, row[0],row[1])
    cur.execute("insert into usertweet values(?,?,?)",t)

db.commit()
db.close()
