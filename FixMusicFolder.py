import os, stat

rootdir = r"d:\Users\Pete\Music"
empty=0
notEmpty=0
converted=0
notConverted=0
errConverted=0
folderFound = True 

try:
    os.chdir(rootdir)
except (WindowsError, OSError):
    print "ERROR: Music folder not found"
    folderFound = False
    
if (folderFound == true):  
    #iterate through all files in root directory
    for root, dirs, filenames in os.walk(rootdir):
        #skip the iTunes folder
        if os.getcwd() != "iTunes":
            for filename in filenames:
                # Get the absolute path to the file.
                filename = os.path.join(root, filename)
                
                #convert read only files to writable
                try: 
                    #if read only
                    if (not os.stat(filename)[0] & stat.S_IWRITE):
                        #make writeable
                        os.chmod(filename, stat.S_IWRITE)
                        print(filename+" is no longer read only")
                        converted+=1
                    else:
                        notConverted+=1
                except(WindowsError, OSError):
                    print("Error converting "+filename)
                    errConverted+=1
                    
                #delete all empty folders
                try:
                    os.rmdir(root)
                    print(root+" removed")
                    empty+=1
                except (WindowsError, OSError):
                    notEmpty+=1
                    
                #delete non-music files
                if (filename.endswith(".mp3") == False) | (filename.endswith(".flac") == False) | (filename.endswith(".aac") == False) | (filename.endswith(".wav") == False) | (filename.endswith(".m4a") == False) | (filename.endswith(".ogg") == False):
                    os.remove(filename)
   
    print(empty," folders removed")
    print(notEmpty," folders kept")
    print(converted, "files converted to writable")
    print(notConverted, "files not converted")
    print(errConverted, "files could not be converted due to error")