import yaml
import serial
import json

class DerinlikSensoru:
    def __init__(self, port='COM5', baudrate=9600):
        """ dev/ttyUSB0 """
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)

    def kontrol(self, value):
        jdata = {}
        if value.strip() == "" or value.isdigit():
            data = 0 if value.strip() == "" else int(value)

            jdata["value"] = data

            if value.strip() == "":
                jdata["msg"] = 'Hazırlanıyor..'
                jdata["status"] = True
            elif data > 25:
                jdata["msg"] = 'Çok derinde'
                jdata["status"] = True
            elif data < 5:
                jdata["msg"] = 'Su içinde değil'
                jdata["status"] = False
            else:
                jdata["msg"] = 'AUV normal'
                jdata["status"] = True
        else:
            jdata["value"] = value
            jdata["msg"] = 'Farklı bir sorun var'
            jdata["status"] = False

        return jdata

    def read_value(self):
        try:

            # with open('./config/sensor_derinlik.yaml', 'r') as file:
            #     derinlikOptions = yaml.safe_load(file)

            # value = self.kontrol(derinlikOptions['value'])

            data = self.ser.readline().decode().strip()

            test = self.kontrol( data )

            return test
        
        except serial.SerialException as e:
            return {
                "value": None, 
                "msg": str(e), 
                "status": False
            }

    def close(self):
        self.ser.close()