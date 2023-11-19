import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPixmap, QColor, QPen, QBrush
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)

        self.label.setPixmap(QPixmap(800, 600))
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.label.setPixmap(QPixmap(800, 600))
        x, y = [randint(5, 500) for i in range(2)]
        r = randint(5, 300)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

        pen = QPen(QColor(color))
        pen.setWidth(3)
        brush = QBrush(color)
        painter = QPainter(self.label.pixmap())
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawEllipse(x, y, r, r)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())()
