import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor
from UI import UI_Form


class MyWidget(QMainWindow, UI_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.ellips(qp)
            self.do_paint = False
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def ellips(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        rec = randint(0, 300)
        x = randint(0, 300)
        y = randint(0, 300)
        qp.drawEllipse(x, y, rec, rec)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())