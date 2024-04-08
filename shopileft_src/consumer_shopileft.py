from confluent_kafka import Consumer
from utils.conflu_config import read_config
from utils.confluent_data_loader import create_insert_data_, get_conn
import json
import os
from sqlalchemy.pool import QueuePool


user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
table_name_transaction = os.getenv('SNOWFLAKE_TABLE_TRANSACTION')
table_name_analytical = os.getenv('SNOWFLAKE_TABLE_ANALYTICAL')

print(f'database {database}')

mypool = QueuePool(
    lambda: get_conn(user, password, account, warehouse, database),
    pool_size=10,
    max_overflow=10,
)

config = read_config()
topic = "idowu_new"
# from snowflake_connect import create_insert_data


def consumer_(topic):
    config["group.id"] = "python-group-1"
    config["auto.offset.reset"] = "earliest"

    # creates a new consumer and subscribes to your topic
    consumer = Consumer(config)
    consumer.subscribe([topic])
    print('running this')
    try:
        while True:
        # consumer polls the topic and prints any incoming messages
            msg = consumer.poll(1.0)
            if msg is not None and msg.error() is None:
                key = msg.key().decode("utf-8")
                print(key)
                # .decode("utf-8")
                # print(msg.value())
                value = json.loads(msg.value()[5:].decode("utf-8").replace("'", '"'))
                print(value)

                print(f"Consumed message from topic {topic}: key = {key:12} value = {value}")
                create_insert_data_(value,table_name_transaction=table_name_transaction,table_name_analytics=table_name_analytical,database_conn=mypool)
                consumer.commit()
            elif msg is not None and msg.error() is not None:
                print(f"Consumer error: {msg.error()}")
                break
    except KeyboardInterrupt:
        pass
    finally:
        # closes the consumer connection
        consumer.close()

consumer_('sample_data')