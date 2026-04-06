import speech_recognition as sr
import pyautogui
import os

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("Command:", command)
            return command
        except:
            return ""

def execute_command(command):
    if "open chrome" in command:
        os.system("start chrome")

    elif "scroll down" in command:
        pyautogui.scroll(-500)

    elif "volume up" in command:
        pyautogui.press("volumeup")