import subprocess
path="C:\Directory"
def open_file_explorer(path):
    subprocess.Popen(['explorer', path])
import tkinter as tk
from tkinter import filedialog

def open_folder_dialog(initial_dir=''):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(initialdir=initial_dir, title="Select a folder")
    
    if folder_path:
        return folder_path
    else:
        return None

# Example usage
selected_folder = open_folder_dialog(initial_dir='C:\\Your\\Desired\\Path')
if selected_folder:
    print("Selected folder:", selected_folder)
else:
    print("User canceled the folder selection.")


def main():
    while True:
        print("\nMenu:")
        print("1. Open PDFs Folder")
        print("2. Open C Codes Folder")
        print("3. Open Python Codes Folder")
        print("4. Open Documents Folder")
        print("5. Open Images Folder")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '0':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            open_file_explorer("C:\Directory\pdf")
        elif choice == '2':
            open_file_explorer("C:\Directory\c_codes")
        elif choice == '3':
            open_file_explorer()
        elif choice == '4':
            open_file_explorer()
        elif choice == '5':
            open_file_explorer()
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

# if __name__ == "__main__":
    # main()
