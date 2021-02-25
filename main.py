import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint

class Example(QWidget):
    def __init__(self):
        super().__init__()  
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Git2')
        self.pushButton = QPushButton(self)
        self.pushButton.move(self.width() // 2, self.height() // 2)
        self.pushButton.clicked.connect(self.draw_bol)
        self.flag = False
        self.show()

    def draw_bol(self):
        self.flag = True
        if self.flag:
            self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        if self.flag:
            x, y, len_ = randint(0, self.width() - 1), randint(0, self.height() - 1), randint(0, self.width() // 2)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, len_, len_)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
