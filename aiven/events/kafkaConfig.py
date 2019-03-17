from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(
    bootstrap_servers="kafka-30b475d9-dhirajkoirala201-9a2d.aivencloud.com:26963",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.crt",
    ssl_keyfile="service.key",
)

'''consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers="kafka-30b475d9-dhirajkoirala201-9a2d.aivencloud.com:26963",
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.crt",
    ssl_keyfile="service.key",
)'''