def verify_file_length(*args, **kwargs)->bool:
    """
        Verify if file has correct length.
        file_name: name of file
        extension: extension to analyse
    """

    file_name = None
    extension = None

    if 'file_name' in kwargs:
        file_name:str
        file_name = kwargs['file_name']
    if 'extension' in kwargs:
        extension:str
        extension = kwargs['extension']
    
    if file_name:
        if extension:
            return len(file_name) > len(extension) + 1
        return len(file_name) > 4
    return False