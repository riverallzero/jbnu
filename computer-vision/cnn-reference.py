import cv2 as cv
import numpy as np
import tensorflow as tf
import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

cnn = tf.keras.models.load_model('./weights/VGG16.h5')  # 모델 읽기
apple_disease = pickle.load(open('trains/apple_disease_types.txt', 'rb'))  # 질병 이름

class ModelReferencing(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사과 잎 질병 분류')
        self.setGeometry(200, 200, 800, 400)

        self.initUI()

    def initUI(self):
        # 전체 레이아웃 설정
        self.mainLayout = QHBoxLayout()

        # 왼쪽 레이아웃에 이미지 표시
        leftLayout = QVBoxLayout()
        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        leftLayout.addWidget(self.imageLabel)
        leftLayout.addStretch(1)
        self.mainLayout.addLayout(leftLayout)

        # 오른쪽 레이아웃에 버튼과 결과 표시
        rightLayout = QVBoxLayout()

        self.fileButton = QPushButton('이미지 업로드', self)
        self.recognitionButton = QPushButton('추론', self)
        self.quitButton = QPushButton('나가기', self)
        self.resultLabel = QLabel('결과:', self)
        self.resultLabel.setAlignment(Qt.AlignTop)

        rightLayout.addWidget(self.fileButton)
        rightLayout.addWidget(self.recognitionButton)
        rightLayout.addWidget(self.quitButton)
        rightLayout.addWidget(self.resultLabel)
        rightLayout.addStretch(1)

        self.mainLayout.addLayout(rightLayout)

        # QWidget을 만들어서 중앙 위젯으로 설정
        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

        # 버튼 연결
        self.fileButton.clicked.connect(self.pictureOpenFunction)
        self.recognitionButton.clicked.connect(self.recognitionFunction)
        self.quitButton.clicked.connect(self.quitFunction)

    def pictureOpenFunction(self):
        fname, _ = QFileDialog.getOpenFileName(self, '이미지 읽기', './')
        if fname:
            self.img = cv.imread(fname)
            if self.img is None:
                sys.exit('파일을 찾을 수 없습니다.')

            self.displayImage(self.img, self.imageLabel)

    def displayImage(self, img, label):
        rgbImage = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        h, w, ch = rgbImage.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(400, 400, Qt.KeepAspectRatio)
        label.setPixmap(QPixmap.fromImage(p))

    def recognitionFunction(self):
        if hasattr(self, 'img'):
            x = np.reshape(cv.resize(self.img, (224, 224)), (1, 224, 224, 3))
            res = cnn.predict(x)[0]  # 예측값
            top4 = np.argsort(-res)[:4]
            top4_disease_names = [apple_disease[i] for i in top4]

            resultText = f'예측 결과: {top4_disease_names[0]}\n'

            resultText += '\n'
            resultText += '각 클래스에 대한 확률\n'
            for i in range(4):
                prob = f'{round(res[top4[i]] * 100, 3)}'
                name = top4_disease_names[i]
                resultText += f' - {name} = {prob}%\n'

            self.resultLabel.setText(resultText)
            self.displayImage(self.img, self.imageLabel)
        else:
            self.resultLabel.setText('이미지를 먼저 업로드하세요.')

    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = ModelReferencing()
win.show()
app.exec_()

