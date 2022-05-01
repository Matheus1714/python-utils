from distutils import extension
import os

def get_files_with_extension(*args, **kwargs)->list:
    """
        Get files with specific extension
        file_name: name of file
        extension: extension to get
    """

    path_files = None
    extension = None
    
    if 'path_files' in kwargs:
        path_files:str
        path_files = kwargs['path_files']
    if 'extension' in kwargs:
        extension:str
        extension = kwargs['extension']

    if path_files:

        files = os.listdir(path_files) or []

        if extension:
            files_with_extension = []
            for file in files:
                if extension in file:
                    files_with_extension.append(file)
            return files_with_extension
    return []
