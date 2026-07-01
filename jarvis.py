# Desktop Assistant Jarvis
# Created for CodTech Internship

import os
import webbrowser
from datetime import datetime

print("===================================")
print("      WELCOME TO JARVIS")
print("===================================")

while True:
    print("\nChoose an option:")
    print("1. Open Google")
    print("2. Open YouTube")
    print("3. Show Current Time")
    print("4. Open Notepad")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        webbrowser.open("https://www.google.com")
        print("Opening Google...")

    elif choice == "2":
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube...")

    elif choice == "3":
        now = datetime.now()
        print("Current Time:", now.strftime("%H:%M:%S"))

    elif choice == "4":
        os.system("notepad")

    elif choice == "5":
        print("Thank you for using Jarvis!")
        break

    else:
        print("Invalid Choice!")