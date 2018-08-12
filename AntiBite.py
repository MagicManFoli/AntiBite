import time

import cv2

# define classifier for faces
cascPath = "haarcascade_frontalface_default.xml"  # from openCV folder
faceCascade = cv2.CascadeClassifier(cascPath)  # identification stats
# fingers
# TODO insert

# ---- NOTES -----
# finger detection depends on background subtraction, this is contrary to face detection.
# project is ON HOLD for the time being.

# ---- functions ----


def find_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
        # minSize=(30, 30)
    )
    return faces


def find_fingers(frame):
    # TODO same structure as faces
    return []


def show_detection(frame, faces, fingers):
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # draw other rectangles around fingers
    for (x, y, w, h) in fingers:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Live Video Feed", frame)


# --- main ---
print("Hello to Antibite")
print("Using OpenCV Version: " + cv2.__version__)

print("\nStarting video stream")
video_feed = cv2.VideoCapture(0)

while not video_feed.isOpened():
    print(".", end="")  # print waiting time as increasing number of dots
    time.sleep(0.2)
    # TODO if time > threshold cancel program

print("Video Feed running, starting window output")

cv2.startWindowThread()
cv2.namedWindow("Live Video Feed")

print("Processing in endless loop, exit with <q>")

while True:
    ret_code, frame = video_feed.read()  # ret_code is ignored

    faces = find_faces(frame)
    fingers = find_fingers(frame)

    # TODO check for intersection of both, send warning if true

    show_detection(frame, faces, fingers)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # needed for imshow to work
        break

print("Cleaning up...")
video_feed.release()  # stop blocking webcam
cv2.destroyAllWindows()  # close windows and background thread

print("Done")
