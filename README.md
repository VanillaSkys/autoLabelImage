# License Plate Thailand

## Install Yolov5

โหลด Yolov5 จากลิงค์นี้ [Yolov5](https://github.com/ultralytics/yolov5)

## Custom Dataset

หารูปภาพจากนั้นนำมาLabel โดยใช้ [roboflow](https://roboflow.com/)

![Label](https://blog.roboflow.com/content/images/size/w2000/2021/06/label-classification.jpg)

> Trick ส่วนตัว หลังจาก่ที่ Label ไปแล้วTrain model พอที่มันจะรู้เรื่องบ้างแล้ว ก็นำมาใช้ Auto Label จาก [autoLabelImage](https://github.com/VanillaSkys/autoLabelImage) ทำให้ประหยัดเวลาในการ Label 

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

nc: 1  # number of classes

ตามจำนวน Class ของเรา

ไฟล์ yolov5s.yaml มีหลายขนาด

* ylov5n.yaml
* ylov5s.yaml
* ylov5m.yaml
* ylov5l.yaml
* ylov5x.yaml

> ในตัวอย่างจะตั้งเป็นlicense.yaml

---

เข้าใน Anaconda Prompt Download จาก [Anaconda](https://www.anaconda.com/products/distribution)

จากนั้นติดตั้ง pytorch  [pytorch](https://pytorch.org/) เพื่อใช้ cuda ของ GPU จะทำให้เร็วกว่าใช้ CPU มาก

สามารถตรวจสอบรุ่น cuda และข้อมูล GPU ทาง command nvidia-smi

หลังจากติดตั้งเสร็จ ให้เขียนcommand

`python`

`import torch`

`torch.cuda.is_available()`

หากเป็น True คือใช้ Cuda เรียบร้อย

หากเป็น False คือยังไม่ได้ใช้ ให้ติดตั้งใหม่

หากเครื่องเป็น Offline ให้โหลด 3 File [torch](https://download.pytorch.org/whl/torch/) ตามด้วยรุ่น โดยส่วนตัวใช้ torch-1.12.0+cu116-cp310-cp310-win_amd64.whl [torchaudio](https://download.pytorch.org/whl/torchaudio/) torchaudio-0.12.0+cu116-cp310-cp310-win_amd64.whl [torchvision](https://download.pytorch.org/whl/torchvision/) torchvision-0.13.0+cu116-cp310-cp310-win_amd64.whl โดยทั้ง 3 File จะต้องเป็นรุ่นที่ใช้ร่วมกัน

หลังจากโหลดเสร็จให้นำ ใส่Flash drive แล้วนำไปติดตั้ง ในเครื่องOffline โดยพิมพ์ command `pip install [ชื่อไฟล์.whl] -f ./ --no-index`

พิมพ์ command

python train.py --data [File name จากFolder Data] --weights [ขนาดที่ต้องการ] --img 640 --batch [กำหนดbatch ปกติ 16] --epochs [กำหนดจำนวนรอบ]

python train.py --data license.yaml --weights yolov5s.pt --img 640 --batch 16 --epochs 100

> หากมี GPU หลายตัว python train.py --data [File name จากFolder Data] --weights [ขนาดที่ต้องการ] --img 640 --batch [กำหนดbatch ปกติ 16] --epochs [กำหนดจำนวนรอบ] --device [เลขGPU]

> python train.py --data license.yaml --weights yolov5s.pt --img 640 --batch 16 --epochs 100 --device 0,1
