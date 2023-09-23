import numpy as np
import cv2 as cv
from tensorflow.keras.models import load_model 


model = load_model('opencv-training/saved_model.h5')
gestures = ['palm', 'l', 'fist', 'fist_moved', 'thumb', 'index', 'ok', 'palm_moved', 'c', 'down']

def predict_gesture(img):
    img = img.reshape(1, 100, 100, 3)
    y_hat = model.predict(img)[0]
    gesture = np.argmax(y_hat, axis=0)
    return gestures[gesture]

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = cv.cvtColor(frame.copy(), cv.COLOR_BGR2RGB)
    resized_frame = cv.resize(img, (100, 100))
    gesture = predict_gesture(resized_frame)
    cv.imshow(gesture, frame)
    cv.waitKey(500)
    cv.destroyAllWindows()
    if 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()