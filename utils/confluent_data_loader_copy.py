import snowflake.connector
from sqlalchemy.pool import QueuePool
import json
import os
from datetime import datetime, timezone
user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
table_name = os.getenv('SNOWFLAKE_TABLE')
print(f'database {database}')
# import pandas as pd
# import json
# import time
# import requests
# from datetime import datetime, timezone
def get_conn():
    conn = snowflake.connector.connect(
        user = user,
        password = password,
        account = account,
        warehouse = warehouse,
        database = database,
    )
    return conn

# mypool = QueuePool(
#     get_conn,
#     pool_size=10,
#     max_overflow=10,
#     pool_timeout=30,
# # )
# def create_insert_data(data_dict):

#     con = get_conn()
#     print('Got the Pool Connection')
#     cur = con.cursor()
#     cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")
#     cur.execute(f"""CREATE TABLE IF NOT EXISTS raw.{table_name}
#                     (ordertime INTEGER, orderid INTEGER, itemid string, orderunits float,
#                     city string, state string, zipcode INTEGER, date_inserted INTEGER);""")
#     # cur.execute("INSERT INTO raw.employees VALUES ('John', 'Doe', 32)")
#     time_unix_now = (datetime.now(tz=timezone.utc) - datetime(1970, 1, 1,tzinfo=timezone.utc)).total_seconds()
#     cur.execute(f"""INSERT INTO raw.{table_name} (ordertime, orderid, itemid, orderunits, city, state, zipcode, date_inserted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
#                     (data_dict['ordertime'], data_dict['orderid'], data_dict['itemid'], data_dict['orderunits'], data_dict['address']['city'], data_dict['address']['state'], data_dict['address']['zipcode'], time_unix_now))
#     # cur.execute("""INSERT INTO raw.coincheckrate(transaction_timestamp, transaction_id, pair, transaction_rate, transaction_amount, transaction_order_side, id_of_taker, id_of_maker) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
#     #             (data_dict['transaction_timestamp'], data_dict['transaction_id'], data_dict['pair'], data_dict['transaction_rate'], data_dict['transaction_amount'], data_dict['transaction_order_side'], data_dict['id_of_taker'], data_dict['id_of_maker']))
#     print('done inserting the records')
#     cdc_query = """INSERT INTO raw.orders_shopileft_analytical (ordertime, orderid, itemid, orderunits, city, state, zipcode,date_inserted)
#         SELECT ordertime, orderid, itemid, orderunits, city, state, zipcode, date_inserted
#         FROM raw.orders_shopileft_transaction_stream
#         WHERE METADATA$ACTION = 'INSERT'"""
#     print('about to execute the cdc query')
#     cur.execute(cdc_query)
#     print('done executing the cdc query')
#     con.commit()
#     con.close()
con = get_conn()
print('Got the Pool Connection')
        # rows = cur.fetchall()
        # print(rows)
        # cur.execute("select * from sf.public.employees")
        # rows = cur.fetchall()
# data = 
# {
#   "ordertime": 1507222211524,
# #   "orderid": 677356,
# #   "itemid": "Item_687",
# #   "orderunits": 2.5410999345876273,
# #   "address": {
# #     "city": "City_78",
# #     "state": "State_",
# #     "zipcode": 62384
# #   }
# }

# def read_data(data_dict):
#     return json.dumps(data_dict)


def create_insert_data_(data_dict):
    create_insert_data(data_dict)
