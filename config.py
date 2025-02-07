# config.py
import os


START_SOUND = "Sounds\\StartGame.mp3"
GAMEOVER_SOUND = "Sounds\\GameOver.mp3"


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
APP_ICON_PATH = os.path.join(BASE_DIR, "icon\\snake_icon.ico")


EASY_INTERVAL = 250
MEDIUM_INTERVAL = 100
HARD_INTERVAL = 50
