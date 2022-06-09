import requests
import json
import pandas as pd

def try_exc(func,):
    def call_func(*args):
        try:
            conn = psycopg2.connect("dbname=***** user=postgres password=*****")#Вместо звёздочек сваоя база данных.
            conn.autocommit=True
            cur = conn.cursor()
            return func(*args)
        except (Exception) as error:
            print("Ошибка при работе с PostgreSQL", error)
        except MySQLdb.IntegrityError:
            pass
        if conn:
            cur.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")
    return call_func


class market_csgo:

    def __init__(self)-> None:
        self.URL_TEMPLATE='https://market.csgo.com/api/v2/prices/RUB.json'

    def parser(self):
        get_json=requests.get(self.URL_TEMPLATE)
        prices=get_json.json()
        self.data=pd.DataFrame(prices['items'])
        self.data['market_hash_name']=self.data['market_hash_name'].str.replace("'","").replace('\\n','')
        return self.data

    @try_exc
    def sql_insert(self):
        conn = psycopg2.connect("dbname=***** user=postgres password=*****")#Вместо звёздочек сваоя база данных.
        cur = conn.cursor()
        for i in range(len(self.data)):
            update=sql.SQL("UPDATE market_csgo_prices SET name_weapon='{}', volume={}, price={} WHERE name_weapon = '{}';".format(*self.data.loc[i],data_marker.loc[i,'market_hash_name']))
            cur.execute(update)
            conn.commit()
            if load+1<=round(((i/self.data.shape[0]))*100):
                load=round(((i/self.data.shape[0]))*100)
                if round(load/20)==load/20:
                    print(str(load)+'%')
    @try_exc
    def sql_select(self):
        conn = psycopg2.connect("dbname=***** user=postgres password=*****")#Вместо звёздочек сваоя база данных.
        cur = conn.cursor()
        select = """"Select * FROM market_csgo_prices WHERE price != NULL"""
        selt.data=data_marketcur.execute(select)

    def in_excel(self, name='market_db.xlsx', index_f=False):
        self.data.to_excel(name, index=index_f)

    def in_csv(self, name='market_db.csv', index_f=False):
        self.data.to_csv(name, index=index_f)
