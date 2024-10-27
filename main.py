import sys
import pygame
from tkinter import filedialog

# Initialize the mixer
pygame.mixer.init()

# Get path file
path = filedialog.askopenfilename()
if not path:
    print(" ")
    print("------------------Not selected file------------------")
    sys.exit()

# Load the music file
pygame.mixer.music.load(f"{path}")

# Play the music
pygame.mixer.music.play()

# Help command
print("Enter 'help' for commands list")

while True:
    # Keep the program running to allow music to play
    print("Press Enter to stop the music :", end=" ")
    command = input()
    command = command.lower()

    if command == "pause" or command == "stop":
        # Pause the music
        pygame.mixer.music.pause()

    if command == "play":
        # play the music
        pygame.mixer.music.play()

    if command == "exit" or command == "quit":
        # Exit the program
        sys.exit()

    if command == "help":
        print("------------------List of commands------------------")
        # List of commands
        print("Pause & Stop => Pause the music")
        print("Play => Stopped playing music")
        print("Exit & Quit => Exit the program")

    print(" ")
