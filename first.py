import cv2


im = cv2.imread('im.jpg')


def main():
    cv2.imshow('display', im)
    k = cv2.waitKey(0)
    if k == ord('s'):
        print('exit')


def webcomcap():
    if not cap.isOpened():
        print("blocked")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('webcam', frame)
        k = cv2.waitKey(0)
        if k == ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()


def webcam_video():
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if cv2.waitKey(1) & 0xFF == 27:
            break
        cv2.imshow('frame', frame)
        out.write(frame)
    out.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('captured.wmv', codec, 25.0, (640, 480))
    webcam_video()
