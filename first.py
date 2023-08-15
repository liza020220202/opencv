import cv2


im = cv2.imread('im.jpg')


def main():
    cv2.imshow('display', im)
    k = cv2.waitKey(0)
    if k == ord('s'):
        print('exit')


if __name__ == '__main__':
    main()