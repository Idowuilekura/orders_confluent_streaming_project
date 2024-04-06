# from confconfluent_data_loader import get_conn
from utils.conflu_config import read_config
# from utils import confluent_data_loader
from confluent_kafka import Consumer
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
config["group.id"] = "python-group-2"
config["auto.offset.reset"] = "earliest"

def test_consumed_loaded():
    value_produced =  {'ordertime': 1513782772235, 'orderid': 254719, 'itemid': 'Item_499', 'orderunits': 1.73566958346702, 'address': {'city': 'City_86', 'state': 'State_', 'zipcode': 74136}}
    consumer = Consumer(config)


    # consumer.subscribe(['idowu_new'])
    consumer.subscribe(["shopileft_topic_test"])
    msg = consumer.poll(10)
    # key = msg.key().decode("utf-8")
    value_consumed = msg.value().decode("utf-8")
    value_consumed = eval(value_consumed)
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
    assert (value_consumed_order_time == value_produced_order_time) and (value_consumed_order_id == value_produced_order_id)\
        and (value_consumed_item_id == value_produced_item_id) and (value_consumed_order_units == value_produced_order_units)\
        and (value_consumed_address_city == value_produced_address_city) and (value_consumed_address_state == value_produced_address_state)\
        and (value_consumed_address_zipcode == value_produced_address_zipcode)
    # print(key)
    # print(type(value))
    # print(eval(value))
    # consumer.commit()
    

# print(json.loads(msg.value()[5:].decode("utf-8").replace("'", '"')))



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

