import cv2

# Corrected RTSP URL
rtsp_url = "rtsp://bradj:7334@192.168.68.54:554/live/ch1"

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Failed to open RTSP stream.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Lost connection to RTSP stream.")
            break
        cv2.imshow('RTSP Stream', frame)
        if cv2.waitKey(1) == 27:  # ESC key to exit
            break

    cap.release()
    cv2.destroyAllWindows()