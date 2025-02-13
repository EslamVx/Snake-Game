# snake_game.py
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QRectF
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from database import load_high_score, save_high_score, initialize_database
from ui import Ui_NameLabel
from config import (
    START_SOUND,
    GAMEOVER_SOUND,
    EASY_INTERVAL,
    MEDIUM_INTERVAL,
    HARD_INTERVAL,
)


class GameScreenWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui
        self.timer = QTimer(self)
        self.setFocusPolicy(Qt.StrongFocus)
        self.timer.timeout.connect(self.game_loop)
        self.fruit_images = [
            QtGui.QPixmap("icon/apple.png"),
            QtGui.QPixmap("icon/orange.png"),
            QtGui.QPixmap("icon/strawberry.png"),
            QtGui.QPixmap("icon/mango.png"),
            QtGui.QPixmap("icon/watermellon.png"),
        ]
        self.food_image = random.choice(self.fruit_images)
        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.snake = [[10, 10], [10, 9], [10, 8]]
        self.direction = Qt.Key_Right
        self.food = self.generate_food()
        self.score = 0
        self.update()

    def start_game(self):
        self.reset_game()
        self.timer.start(self.timer_interval)
        if self.ui is not None:
            self.ui.CurrentScore.display(self.score)

    def pause_game(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(self.timer_interval)

    def generate_food(self):
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        while [y, x] in self.snake:
            x = random.randint(0, 29)
            y = random.randint(0, 29)
        self.food_image = random.choice(self.fruit_images)
        return [y, x]

    def game_loop(self):
        if self.game_over:
            self.timer.stop()
            self.update()
            self.parent().parent().media_player.stop()
            self.parent().parent().game_over_player.stop()
            self.parent().parent().game_over_player.setPosition(0)
            self.parent().parent().game_over_player.play()
            current_high = load_high_score()
            if self.score > current_high:
                save_high_score(self.score)
                if self.ui is not None:
                    self.ui.HighScore.display(self.score)
            return

        head_y, head_x = self.snake[0]
        if self.direction == Qt.Key_Up:
            head_y -= 1
        elif self.direction == Qt.Key_Down:
            head_y += 1
        elif self.direction == Qt.Key_Left:
            head_x -= 1
        elif self.direction == Qt.Key_Right:
            head_x += 1
        new_head = [head_y, head_x]
        if (head_y < 0 or head_y > 29 or head_x < 0 or head_x > 29
                or new_head in self.snake):
            self.game_over = True
            self.update()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()
        self.update()
        if self.ui is not None:
            self.ui.CurrentScore.display(self.score)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up and self.direction != Qt.Key_Down:
            self.direction = Qt.Key_Up
        elif key == Qt.Key_Down and self.direction != Qt.Key_Up:
            self.direction = Qt.Key_Down
        elif key == Qt.Key_Left and self.direction != Qt.Key_Right:
            self.direction = Qt.Key_Left
        elif key == Qt.Key_Right and self.direction != Qt.Key_Left:
            self.direction = Qt.Key_Right
        event.accept()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        cell_w = self.width() // 30
        cell_h = self.height() // 30
        snake_color = "orchid"
        if self.ui is not None and hasattr(self.ui, "comboBox2"):
            selected_color = self.ui.comboBox2.currentText().strip()
            if selected_color:
                snake_color = selected_color
        painter.setBrush(QColor(snake_color))

        for seg in self.snake:
            y, x = seg
            painter.drawRect(
                QtCore.QRectF(x * cell_w, y * cell_h, cell_w, cell_h))
        food_y, food_x = self.food
        scaled_image = self.food_image.scaled(cell_w, cell_h,
                                              Qt.KeepAspectRatio,
                                              Qt.SmoothTransformation)
        painter.drawPixmap(food_x * cell_w, food_y * cell_h, scaled_image)

        if self.game_over:
            painter.setPen(Qt.white)
            painter.setFont(QtGui.QFont("Forte", 24))
            painter.drawText(self.rect(), Qt.AlignCenter, "Game Over!")


class SnakeGameDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        initialize_database()
        self.ui = Ui_NameLabel()
        self.ui.setupUi(self)
        stored_high = load_high_score()
        self.ui.HighScore.display(stored_high)
        self.game_widget = GameScreenWidget(self.ui.GameScreen, self.ui)
        layout = QtWidgets.QVBoxLayout(self.ui.GameScreen)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.game_widget)
        self.ui.StartButton.clicked.connect(self.start_game)
        self.ui.PauseButton.clicked.connect(self.toggle_pause)
        self.ui.EndButton.clicked.connect(self.close)
        self.ui.comboBox.currentIndexChanged.connect(self.update_difficulty)
        self.update_difficulty()
        self.ui.comboBox2.currentIndexChanged.connect(self.game_widget.update)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(
            QMediaContent(QtCore.QUrl.fromLocalFile(START_SOUND)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.media_player = QMediaPlayer()
        self.media_player.setPlaylist(self.playlist)
        self.game_over_player = QMediaPlayer()
        self.game_over_player.setMedia(
            QMediaContent(QtCore.QUrl.fromLocalFile(GAMEOVER_SOUND)))

    def update_difficulty(self):
        difficulty = self.ui.comboBox.currentText().strip()
        if difficulty == "Easy":
            self.game_widget.timer_interval = EASY_INTERVAL
        elif difficulty == "Medium":
            self.game_widget.timer_interval = MEDIUM_INTERVAL
        elif difficulty == "Hard":
            self.game_widget.timer_interval = HARD_INTERVAL
        else:
            self.game_widget.timer_interval = MEDIUM_INTERVAL

    def start_game(self):
        self.update_difficulty()
        self.game_widget.setFocus()
        self.game_widget.start_game()
        self.ui.PauseButton.setText("Stop")
        self.media_player.stop()
        self.media_player.setPosition(0)
        self.media_player.play()

    def toggle_pause(self):
        if self.game_widget.timer.isActive():
            self.game_widget.pause_game()
            self.media_player.stop()
            self.ui.PauseButton.setText("Resume")
        else:
            self.game_widget.pause_game()
            self.media_player.play()
            self.ui.PauseButton.setText("Stop")


# Thx to EslamVx && Bassel .
# End of code ...
