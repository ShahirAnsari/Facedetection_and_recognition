# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        AboutUs.setObjectName(_fromUtf8("AboutUs"))
        AboutUs.setEnabled(True)
        AboutUs.resize(400, 286)
        AboutUs.setMouseTracking(True)
        self.frame = QtGui.QFrame(AboutUs)
        self.frame.setGeometry(QtCore.QRect(10, 9, 381, 121))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(5, 10, 101, 101))
        self.label.setMouseTracking(True)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 191, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(-40, 110, 431, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.frame_2 = QtGui.QFrame(AboutUs)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 381, 101))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.line_2 = QtGui.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(0, 80, 401, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 60, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(90, 60, 100, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.okbutton = QtGui.QPushButton(AboutUs)
        self.okbutton.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.okbutton.setObjectName(_fromUtf8("okbutton"))

        self.retranslateUi(AboutUs)
        QtCore.QMetaObject.connectSlotsByName(AboutUs)

    def setlogo(self):
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('smallogo.png')))
        self.label.setScaledContents(False)

    def retranslateUi(self, AboutUs):
        AboutUs.setWindowTitle(_translate("AboutUs", "About Us", None))
        self.label_2.setText(_translate("AboutUs", "Visulization And Analysis Software", None))
        self.label_3.setText(_translate("AboutUs", "Version 1.2.1", None))
        self.label_4.setText(_translate("AboutUs", "Licence   :", None))
        self.label_5.setText(_translate("AboutUs", "Free Version", None))
        self.label_6.setText(_translate("AboutUs", "Email       :", None))
        self.label_7.setText(_translate("AboutUs", "vaas#04@gmail.com", None))
        self.okbutton.setText(_translate("AboutUs", "OK", None))
        self.setlogo()
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AboutUs = QtGui.QWidget()
    ui = Ui_AboutUs()
    ui.setupUi(AboutUs)
    AboutUs.show()
    sys.exit(app.exec_())

