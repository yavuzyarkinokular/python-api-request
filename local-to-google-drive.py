# Google Driver Uploader

# Packages
import json
import requests
import random

push_to_data = input("Dosya yolunu dosyayı seçerek giriniz:")
dosya_adi = input("Dosya adı kaç basamaklı olmalı:")
dosyaAd = "yarkin"
my_Data = "123456789"
for i in range(0, dosya_adi):
    secilmiskisi = random.choices(my_Data)
    ready_to_exit = dosyaAd + str(secilmiskisi)

headers = {
    "Authorization": "Bearer apı_key"
}
para = {
    "name": ready_to_exit,
}
files = {
    "data": ("metadata", json.dumps(para), "application/json; charset=UTF-8"),
    "file": open(push_to_data, "rb"),
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files,
)
print(r.text)
