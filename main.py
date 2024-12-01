import sys
from random import randint

from circles_widget import Ui_Form
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QApplication


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            r = randint(1, self.height() // 2)
            x, y = randint(r, self.width() - r), randint(r, self.height() - r)
            qp.drawEllipse(QPoint(x, y), r, r)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
