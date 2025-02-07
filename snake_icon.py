# snake_icon.py
import sys
from PyQt5.QtGui import QPixmap, QPainter, QFont
from PyQt5.QtCore import Qt


def create_snake_icon(output_path="icon\\snake_icon.png", size=256):
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    font = QFont("Segoe UI Emoji", size // 2)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "🐍")
    painter.end()

    if pixmap.save(output_path):
        print(f"Icon saved to {output_path}")
    else:
        print("Failed to save icon.")


if __name__ == "__main__":
    create_snake_icon()
