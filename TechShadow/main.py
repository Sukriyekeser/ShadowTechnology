import load
from script.yardimci_fonksiyonlar import read_sensor_data
from sensor.derinlik import DerinlikSensoru
import cv2
import threading
import yaml
import json

def main():
    derinlik_sensoru = DerinlikSensoru()

    # yolo_detector = NesneTespit("model/...")

    # with open('config/auv_options.yaml', 'r') as file:
    #     auv_options = yaml.safe_load(file)

    while True:

        #d_degeri = read_sensor_data(derinlik_sensoru)

        deger = derinlik_sensoru.read_value();

        if deger["status"]:
            print(f"Derinlik Değeri: {deger['value']} - {deger['msg']}")
        else:
            print(f"Derinlik Değeri: {deger['value']} - {deger['msg']}")
            break

        """
        Örnek Sıralama.. 

        Güvenlik (Suyun içinde mi, Sıcaklık seviyeleri, sensör sorunları)
            PID (AUV suyun içinde mi, dengede mi, düz mü) [Motor Kontrol]
                Görev Durum (Görev tespit, Görevler bitti mi, Geri dön)
                    Kamera (Veri al)
                        Nesne Tespit (Veri işle, yön bul)
                            Motor Kontrol (Harket et, dur, dengele) [PID]


        Kameradan alınan görüntüyü yolo kütüphanesinde işleyip, x,y koordinat verisini alıp motor kontrol sınıfında yönetilecek.
        frame = camera.get_frame()
        if frame is not None:
            detections = yolo_detector.detect(frame)

            ... motor kontrol..
        else:
            print("Kamera görüntüsü okunamadı.")
            break
        
        """

        # -------------------

        # p_degeri = read_sensor_data(pusula_sensoru)
        # b_degeri = read_sensor_data(basinc_sensoru)
        # d_degeri = read_sensor_data(derinlik_sensoru)

        # # -------------------

        # print(f"Pusula Değeri: {p_degeri}")
        # print(f"Basınç Değeri: {b_degeri}")
        # print(f"Derinlik Değeri: {d_degeri}")

        # # -------------------

        # # Kamera görüntüsü al
        # frame = camera.get_frame()

        # # Nesneleri tespit et
        # objects, coordinates = nesne_tespit.detect_objects(frame)

        # # Motorları kontrol et
        # motor_kontrol.adjust_motors(objects, coordinates)

        # # -------------------

        # if d_degeri > auv_options['sensör_ayarlari']['derinlik_hassasiyeti']:
        #     print("Derinlik yüksek")
        # else:
        #     print("Derinlik iyi durumda")

if __name__ == '__main__':
    main()
