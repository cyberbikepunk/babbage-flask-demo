from pandas import read_csv
from babbage_flask_demo import engine


cra = read_csv('cap_or_cur.csv')
cra.to_sql('cap_or_cur', engine, if_exists='replace')
