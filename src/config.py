import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

ASSETS_DIR = PROJECT_ROOT / "assets"
ICONS_DIR = PROJECT_ROOT / "icons"
IMAGE_DIR = PROJECT_ROOT / "images"

APP_NAME = "c.3D.v"
APP_VERSION = "0.1.0"
APP_AUTHOR = ""

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 800
WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 600

APPEARANCE_MODE = "System"
COLOR_THEME = "dark-blue"

FONT_FAMILY = "Helvetica"
FONT_TITLE = (FONT_FAMILY, 20, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 20, "italic")
FONT_BODY = (FONT_FAMILY, 12, "normal")

DB_NAME = "C3DV.db"
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASSWORD = ""

DEBUG = True