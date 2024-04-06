from utils.conflu_config import read_config
import json
from utils.confluent_data_loader import create_insert_data_

config = read_config()
topic = "idowu_new"
# from snowflake_connect import create_insert_data
from confluent_kafka import Consumer

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
                create_insert_data_(value)
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