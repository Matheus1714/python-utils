from PyPDF2 import PdfFileMerger

from .constants import input_path, result_path
from file_utils.get_files_with_extension import get_files_with_extension

def join_pdfs(*args, **kwargs)->None:
    
    result_file_name = "result"
    if 'result_file_name' in kwargs:
        result_file_name:str
        result_file_name = kwargs['result_file_name']

    input_files = get_files_with_extension(input_path)

    merger = PdfFileMerger()
    for inputs_file in input_files:
        merger.append(input_path + inputs_file)

    output_path = result_path + result_file_name + '.pdf'
    merger.write(output_path)

    merger.close()
