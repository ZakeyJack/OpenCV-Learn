import cv2 as cv

def rescaleFrame(frame, scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Read a video
# capture = cv.VideoCapture('Videos/ruas_jalan.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, 0.5)
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break
# capture.release()
# cv.destroyAllWindows()
# cv.waitKey(0)

# Read an image
img = cv.imread('Photos/cantikku_5.jpg')
resized_image = rescaleFrame(img, 0.1)
cv.imshow('Gambar', img)
cv.imshow('Gambar Resized', resized_image)
cv.waitKey(0)