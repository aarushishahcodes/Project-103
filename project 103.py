import sys
import time
import random
import os
import shutil

import watchdog.observers Observer
import watchdog.events FileSystemEventHandler

from_dir = "<Set path for tracking file system events>"\

# Event Handler Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()