from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys


class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200, 200, 700, 200)

        collectButton = QPushButton('영상 수집', self)
        self.showButton = QPushButton('영상 보기', self)
        self.stitchButton = QPushButton('봉합', self)
        self.saveButton = QPushButton('저장', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)

        collectButton.setGeometry(10, 25, 100, 30)
        self.showButton.setGeometry(110, 25, 100, 30)
        self.stitchButton.setGeometry(210, 25, 100, 30)
        self.saveButton.setGeometry(310, 25, 100, 30)
        quitButton.setGeometry(450, 25, 100, 30)
        self.label.setGeometry(10, 70, 600, 170)

        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)

        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        # 마우스 이벤트 처리를 위한 변수 초기화
        self.drawing = False
        self.pt1 = (0, 0)
        self.pt2 = (0, 0)
        self.rectangles = []

    def collectFunction(self):
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.label.setText('c를 여러 번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')

        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened(): sys.exit('카메라 연결 실패')

        self.imgs = []
        while True:
            ret, frame = self.cap.read()
            if not ret: break

            cv.imshow('video display', frame)

            key = cv.waitKey(1)
            if key == ord('c'):
                self.imgs.append(frame)
            elif key == ord('q'):
                self.cap.release()
                cv.destroyWindow('video display')
                break

        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.saveButton.setEnabled(True)

    # 사각형 그리는 마우스 이벤트
    def mouse_event(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.pt1 = (x, y)
        elif event == cv.EVENT_MOUSEMOVE and self.drawing:
            self.pt2 = (x, y)
            temp_img = self.img_stitched.copy()
            cv.rectangle(temp_img, self.pt1, self.pt2, (0, 255, 0), 2)
            cv.imshow('Image stitched panorama', temp_img)
        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False
            self.pt2 = (x, y)
            self.rectangles.append((self.pt1, self.pt2))

    def showFunction(self):
        self.label.setText('수집된 영상은 ' + str(len(self.imgs)) + '장 입니다.')
        stack = cv.resize(self.imgs[0], dsize=(0, 0), fx=0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            stack = np.hstack((stack, cv.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)))
        cv.imshow('Image collection', stack)

    def stitchFunction(self):
        stitcher = cv.Stitcher_create()
        status, self.img_stitched = stitcher.stitch(self.imgs)
        if status == cv.STITCHER_OK:
            cv.imshow('Image stitched panorama', self.img_stitched)
            cv.setMouseCallback('Image stitched panorama', self.mouse_event)
        else:
            winsound.Beep(3000, 500)
            self.label.setText('파노라마 제작에 실패했습니다. 다시 시도하세요.')

    def saveFunction(self):
        if not self.rectangles:  # 사각형 영역이 없으면 전체 이미지를 저장
            fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
            cv.imwrite(fname[0], self.img_stitched)
        else:
            for rect in self.rectangles:  # 선택한 사각형 영역 저장
                pt1, pt2 = rect
                cropped_img = self.img_stitched[pt1[1]:pt2[1], pt1[0]:pt2[0]]
                fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
                cv.imwrite(fname[0], cropped_img)

    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()


app = QApplication(sys.argv)
win = Panorama()
win.show()
app.exec_()
