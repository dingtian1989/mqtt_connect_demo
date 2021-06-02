# -*- coding: utf-8 -*-#

# ----------------------------------------------------------
# @Author:       dingtian
# @Email:        dingtian1989@outlook.com
# ----------------------------------------------------------

import paho.mqtt.client as mqtt
import random
import string
import time

host, port = '127.0.0.1', 1883


username = r'admin'
password = 'Test1234'


def on_connect(client, userdata, flags, rc):
    # print("Connected with result code " + str(rc))
    client.subscribe('Test/test')


def on_message(client, userdata, msg):
    print(
        f'Get 1 msg, its topic is {msg.topic}, its payload is {msg.payload}, its qos is {msg.qos}'
    )


def _conn():
    client_id = 'TEST_AUTO_'+ ''.join(random.sample(string.ascii_letters + string.digits, 32))
    client = mqtt.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    # print('Try to connect to mqtt server ...')
    # print(
    #     f'server: {host}:{port}\nclient_id: {client_id}\nusername: {username}\npassword: {password}'
    # )
    client.connect(host, port, keepalive=20)

    # client.loop_forever()

    # while 1:
    #     pass

    client.loop_start()
    time.sleep(30)
    client.loop_stop()

if __name__ == '__main__':
    from threading import Thread, enumerate

    th_list = []
    for _ in range(10):
        th_list.append(Thread(target=_conn))
    
    for th in th_list:
        th.start()
    
    # for th in th_list:
    #     th.join()

    print(len(enumerate()))
    time.sleep(30)
    