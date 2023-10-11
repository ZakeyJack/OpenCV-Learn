import cv2

# Read an image
# img = cv2.imread('Photos/cantikku_0.JPG')
# cv2.imshow("Gambar", img)
# cv2.waitKey(0)

# Read a video
capture = cv2.VideoCapture('Videos/ruas_jalan.mp4')
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv2.destroyAllWindows()