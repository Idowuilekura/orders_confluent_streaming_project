# from confconfluent_data_loader import get_conn
from sqlalchemy.pool import QueuePool
from snowflake.sqlalchemy import URL
import uuid
import pandas as pd
import os
from utils.conflu_config import read_config
from utils.confluent_data_loader import create_insert_data_, get_conn
# from utils.conflu_config import read_config
# from utils.confluent_data_loader import create_insert_data_, get_conn
from confluent_kafka import Consumer
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
print(mypool.connect())

consumer = Consumer(config)


# consumer.subscribe(['idowu_new'])
consumer.subscribe(["shopileft_topic_test"])
value_count = 0
while True:
    msg = consumer.poll(1.0)
    if msg is not None and value_count !=0:
            print(msg)
            value_count += 1
            break
    # table_name_transaction = os.getenv('SNOWFLAKE_TABLE_TRANSACTION')
    # table_name_analytical = os.getenv('SNOWFLAKE_TABLE_ANALYTICAL')
    # create_insert_data_(msg.value(),table_name_transaction=table_name_transaction,table_name_analytics=table_name_analytical,database_conn=mypool)
    consumer.commit()
# msg = consumer.poll(1.0)
# print(msg)
# while True:
#     msg = consumer.poll(1.0)
#     if msg is not None:
#             break
# table_name_transaction = os.getenv('SNOWFLAKE_TABLE_TRANSACTION')
# table_name_analytical = os.getenv('SNOWFLAKE_TABLE_ANALYTICAL')


    
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



