import pandas as pd
import sqlite3 as sql

conn = sql.connect('data/tweets.db')

twits = pd.read_sql('SELECT COUNT(DISTINCT(ID)) AS num_tweets FROM tweets ORDER BY created_at DESC', conn)

twits2 = pd.read_sql('SELECT * FROM tweets ORDER BY created_at DESC LIMIT 10', conn)

latest = pd.read_sql('SELECT ID, MIN(created_at) AS min, MAX(created_at) AS max FROM tweets', conn)

print(twits)
print(twits2)
print(latest)