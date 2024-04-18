import subprocess
import time


class KafkaManager:
    def __init__(self, kafka_path):
        self.kafka_path = kafka_path

    def start_zookeeper(self):
        zookeeper_command = f"{self.kafka_path}/bin/zookeeper-server-start.sh {self.kafka_path}/config/zookeeper.properties"
        subprocess.Popen(zookeeper_command, shell=True)
        time.sleep(10)

    def start_kafka(self):
        kafka_command = f"{self.kafka_path}/bin/kafka-server-start.sh {self.kafka_path}/config/server.properties"
        subprocess.Popen(kafka_command, shell=True)
        time.sleep(10)

    def stop_zookeeper(self):
        zookeeper_command = f"{self.kafka_path}/bin/zookeeper-server-stop.sh {self.kafka_path}/config/zookeeper.properties"
        subprocess.Popen(zookeeper_command, shell=True)
        time.sleep(10)

    def stop_kafka(self):
        kafka_command = f"{self.kafka_path}/bin/kafka-server-stop.sh {self.kafka_path}/config/server.properties"
        subprocess.Popen(kafka_command, shell=True)
        time.sleep(10)

    def start(self):
        self.start_zookeeper()
        self.start_kafka()
        print("Zookeeper and Kafka servers started successfully.")

    def stop(self):
        self.stop_kafka()
        self.stop_zookeeper()
        print("Zookeeper and Kafka servers stopped successfully.")


# # Usage:
# kafka_manager = KafkaManager("/home/mohan")
# kafka_manager.start()
# # Do something with Kafka
# kafka_manager.stop()
