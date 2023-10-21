import cv2 as cv
import numpy as np
import os

people = ['Danting', 'Hongyu', 'Nnian', 'Yeha', 'YeonyuMilk', 'Yuzi Jiang Fish']
DIR = r'C:\Users\zakin\Documents\GitHub\OpenCV-Learn\Photos\People\Train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    # save the label into a list for each person.
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        # read the image from each person's folder and convert it into a gray scale image.
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # detect the face in the image.
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # show the progress of the training.
            print(f'Processing image {img_path}')

            # crop the face and save it into the features
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # crop the face. y:y+h is the height of the face, x:x+w is the width of the face.
                features.append(faces_roi) # save the face into the features list.
                labels.append(label) # save the label into the labels list. The label is the index of the person in the people list.

create_train()
print('Training done -----------------')
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')
print('-----------------')

# convert the features and labels into numpy array.
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer.
face_recognizer.train(features, labels)

# save the trained model.
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
print('Model saved -----------------')