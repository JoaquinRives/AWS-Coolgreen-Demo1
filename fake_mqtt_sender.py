"""
Fake simulated device to check the AWS IoT MQTT rules and Sitewise assets.
"""
import boto3
import json
import time
import numpy as np

# AWS profile
ses = boto3.session.Session(profile_name='coolgreen')

# resource
client = ses.client('iot-data', region_name='eu-west-1')

# sn: dc97e9fb-3f64-4534-8a7e-34ac4132b681
# zone: 61a5a3a5-ee77-4f85-ad6a-29d926fb6db2
# site: 22cecfa0-db40-4a4b-a22f-ff22c1f9a381

gw_id = "gw00000"
sn_id = "sn00001"
as_id = "as00002"

# examples payloads
msg_AssetSensor = {"Acceleration":{"Y":-53,"X":10,"Z":-1150},"SourceAddress":"7925763","SensorNodeId":as_id,
                   "Timestamp":1605965859,"GatewayId":"66666gw","Type":"scalar","Movement":4}

msg_SensorNodeAC_routine = {"Temperature":24,"Humidity":35.49,"CO2Index":500,"IAQaccuracy":0,"Ambient_light":0,
                            "SensorNodeId":sn_id,"Pressure":1007,"SourceAddress":"2307893","Timestamp":1606193592,
                            "GatewayId":gw_id,"BatteryLevel":0,"Type":"scalar","AirQuality":25,"Movement":4}

msg_SensorNodeAC_movement = {"SourceAddress":"2307893","SensorNodeId":sn_id,"Timestamp":1606059682,
                             "GatewayId":gw_id,"Type":"scalar","Movement":4}

messages = [msg_AssetSensor, msg_SensorNodeAC_routine, msg_SensorNodeAC_movement]
# messages = [msg_SensorNodeAC_routine, msg_SensorNodeAC_movement]

while True:
    for payload in messages:

        payload['Timestamp'] = int(time.time())
        if 'Temperature' in payload.keys():
            if payload['SensorNodeId'] == sn_id:
                payload['Temperature'] = np.random.randint(0, 50) + np.random.rand()
            else:
                payload['Temperature'] = np.random.randint(60, 100) + np.random.rand()

        if 'Humidity' in payload.keys():
            if payload['SensorNodeId'] == sn_id:
                payload['Humidity'] = np.random.randint(100, 200) + np.random.rand()
            else:
                payload['Humidity'] = np.random.randint(200, 300) + np.random.rand()

        if 'Acceleration' in payload.keys():
            payload['Acceleration']['X'] = np.random.randint(-1, 3) + np.random.rand()
            payload['Acceleration']['Y'] = np.random.randint(-1, 3) + np.random.rand()
            payload['Acceleration']['Z'] = np.random.randint(-1, 3) + np.random.rand()

        if 'Movement' in payload.keys():
            payload['Movement'] = np.random.choice(['0', '0', '4'])

        response = client.publish(
                topic=f"treon/devices/{gw_id}",
                payload=json.dumps(payload)
            )
        statusCode = response['ResponseMetadata']['HTTPStatusCode']
        print(f"--- ERROR: {statusCode} ----" if statusCode != 200 else f" {statusCode} Ok!")
        time.sleep(5)
