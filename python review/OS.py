import os

# path = "C:\\Users\\milad\\OneDrive\\Documents\\python review\\Notes\\OS.txt"
path = "C:\\Users\\milad\\OneDrive\\Documents\\python review\\Notes\\"

if os.path.exists(path):
    print("that location is exist.")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("this path is a directory!")
else:
    print("this file isn't exist.")