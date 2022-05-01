def verify_extension(*args, **kwargs)->bool:
    """
        Verify if extension is in file name
        file_name: name of file
        extension: extension to analyse
    """
    
    if 'file_name' in kwargs and 'extension' in kwargs:

        file_name:str
        extension_with_dot:str

        file_name = kwargs['file_name']
        extension_with_dot = "." + kwargs['extension']

        return extension_with_dot in file_name and extension_with_dot == file_name[-4:]
    return False