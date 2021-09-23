import os

def Filelist(root, file_type):
    """ This function takes as input a path 'root' and 'file type' and returns
        all the files under the given path with the mentioned type. """
    return [f for _, _, files in os.walk(root) for f in files if f.endswith(file_type)]
