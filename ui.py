# ui.py
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NameLabel(object):

    def setupUi(self, NameLabel):
        NameLabel.setObjectName("NameLabel")
        NameLabel.resize(900, 900)
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(12)
        NameLabel.setFont(font)
        NameLabel.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.GameScreen = QtWidgets.QWidget(NameLabel)
        self.GameScreen.setGeometry(QtCore.QRect(10, 130, 750, 750))
        self.GameScreen.setStyleSheet("background-color: black;\n"
                                      "")
        self.GameScreen.setObjectName("GameScreen")
        self.EndButton = QtWidgets.QPushButton(NameLabel)
        self.EndButton.setGeometry(QtCore.QRect(770, 510, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(24)
        self.EndButton.setFont(font)
        self.EndButton.setMouseTracking(False)
        self.EndButton.setStyleSheet("color: rgb(255, 33, 85);")
        self.EndButton.setObjectName("EndButton")
        self.PauseButton = QtWidgets.QPushButton(NameLabel)
        self.PauseButton.setGeometry(QtCore.QRect(770, 440, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(21)
        self.PauseButton.setFont(font)
        self.PauseButton.setMouseTracking(False)
        self.PauseButton.setStyleSheet("color: rgb(92, 233, 255);")
        self.PauseButton.setObjectName("PauseButton")
        self.CurrentScore = QtWidgets.QLCDNumber(NameLabel)
        self.CurrentScore.setGeometry(QtCore.QRect(770, 660, 121, 51))
        self.CurrentScore.setObjectName("CurrentScore")
        self.CurrentScoreLabel = QtWidgets.QLabel(NameLabel)
        self.CurrentScoreLabel.setGeometry(QtCore.QRect(770, 580, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)
        self.CurrentScoreLabel.setFont(font)
        self.CurrentScoreLabel.setStyleSheet("color: rgb(52, 255, 238);")
        self.CurrentScoreLabel.setObjectName("CurrentScoreLabel")
        self.HighScoreLabel = QtWidgets.QLabel(NameLabel)
        self.HighScoreLabel.setGeometry(QtCore.QRect(770, 730, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(13)
        self.HighScoreLabel.setFont(font)
        self.HighScoreLabel.setStyleSheet("color: rgb(19, 153, 255);")
        self.HighScoreLabel.setObjectName("HighScoreLabel")
        self.HighScore = QtWidgets.QLCDNumber(NameLabel)
        self.HighScore.setGeometry(QtCore.QRect(770, 820, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HighScore.setFont(font)
        self.HighScore.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HighScore.setObjectName("HighScore")
        self.label = QtWidgets.QLabel(NameLabel)
        self.label.setGeometry(QtCore.QRect(8, 10, 881, 101))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.StartButton = QtWidgets.QPushButton(NameLabel)
        self.StartButton.setGeometry(QtCore.QRect(770, 370, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(23)
        self.StartButton.setFont(font)
        self.StartButton.setMouseTracking(False)
        self.StartButton.setStyleSheet("Color: rgb(130, 255, 46);")
        self.StartButton.setCheckable(False)
        self.StartButton.setObjectName("StartButton")
        self.comboBox = QtWidgets.QComboBox(NameLabel)
        self.comboBox.setGeometry(QtCore.QRect(770, 310, 121, 51))
        self.comboBox.setStyleSheet(
            "QComboBox QAbstractItemView { selection-background-color: orange; }"
        )
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(19)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(218, 112, 214);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(NameLabel)
        self.comboBox2.setGeometry(QtCore.QRect(770, 190, 121, 51))
        self.comboBox2.setStyleSheet(
            "QComboBox QAbstractItemView { selection-background-color: orchid; }"
        )
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(19)
        self.comboBox2.setFont(font)
        self.comboBox2.setStyleSheet("Color:rgb(218, 112, 214);")
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.HighScoreLabel_2 = QtWidgets.QLabel(NameLabel)
        self.HighScoreLabel_2.setGeometry(QtCore.QRect(770, 130, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(16)
        self.HighScoreLabel_2.setFont(font)
        self.HighScoreLabel_2.setStyleSheet("color: rgb(195, 135, 255);")
        self.HighScoreLabel_2.setObjectName("HighScoreLabel_2")
        self.HighScoreLabel_3 = QtWidgets.QLabel(NameLabel)
        self.HighScoreLabel_3.setGeometry(QtCore.QRect(770, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(13)
        self.HighScoreLabel_3.setFont(font)
        self.HighScoreLabel_3.setStyleSheet("color: rgb(42, 145, 255);")
        self.HighScoreLabel_3.setObjectName("HighScoreLabel_3")
        self.CurrentScore.raise_()
        self.GameScreen.raise_()
        self.EndButton.raise_()
        self.PauseButton.raise_()
        self.CurrentScoreLabel.raise_()
        self.HighScoreLabel.raise_()
        self.HighScore.raise_()
        self.label.raise_()
        self.StartButton.raise_()
        self.comboBox.raise_()
        self.comboBox2.raise_()
        self.HighScoreLabel_2.raise_()
        self.HighScoreLabel_3.raise_()

        self.retranslateUi(NameLabel)
        QtCore.QMetaObject.connectSlotsByName(NameLabel)

    def retranslateUi(self, NameLabel):
        _translate = QtCore.QCoreApplication.translate
        NameLabel.setWindowTitle(_translate("NameLabel", "EB Snake"))
        self.EndButton.setText(_translate("NameLabel", "Exit"))
        self.PauseButton.setText(_translate("NameLabel", "Stop"))
        self.CurrentScoreLabel.setText(
            _translate(
                "NameLabel",
                "<html><head/><body><p align=\"center\">SCORE 👻</p></body></html>"
            ))
        self.HighScoreLabel.setText(
            _translate(
                "NameLabel",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">High Score🪬</span></p></body></html>"
            ))
        self.label.setText(
            _translate(
                "NameLabel",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#4fe223;\">SNAKE GAME</span></p></body></html>"
            ))
        self.StartButton.setText(_translate("NameLabel", "Start"))
        self.comboBox.setItemText(0, _translate("NameLabel", "   Easy"))
        self.comboBox.setItemData(0, QtGui.QBrush(QtGui.QColor(144, 238, 144)),
                                  QtCore.Qt.ForegroundRole)
        self.comboBox.setItemText(1, _translate("NameLabel", "Meduim"))
        self.comboBox.setItemData(1, QtGui.QBrush(QtGui.QColor(255, 215, 0)),
                                  QtCore.Qt.ForegroundRole)
        self.comboBox.setItemText(2, _translate("NameLabel", "  Hard"))
        self.comboBox.setItemData(2, QtGui.QBrush(QtGui.QColor(255, 99, 71)),
                                  QtCore.Qt.ForegroundRole)
        self.comboBox2.setItemText(0, _translate("NameLabel", "  Orchid"))
        self.comboBox2.setItemData(0, QtGui.QBrush(QtGui.QColor("orchid")),
                                   QtCore.Qt.ForegroundRole)
        self.comboBox2.setItemText(1, _translate("NameLabel", "   Green"))
        self.comboBox2.setItemData(1, QtGui.QBrush(QtGui.QColor("green")),
                                   QtCore.Qt.ForegroundRole)
        self.comboBox2.setItemText(2, _translate("NameLabel", "    Red"))
        self.comboBox2.setItemData(2, QtGui.QBrush(QtGui.QColor("red")),
                                   QtCore.Qt.ForegroundRole)
        self.comboBox2.setItemText(3, _translate("NameLabel", "    Blue"))
        self.comboBox2.setItemData(3, QtGui.QBrush(QtGui.QColor("blue")),
                                   QtCore.Qt.ForegroundRole)
        self.HighScoreLabel_2.setText(
            _translate(
                "NameLabel",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Snake Color </span></p></body></html>"
            ))
        self.HighScoreLabel_3.setText(
            _translate(
                "NameLabel",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">levels</span></p></body></html>"
            ))
