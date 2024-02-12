import subprocess
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def open_folder_dialog(initial_dir=''):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(initialdir=initial_dir, title="Select a folder")
    
    if folder_path:
        folder_name=os.path.basename(folder_path)
        return folder_name,folder_path
    else:
        return None

# Example usage


videos=[".WEBM",".MKV",".MPG",".MP2",".MPEG", ".MPE", ".MPV",".OGG",".MP4", ".M4P",".M4V",".AVI", ".WMV",".MOV",".QT",".FLV",".SWF",".AVCHD"]
documents=[".DOCX",".DOC",".PPT",".PPTX",".TXT"]
images=[".JPEG",".JPG",".GIF",".WEBP",".RAW",".SVG"]
directory_path = "c:/Directory" #Enter the directory where you would like to create the folders
if os.path.exists(directory_path):
    os.makedirs(directory_path+"/videos",exist_ok=True)
    os.makedirs(directory_path+"/documents",exist_ok=True)
    os.makedirs(directory_path+"/pdf",exist_ok=True)
    os.makedirs(directory_path+"/pythoncodes",exist_ok=True)
    os.makedirs(directory_path+"/c_codes",exist_ok=True)
    os.makedirs(directory_path+"/images",exist_ok=True)
    pass
    # print(f"Directory '{directory_path}' already exists.")
else:
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created successfully.")

pathtc="C:/Users/KIIT/OneDrive/Desktop"
videospath=directory_path+"/videos"
docspath=directory_path+"/documents"
pdfpath=directory_path+"/pdf"
pythonpath=directory_path+"/pythoncodes"
ccodepath=directory_path+"/c_codes"
imagepath=directory_path+"/images"

def open_file_explorer(path):
    subprocess.Popen(['explorer', path])



def folder_cleaner(pathtc,files):
    print("File recieved",files)
    for file in files:
            filespath=os.path.join(pathtc,file)
            if os.path.isfile(filespath):
                filename,extension=os.path.splitext(file)
                if filename[0]!='~':
                    print(f"File: {filename}, Extension: {extension}")
                    if extension.upper() in videos:
                        shutil.move(filespath,videospath)
                        print("ofc this works")
                    elif extension.upper() in documents:
                        shutil.move(filespath,docspath)
                        print("dayum this works too")
                    elif extension.upper() ==".PDF":
                        shutil.move(filespath,pdfpath)
                        print("PDF works too")
                    elif extension.upper() ==".CPP" or extension.upper() ==".C":
                        shutil.move(filespath,ccodepath)
                        print("C code works too")
                    elif extension.upper() ==".PY":
                        shutil.move(filespath,pythonpath)
                        print("Python works too")
                    elif extension.upper() in images:
                        shutil.move(filespath,imagepath)
                        print("Image works too")
                    elif extension.upper() ==".EXE":
                        os.remove(filespath)
                    else:
                        pass
                else:
                    # print(filename)
                    pass

def cleaner(pathtc,dirname):
    if os.path.exists(pathtc):
        files=os.listdir(pathtc)
        print(files)
        if files:
            for folder in files:
                newpath=str(pathtc)+"/"+str(folder)
                print(newpath)
                if os.path.isdir(newpath):
                    print("okay its folder")
                    files1=os.listdir(newpath)
                    # folder_cleaner(newpath,files1)
                    # cleaner(newpath,folder)
                elif os.path.isfile(newpath):
                    print("File is being detected")
                    folder_cleaner(pathtc,files)
                else:
                    print("Theres some error")
def main():
    # choice=1
    global pathtc
    # while choice:
    print(
'''
Choice
1. Move files
2. File opener
'''
            )
    choice=int(input('-->'))
    if choice==1:
        result = open_folder_dialog(initial_dir=pathtc)
        if result:
            Dirname,path=result
            cleaner(path,Dirname)
            print("Selected folder:", Dirname)
        else:
            print("User canceled the folder selection.")
            
    elif choice==2:
        path="C:\Directory"
        open_file_explorer(path)
if __name__=="__main__":
    main()