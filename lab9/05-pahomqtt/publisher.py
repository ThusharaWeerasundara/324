import sys
import paho.mqtt.client as mqtt
import Task
import json

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def addTask(description):

	taskId = hash(description)

	t = Task.task(description, "OPEN")
	
	jsonStr = json.dumps(t.__dict__)

	infot = client.publish("CO324/addTask", jsonStr, qos=2)

	infot.wait_for_publish()

	return t

def delTask(taskID):

	taskId = str(integer_value)

	infot = client.publish("CO324/delTask", taskId, qos=2)

	infot.wait_for_publish()






client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()

t = Task.task("OPEN", "tes1t")
jsonStr = json.dumps(t.__dict__)

infot = client.publish("CO324/addTask", jsonStr, qos=2)

infot.wait_for_publish()