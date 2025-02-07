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
        self.GameScreen.setStyleSheet("background-color: black;")
        self.GameScreen.setObjectName("GameScreen")

        self.EndButton = QtWidgets.QPushButton(NameLabel)
        self.EndButton.setGeometry(QtCore.QRect(770, 340, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(24)
        self.EndButton.setFont(font)
        self.EndButton.setStyleSheet("color: rgb(255, 33, 85);")
        self.EndButton.setObjectName("EndButton")

        self.PauseButton = QtWidgets.QPushButton(NameLabel)
        self.PauseButton.setGeometry(QtCore.QRect(770, 270, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(21)
        self.PauseButton.setFont(font)
        self.PauseButton.setStyleSheet("color: rgb(92, 233, 255);")
        self.PauseButton.setObjectName("PauseButton")

        self.CurrentScore = QtWidgets.QLCDNumber(NameLabel)
        self.CurrentScore.setGeometry(QtCore.QRect(770, 510, 121, 51))
        self.CurrentScore.setObjectName("CurrentScore")

        self.CurrentScoreLabel = QtWidgets.QLabel(NameLabel)
        self.CurrentScoreLabel.setGeometry(QtCore.QRect(770, 420, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)
        self.CurrentScoreLabel.setFont(font)
        self.CurrentScoreLabel.setStyleSheet("color: rgb(52, 255, 238);")
        self.CurrentScoreLabel.setObjectName("CurrentScoreLabel")

        self.HighScoreLabel = QtWidgets.QLabel(NameLabel)
        self.HighScoreLabel.setGeometry(QtCore.QRect(770, 580, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(13)
        self.HighScoreLabel.setFont(font)
        self.HighScoreLabel.setStyleSheet("color: rgb(19, 153, 255);")
        self.HighScoreLabel.setObjectName("HighScoreLabel")

        self.HighScore = QtWidgets.QLCDNumber(NameLabel)
        self.HighScore.setGeometry(QtCore.QRect(770, 680, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(12)
        font.setBold(False)
        self.HighScore.setFont(font)
        self.HighScore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HighScore.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HighScore.setObjectName("HighScore")

        self.label = QtWidgets.QLabel(NameLabel)
        self.label.setGeometry(QtCore.QRect(8, 10, 881, 101))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.StartButton = QtWidgets.QPushButton(NameLabel)
        self.StartButton.setGeometry(QtCore.QRect(770, 200, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(23)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("color: rgb(130, 255, 46);")
        self.StartButton.setObjectName("StartButton")

        self.label_2 = QtWidgets.QLabel(NameLabel)
        self.label_2.setGeometry(QtCore.QRect(770, 740, 121, 131))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(38)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(NameLabel)
        self.comboBox.setGeometry(QtCore.QRect(770, 130, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(19)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(181, 33, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.CurrentScore.raise_()
        self.GameScreen.raise_()
        self.EndButton.raise_()
        self.PauseButton.raise_()
        self.CurrentScoreLabel.raise_()
        self.HighScoreLabel.raise_()
        self.HighScore.raise_()
        self.label.raise_()
        self.StartButton.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()

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
                '<html><head/><body><p align="center">SCORE 👻</p></body></html>',
            )
        )
        self.HighScoreLabel.setText(
            _translate(
                "NameLabel",
                '<html><head/><body><p align="center"><span style=" font-size:14pt;">High Score🪬</span></p></body></html>',
            )
        )
        self.label.setText(
            _translate(
                "NameLabel",
                '<html><head/><body><p align="center"><span style=" font-size:48pt; color:#4fe223;">SNAKE GAME 🐍</span></p></body></html>',
            )
        )
        self.StartButton.setText(_translate("NameLabel", "Start"))
        self.label_2.setText(
            _translate(
                "NameLabel",
                '<html><head/><body><p align="center"><span style=" font-size:48pt; color:#4fe223;">🐍</span></p></body></html>',
            )
        )
        self.comboBox.setItemText(0, _translate("NameLabel", "Easy"))
        self.comboBox.setItemText(1, _translate("NameLabel", "Medium"))
        self.comboBox.setItemText(2, _translate("NameLabel", "Hard"))
