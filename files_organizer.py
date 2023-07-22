import os
import shutil
import datetime

extension_data = {
    "compressed": ["zip", "7zip", "rar", "gz"],
    "audio": ["mp3", "aac", "flac", "wav", "aiff", "dsd", "pcm"],
    "video": ["mp4", "mov", "wmv", "avi", "avchd", "flv", "f4v", "swf", "mkv", "webm", "html5", "mpeg-2", "srt"],
    "picture": ["jpg", "png", "jpeg"],
    "programs": ["exe", "msi"],
    "documents": ["pdf", "docx", "xlsx", "txt"]
}

file = open(r"C:\Users\nirav\Downloads\documents\file_organizer_log.txt", "a")
file.write(f"{datetime.datetime.now()} - The script ran\n")
# path = input("Please enter the path:")
path = r"C:\Users\nirav\Downloads"
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    print(filename)
    print(extension)

    extension.lower() 
    extension = extension[1:]

    for type, ext in extension_data.items(): # store keys in type variable and values in ext 
        if extension in ext: # if the extension exists in the list then we find the associated key and use it to make dir or move file
            if os.path.exists(path+'/'+type):
             shutil.move(path+'/'+file, path+'/'+type)
            else:
               os.makedirs(path+'/'+type)
               shutil.move(path+'/'+file, path+'/'+type)

             
             
        
             
             