import paho.mqtt.client as mqtt

client =mqtt.Client('PublicadorUCA')

client.connect('localhost',2000)

topic = 'universidad/andalucia/uca'

client.publish(topic,'Informacion sobre la Uca')
