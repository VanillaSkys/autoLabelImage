import torch
import numpy as np
import cv2
import os


class ObjectDetection:

    def __init__(self):
        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("\n\nDevice Used:", self.device)

    def load_model(self):
        model = torch.hub.load(
            './yolov5', 'custom', source='local', path='best.pt', force_reload=True)  # change path according to file
        return model

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)

        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label_text(self, x):
        return self.classes[int(x)]

    def class_to_label(self, x):
        return int(x)

    def convert(self, size, box):
        dw = 1./size[0]
        dh = 1./size[1]
        x = (box[0] + box[1])/2.0
        y = (box[2] + box[3])/2.0
        w = box[1] - box[0]
        h = box[3] - box[2]
        x = x*dw
        w = w*dw
        y = y*dh
        h = h*dh
        return (x, y, w, h)

    def plot_boxes(self, results, frame, file):
        # img = np.array(frame)
        original_img = frame.copy()
        (h, w) = frame.shape[:2]
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(
                    row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label_text(labels[i]), (x1, y1),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                classType = self.class_to_label(labels[i])
                license_img = original_img[y1:y2, x1:x2]
                xmin = min(x1, x2)
                xmax = max(x1, x2)
                ymin = min(y1, y2)
                ymax = max(y1, y2)
                box = (xmin, xmax, ymin, ymax)
                yoloX, yoloY, yoloW, yoloH = self.convert((w, h), box)
                text = [str(classType), str(yoloX), str(
                    yoloY), str(yoloW), str(yoloH)]
                cutFile = file[:-4]
                with open(f'./labels/{cutFile}.txt', 'w') as f:
                    f.write('\t'.join(text))
                cv2.imwrite(f'./images/{file}', frame)
                cv2.imwrite(f'./crops/{str(i)+"-"+file}', license_img)
        return frame

    def __call__(self):
        DirPath = '.\input'
        Files = os.listdir(DirPath)
        for file in Files:
            imgPath = os.path.join(DirPath, file)
            frame = cv2.imread(imgPath)
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame, file)


# Create a new object and execute.
detection = ObjectDetection()
detection()
