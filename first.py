import cv2


im = cv2.imread('im.jpg')


def main():
    cv2.imshow('display', im)
    k = cv2.waitKey(0)
    if k == ord('s'):
        print('exit')


def webcomcap():
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        print("blocked")
        exit()

    while True:
        ret, frame = capture.read()
        print(ret)


if __name__ == '__main__':
    webcomcap()