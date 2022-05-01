from file_utils.verify_file_length import verify_file_length
from file_utils.verify_extension import verify_extension

def verify_pdf_file(*args, **kwargs):
    """
        Verify if file_name is pdf
        file_name: name of file to analyse
    """

    if 'file_name' in kwargs:
        file_name:str
        file_name = kwargs['file_name']
        if verify_extension(file_name=file_name, extension='pdf') and\
            verify_file_length(file_name=file_name, extension='pdf'):
            return True
    return False
