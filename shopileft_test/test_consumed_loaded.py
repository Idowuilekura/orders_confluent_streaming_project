# from confconfluent_data_loader import get_conn
from sqlalchemy.pool import QueuePool
from snowflake.sqlalchemy import URL
import pandas as pd
from utils.conflu_config import read_config
from utils.confluent_data_loader import create_insert_data_, get_conn
from confluent_kafka import Consumer
import pytest
import os
import socket
import json
import uuid
config = {
    "bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS_TEST"),
    "client.id": uuid.uuid4(),
    "security.protocol": os.getenv("SECURITY_PROTOCOL_TEST"),
    "sasl.mechanisms": os.getenv("SASL_MECHANISMS_TEST"),
    "sasl.username": os.getenv("SASL_USERNAME_TEST"),
    "sasl.password": os.getenv("SASL_PASSWORD_TEST"),
    "session.timeout.ms": 45000
}
config["group.id"] = "python-group-3"
config["auto.offset.reset"] = "earliest"

user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')

mypool = QueuePool(
    lambda: get_conn(user, password, account, warehouse, database),
    pool_size=4,
    max_overflow=5,
)
# table_name_transaction = os.getenv('SNOWFLAKE_TABLE_TRANSACTION')
# table_name_analytical = os.getenv('SNOWFLAKE_TABLE_ANALYTICAL')

print(f'database {user}')
print(f'database {password}')

def test_consumed():
    value_produced =  {'ordertime': 1513782772235, 'orderid': 254719, 'itemid': 'Item_499', 'orderunits': 1.73566958346702, 'address': {'city': 'City_86', 'state': 'State_', 'zipcode': 74136}}
    consumer = Consumer(config)


    # consumer.subscribe(['idowu_new'])
    consumer.subscribe(["shopileft_topic_test"])
    while True:
        msg = consumer.poll(1.0)
        if msg is not None:
            break
    # key = msg.key().decode("utf-8")
    value_consumed = msg.value().decode("utf-8")
    value_consumed = eval(value_consumed)
    # print(value_consumed)
    # print('------------------')
    value_consumed_order_time = value_consumed['ordertime']
    value_consumed_order_id = value_consumed['orderid']
    value_consumed_item_id = value_consumed['itemid']
    value_consumed_order_units = value_consumed['orderunits']
    value_consumed_address_city = value_consumed['address']['city']
    value_consumed_address_state = value_consumed['address']['state']
    value_consumed_address_zipcode = value_consumed['address']['zipcode']
    value_produced_order_time = value_produced['ordertime']
    value_produced_order_id = value_produced['orderid']
    value_produced_item_id = value_produced['itemid']
    value_produced_order_units = value_produced['orderunits']
    value_produced_address_city = value_produced['address']['city']
    value_produced_address_state = value_produced['address']['state']
    value_produced_address_zipcode = value_produced['address']['zipcode']
    consumer.close()
    print(password)
    # con = get_conn(user, password, account, warehouse, database)
   
    # value_consumed = test_consumed()
    print(value_consumed)
    create_insert_data_(value_consumed,'order_shopileft_transaction_test', 'order_shopileft_analytics_test', mypool)
    assert (value_consumed_order_time == value_produced_order_time) and (value_consumed_order_id == value_produced_order_id)\
        and (value_consumed_item_id == value_produced_item_id) and (value_consumed_order_units == value_produced_order_units)\
        and (value_consumed_address_city == value_produced_address_city) and (value_consumed_address_state == value_produced_address_state)\
        and (value_consumed_address_zipcode == value_produced_address_zipcode)
    # print(key)
    # print(type(value))
    # print(eval(value))
    # consumer.commit()
    

# print(json.loads(msg.value()[5:].decode("utf-8").replace("'", '"')))

def test_loaded():
    # snowflake_engine = create_engine(URL(
    #     user=user,
    #     password=password,
    #     account=account,
    #     warehouse=warehouse,
    #     database=database))
    # con = get_conn(user, password, account, warehouse, database)
    con = mypool.connect()
    cur = con.cursor()
    dat_retrieved = cur.execute('select * from raw.order_shopileft_analytics_test')
    data_test = dat_retrieved.fetchall()
    data_df = pd.DataFrame(data_test)
    cur.execute("""DELETE FROM raw.order_shopileft_analytics_test WHERE 1=1;""")
    cur.execute("""DELETE FROM raw.order_shopileft_transaction_test WHERE 1=1;""") 
    con.commit()
    con.close()
    print(data_df)
    assert len(data_df) == 1
    




# test_consumed()
# test_loaded()

# try:
#     while True:
#         msg = consumer.poll(1.0)
#         if msg is None:
#             continue
#         if msg.error():
#             print("Consumer error: {}".format(msg.error()))
#             continue
#         print('Received message: {}'.format(msg.value().decode('utf-8')))
# except KeyboardInterrupt:
#     pass
# finally:
#     consumer.close()

