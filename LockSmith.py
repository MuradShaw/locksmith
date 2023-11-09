import os
import pyautogui
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from MySQLHandler import MySQLHandler
import time
import pyperclip

class LockSmith:
    def __init__(self):
        self.keydir = "C:/Users/annar/OneDrive/Desktop/Key"  # Directory for our key storage
        self.curdir = os.getcwd()  # Directory for program files
        self.driverdir = self.curdir + "\ChromeDriver"  # Directory for chrome driver
        self.mysql_handler = MySQLHandler()  # Initiate MySQLHandler as mysql_handler
        self.driver = webdriver.Chrome()  # Initiate chrome driver as driver


    def directory_exists(self, directory):
        """
            Check if our directory has become accessible.
            This is essential to knowing if our key is inserted or not.
        """

        if os.path.exists(directory) and os.path.isdir(directory):
            return True
        else:
            return False


    def key_inserted(self):
        """
            Take our data file from our key directory and
            print its contents.
        """

        print(Fore.YELLOW + "Success | Key Inserted > Main.py")

        # Get our data as a HTML insertable string format
        with open("C:/Users/annar/OneDrive/Desktop/Key/data.txt") as f:
            key_data = f.read()

        print(Fore.LIGHTCYAN_EX + "Key Data | " + key_data + " > Key")

        # Insert in our webpage
        self.set_data_and_go(key_data)


    def set_data_and_go(self, field_data):
        """
            Very strange method that opens up a webpage url, takes
            an html element from it, and fills it with data.

            We then automatically and digitally "press" the "enter" key,
            effectively submitting a request.
        :param field_data: Data to be inserted into an html field
        """

        # TODO: Dynamically get URL
        url = 'https://www.linkedin.com/home'
        self.driver.get(url)

        print(Fore.BLACK + f"Reaching {url}... > Main.py")

        # Wait before proceeding
        time.sleep(2)

        try:
            # Dynamically get element ID
            element = self.driver.switch_to.active_element

            # Retrieve the HTML ID of the selected element
            element_id = element.get_attribute("id")

            # Nothing was selected/some other error
            if not element_id:
                # Copy to the clipboard instead
                pyperclip.copy(field_data)
                print(Fore.YELLOW + "Warning | Field not found, copying data to clipboard instead > Main.py")

                return

            # Get our element via ID
            input_field = self.driver.find_element(By.ID, element_id)

            print(Fore.BLACK + f"Locating element {element_id}... > Main.py")

        except Exception as e:
            print(Fore.RED + f"Failure | Cannot find HTML element-id, returning... > Main.py")
            print(e)
            return

        data_to_fill = field_data  # This line literally makes no sense
        input_field.send_keys(data_to_fill)  # Fill in HTML element with data

        print(Fore.BLACK + f"Inserting Data {data_to_fill}... > Main.py")

        pyautogui.press('enter')  # Digitally hit "enter" submitting our request

        print(Fore.BLACK + "Go! > Main.py")