from confluent_kafka import Producer 
import os
import socket
import logging 
from shopileft_test.read_logging import read_log
import pytest 
# import read_logging
import json
config = {
    "bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS_TEST"),
    "client.id": socket.gethostname(),
    "security.protocol": os.getenv("SECURITY_PROTOCOL_TEST"),
    "sasl.mechanisms": os.getenv("SASL_MECHANISMS_TEST"),
    "sasl.username": os.getenv("SASL_USERNAME_TEST"),
    "sasl.password": os.getenv("SASL_PASSWORD_TEST"),
    "session.timeout.ms": 45000
}
# config["group.id"] = "python-group-1"
# config["auto.offset.reset"] = "earliest"

def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
            logging.basicConfig(filename='shopileft_producer_error.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', force=True)
            logging.info('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic test_jokes {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
            logging.basicConfig(filename='shopileft_producer_success.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',force=True)
            logging.info("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

# producer = Producer(config)

# value =  {'ordertime': 1513782772235, 'orderid': 254719, 'itemid': 'Item_499', 'orderunits': 1.73566958346702, 'address': {'city': 'City_86', 'state': 'State_', 'zipcode': 74136}}

# producer.produce("shopileft_topic_test", key='key_1', value=str(value), callback=delivery_callback)

# producer.poll(0)
# producer.flush()
# print('hello')


def test_loaded():
    """
    Test the loaded data by comparing the values from the log file with the expected values.
    """
    producer = Producer(config)

    value =  {'ordertime': 1513782772235, 'orderid': 254719, 'itemid': 'Item_499', 'orderunits': 1.73566958346702, 'address': {'city': 'City_86', 'state': 'State_', 'zipcode': 74136}}

    producer.produce("shopileft_topic_test", key='key_1', value=str(value), callback=delivery_callback)

    producer.poll(1.0)
    # producer.flush()
    try:
        key_log, value_log = read_log('shopileft_producer_error.log')
    except:
        key_log, value_log = read_log('shopileft_producer_success.log')
    # print(key_log)
    # assert key_log == 'key_1'
    value_order_time = value['ordertime']
    value_order_id = value['orderid']
    value_item_id = value['itemid']
    value_order_units = value['orderunits']
    value_address_city = value['address']['city']
    value_address_state = value['address']['state']
    value_address_zipcode = value['address']['zipcode']
    value_log_order_time = value_log['ordertime']
    value_log_order_id = value_log['orderid']
    value_log_item_id = value_log['itemid']
    value_log_order_units = value_log['orderunits']
    value_log_address_city = value_log['address']['city']
    value_log_address_state = value_log['address']['state']
    value_log_address_zipcode = value_log['address']['zipcode']
    assert ((key_log == 'key_1') and (value_order_time == value_log_order_time) \
        and (value_order_id == value_log_order_id) \
            and (value_item_id == value_log_item_id) \
                and (value_order_units == value_log_order_units) \
                    and (value_address_city == value_log_address_city) \
                        and (value_address_state == value_log_address_state) \
                            and (value_address_zipcode == value_log_address_zipcode))



print(test_loaded())



# export BOOTSTRAP_SERVERS='pkc-12576z.us-west2.gcp.confluent.cloud:9092'
# export SECURITY_PROTOCOL='SASL_SSL'
# export SASL_MECHANISMS='PLAIN'
# export SASL_USERNAME='BFK4SFFTA7ZX553I'
# export SASL_PASSWORD='4r95t9NE6O/xLQK9yJyH8cdpDO/Hu2TCJl2SaiNv6OEGtgo3VIti1NqmTIQa63T0'
# export SESSION_TIMEOUT_MS=45000