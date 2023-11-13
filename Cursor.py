"""
    Cursor.py

    Changes user's cursor to a custom cursor.
    Useful in conjunction with GUI elements such as
    warnings and alerts.
"""

import pyautogui
import os

class Cursor:
    def __init__(self):
        self.cursor_path = None
        self.cursor_folder = None

    def change_cursors_folder(self, cursor_folder):
        # Get the list of cursor files in the folder
        cursor_files = [file for file in os.listdir(self.cursor_folder) if file.endswith('.cursor')]

        # Loop through each cursor file
        for cursor_file in cursor_files:
            cursor_path = os.path.join(self.cursor_folder, cursor_file)

            # Load the custom cursor image
            cursor_image = pyautogui.Image(cursor_path)

            # Get the dimensions of the cursor image
            cursor_width, cursor_height = cursor_image.size

            # Calculate the center coordinates for the cursor
            screen_width, screen_height = pyautogui.size()
            cursor_x = (screen_width - cursor_width) // 2
            cursor_y = (screen_height - cursor_height) // 2

            # Change the mouse cursor
            pyautogui.moveTo(cursor_x, cursor_y)
            pyautogui.mouseDown()
            pyautogui.mouseUp()

    def change_cursor_png(self, cursor_path):
        self.cursor_path = cursor_path

        # Get the screen width and height
        screen_width, screen_height = pyautogui.size()

        # Load the custom cursor image
        cursor_image = pyautogui.Image(self.cursor_path)

        # Get the dimensions of the cursor image
        cursor_width, cursor_height = cursor_image.size

        # Calculate the center coordinates for the cursor
        cursor_x = (screen_width - cursor_width) // 2
        cursor_y = (screen_height - cursor_height) // 2

        # Change the mouse cursor
        pyautogui.moveTo(cursor_x, cursor_y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()