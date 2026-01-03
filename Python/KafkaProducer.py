import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

# Creating the producer function
producer = KafkaProducer(
    bootstrap_servers=['IP Address:9092'],  # change for your IP here
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Reading the CSV file
df = pd.read_csv('us_deaths.csv')

# Sending data to Kafka
try:
    while True:
        dict_stock = df.sample(1).to_dict(orient="records")[0]
        producer.send('kafka_project', value=dict_stock)
        sleep(1)
except KeyboardInterrupt:
    print("Stopped by the user.")
finally:
    # Clean up
    producer.flush()
    producer.close()
    print("Producer closed.")
