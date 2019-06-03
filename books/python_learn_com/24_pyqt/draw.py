#! /usr/bin/python

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()
      self.initUI()
		
   def initUI(self):
      self.text = "hello world"
      self.setGeometry(100,100, 600,600)
      self.setWindowTitle('Draw Demo')
      self.show()
		
   def paintEvent(self, event):
      qp = QPainter()
      qp.begin(self)
      qp.setPen(QColor(Qt.red))
      qp.setFont(QFont('Arial', 20))

      qp.drawPixmap(10,10,QPixmap("python.jpg"))
		
      qp.drawText(400,50, "hello Python")
      qp.setPen(QColor(Qt.blue))
      qp.drawLine(0,0,600,600)
      qp.drawRect(350,350,400,400)
		
      qp.setPen(QColor(Qt.yellow))
      qp.drawEllipse(300,300,100,50)
      qp.fillRect(500,500,550,500,QBrush(Qt.SolidPattern))
      qp.end()
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()

