# License Plate Thailand

## Install Yolov5

โหลด Yolov5 จากลิงค์นี้ [Yolov5](https://github.com/ultralytics/yolov5)

## Custom Dataset

หารูปภาพจากนั้นนำมาLabel โดยใช้ [roboflow](https://roboflow.com/)

![Label](https://blog.roboflow.com/content/images/size/w2000/2021/06/label-classification.jpg)

## Train Model

หลังจาก Export File ที่ Label เป็น File Yolov5 จะได้ Folder และ File

* Images
* Labels
* data.yaml

Copyไฟล์ yolov5/data/coco.yaml และ แก้ไขเป็น

train: ใส้Path train  # train images (relative to 'path') 118287 images

val: ใส่Path val  # val images (relative to 'path') 5000 images

names:

ใส้เลขindex และตามด้วย ชื่อ Class เช่น

  0: license

---

Copyไฟล์ yolov5/models/yolov5s.yaml และ แก้ไขในส่วน

> nc: 1  # number of classes

> ตามจำนวน Class ของเรา

> ไฟล์ yolov5s.yaml มีหลายขนาด

> * ylov5n.yaml
> * ylov5s.yaml
> * ylov5m.yaml
> * ylov5l.yaml
> * ylov5x.yaml

---

เข้าใน Terminal พิมพ์ command

python train.py --data [File name จากFolder Data] --weights [ขนาดที่ต้องการ] --img 640 --batch [กำหนดbatch ปกติ 16] --epochs [กำหนดจำนวนรอบ]

python train.py --data license.yaml --weights yolov5s.pt --img 640 --batch 16 --epochs 100

