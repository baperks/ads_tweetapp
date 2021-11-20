import pandas as pd
import sqlite3 as sql

conn = sql.connect('data/tweets.db')

twits = pd.read_sql('SELECT COUNT(DISTINCT(ID)) AS num_tweets FROM tweets ORDER BY created_at DESC', conn)

twits2 = pd.read_sql('SELECT ID, text FROM tweets ORDER BY created_at DESC LIMIT 20', conn)

print(twits)
print(twits2)