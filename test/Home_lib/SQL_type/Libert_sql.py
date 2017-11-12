#### SQL DB try ####

import sqlite3

conn = sqlite3.connect('sqldb')


curs = conn.cursor()

tblcmd = '''CREATE TABLE books (
title CHAR(50),
author CHAR(50),
page INT(4),
publisher CHAR(50),
comment CHAR(1000))'''

curs.execute(tblcmd)
