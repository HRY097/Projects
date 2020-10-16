#This program makes many folers like Images,Docs,Installers,Videos and Others and puts all of the files on that folders present in the current directory
import os
#A Print Statement So That User Could Verify That AutoCleaner Has Started
print("AutoCleaner have started")
#A Function To Make The Folders
def CreateFolder(folder):
    if not os.path.exists(folder):
         os.makedirs(folder)
#A Function To Move Folders
def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")
# Creating The Folders
CreateFolder('ZipFiles'), CreateFolder('Images'), CreateFolder('Docs'), CreateFolder('Installers'), CreateFolder('Videos'), CreateFolder('Others')
files = os.listdir()
files.remove('AutoCleaner.py'), files.remove('Images'), files.remove('Docs'), files.remove('Installers'), files.remove('Videos'), files.remove('Others'), files.remove('ZipFiles')
# Telling The Interpreter About All The Extensions
imgExts = ['.png','.jpg','.jpeg']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]
docExts = ['.pdf','.doc','.docx','.xlsx','.ods']
documents = [file for file in files if os.path.splitext(file)[1].lower() in docExts ]
installersExts = ['.msi','.exe',]
installer = [file for file in files if os.path.splitext(file)[1].lower() in installersExts ]
videosExts = ['.mp4','.mkv']
videos = [file for file in files if os.path.splitext(file)[1].lower() in videosExts ]
audioExts = ['.mp3']
audio = [file for file in files if os.path.splitext(file)[1].lower() in audioExts ]
zipExts = ['.zip','.tar','.rar','.gz','.tar.gz']
zipfiles = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]
# Files Which Are Apart From The Mentioned Above Will Be Moved To Others Folder
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in installersExts) and (ext not in videosExts) and (ext not in audioExts) and (ext not in zipExts):
        others.append(file)
# Moving The Files To Folders
move("Images", images), move("Docs", documents), move("Installers", installer), move("Videos", videos), move("Audio", audio), move("Others", others), move("ZipFiles", zipfiles)
# A Print Statement So That User Could Verify That The Tool Has Ended
print("AutoCleaner has sorted all your files")
