from PIL import Image
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive
drive.mount('/content/drive')
import os
path='/content/drive/MyDrive/data face'
print(os.listdir(path))
def data(path1):
  paths= [os.path.join(path1,f) for f in os.listdir(path1)]
  faces=[]
  ids=[]
  for p in paths:
    #print(paths) to check value
    image= Image.open(p).convert('L')
    #PIL to numpy array
    image_np= np.array(image,'uint8')
    #splitting logic in copy
    id= int(p.split('.')[1])

    ids.append(id)
    faces.append(image_np)
  return ids,faces
  
ids,faces= data(path)
ids1 = np.array(ids)
classifier= cv2.face.LBPHFaceRecognizer_create(radius=4,neighbors=14,grid_x=9,grid_y=9)
classifier.train(faces,ids1)
classifier.write('/content/drive/MyDrive/face_recognizer.ymnl')
