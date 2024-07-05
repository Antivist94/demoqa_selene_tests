import os

file = 'photo_man.png'

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, 'files/')
PHOTO_PATH = os.path.abspath(FILES_DIR + file)


