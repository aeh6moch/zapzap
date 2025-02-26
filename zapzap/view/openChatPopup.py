from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/openChatPopup.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OpenChatPopup(object):
    def setupUi(self, OpenChatPopup):
        OpenChatPopup.setObjectName("OpenChatPopup")
        OpenChatPopup.resize(466, 263)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenChatPopup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.popupMargins = QtWidgets.QFrame(parent=OpenChatPopup)
        self.popupMargins.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.popupMargins.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.popupMargins.setObjectName("popupMargins")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.popupMargins)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.popupFrame = QtWidgets.QFrame(parent=self.popupMargins)
        self.popupFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.popupFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.popupFrame.setObjectName("popupFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.popupFrame)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.popupFrame)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.popupFrame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.numberPhone = QtWidgets.QLineEdit(parent=self.popupFrame)
        self.numberPhone.setInputMask("00000000000000000000000")
        self.numberPhone.setObjectName("numberPhone")
        self.verticalLayout_2.addWidget(self.numberPhone)
        self.btnPhoneHelper = QtWidgets.QPushButton(parent=self.popupFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnPhoneHelper.setFont(font)
        self.btnPhoneHelper.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WhatsThisCursor))
        self.btnPhoneHelper.setStatusTip("")
        self.btnPhoneHelper.setObjectName("btnPhoneHelper")
        self.verticalLayout_2.addWidget(self.btnPhoneHelper)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCancel = QtWidgets.QPushButton(parent=self.popupFrame)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnOk = QtWidgets.QPushButton(parent=self.popupFrame)
        self.btnOk.setShortcut("Enter")
        self.btnOk.setAutoDefault(False)
        self.btnOk.setDefault(False)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.popupFrame)
        self.verticalLayout.addWidget(self.popupMargins)

        self.retranslateUi(OpenChatPopup)
        QtCore.QMetaObject.connectSlotsByName(OpenChatPopup)

    def retranslateUi(self, OpenChatPopup):
        
        OpenChatPopup.setWindowTitle(_("Form"))
        self.label_4.setText(_("Open chat by phone number"))
        self.label.setText(_("Enter phone number:"))
        self.btnPhoneHelper.setToolTip(_("See here the code of your country"))
        self.btnPhoneHelper.setText(_("(COUNTY CODE + AREA CODE + PHONE NUMER)"))
        self.btnCancel.setText(_("Cancel"))
        self.btnOk.setText(_("Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenChatPopup = QtWidgets.QWidget()
    ui = Ui_OpenChatPopup()
    ui.setupUi(OpenChatPopup)
    OpenChatPopup.show()
    sys.exit(app.exec())
