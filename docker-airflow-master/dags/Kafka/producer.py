from kafka import KafkaProducer
from json import dumps
import requests
# from zookeeper_and_kafka_manager import KafkaManager
from datetime import datetime
import time

def get_api_data():
    response = requests.get("https://api.quotable.io/quotes/random")
    data = response.json()
    # return [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data]
    return data

def main():

    my_producer = KafkaProducer(bootstrap_servers=['192.168.0.119:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
    end_time = time.time()+60
    while end_time >= time.time():
        data = get_api_data()
        print(data)
        my_producer.send(topic='quotes',value=data)
        time.sleep(2)

if __name__ == '__main__':
    # kafka_manager = KafkaManager("/home/mohan/kafka")
    # kafka_manager.start()
    main()
    # kafka_manager.stop()