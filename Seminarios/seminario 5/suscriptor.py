import paho.mqtt.client as mqtt
import time

def mostrar_mensaje(client,userdata,message):
    print('Evento recibido: {}'.format(str(message.payload.decode('utf-8' ))))
    print("Tema: {}".format(message.topic()))




client=mqtt.Client('Suscriptor')
client.on_message = mostrar_mensaje
client.connect('localhost',2000)



client.loop_start()

client.subscribe('universidad/andalucia/uca')
time.sleep(120)

client.loop_stop()
