from PyPDF2 import PdfFileMerger
import os

def join_pdfs():
    
    input_path = os.getcwd() + '\\pdf_utils\\inputs\\'
    result_path = os.getcwd() + '\\outputs\\'
    input_files = os.listdir(input_path)

    merger = PdfFileMerger()
    for inputs_file in input_files:
        merger.append(input_path + inputs_file)

    merger.write(result_path + "result.pdf")
    merger.close()
