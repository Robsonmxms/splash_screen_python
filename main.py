import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, 
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
)
from PySide2.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, 
    QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
)
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow

def main():
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

class SplashScreen(QMainWindow):
    counter = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.interface()

    def interface(self):
        self.setTitle("<strong>YOUR</strong> APPLICATION")
        self.setCredits("<strong>Created by:</strong> Robson Lima Lopes")
        self.__removeTitleBar()
        self.__dropShadowEffect()
        self.__startQTimerInMilliseconds()
        self.__changeDescription()
        self.show()
    
    def setTitle(self, title):
        self.ui.label_title.setText(title)
    
    def setCredits(self, credits):
        self.ui.label_credits.setText(credits)

    def __removeTitleBar(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def __dropShadowEffect(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

    def __startQTimerInMilliseconds(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.__progress)
       
        self.timer.start(50)

    def __changeDescription(self):
        QtCore.QTimer.singleShot(
            0,
            lambda: self.ui.label_description
            .setText("<strong>LOADING</strong> DATABASE")
        )
        QtCore.QTimer.singleShot(
            4000, 
            lambda: self.ui.label_description
            .setText("<strong>LOADING</strong> DATABASE")
        )
        QtCore.QTimer.singleShot(
            8000, 
            lambda: self.ui.label_description
            .setText("<strong>LOADING</strong> USER INTERFACE")
        )
        
    def __progress(self):
        self.ui.progressBar.setValue(self.counter)

        if self.counter > 100:
            self.__isFinished()
            
        self.counter += 1
    
    def __isFinished(self):
        self.timer.stop()
        self.__showMainWindow()
        self.close()
    
    def __showMainWindow(self):
        self.main = MainWindow()
        self.main.show()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    main()
