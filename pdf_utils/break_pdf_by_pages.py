from PyPDF2 import PdfFileReader, PdfFileWriter

from .constants import input_path, result_path
from file_utils.get_files_with_extension import get_files_with_extension
from .verify_pdf_file import verify_pdf_file

def break_pdfs_by_pages(*args, **kwargs):

    input_files = get_files_with_extension(path_files=input_path, extension="pdf")

    for inputs_file in input_files:
        pdf_obj = open(input_path + inputs_file, 'rb')
        reader_pdf = PdfFileReader(
            stream=pdf_obj
        )
        num_of_page = reader_pdf.getNumPages()
        for index_page in range(num_of_page):
            
            out_obj = open("{}result_{}_{}.pdf".format(result_path, inputs_file, index_page), 'wb')
            page = reader_pdf.getPage(index_page)

            writer_pdf = PdfFileWriter()
            writer_pdf.addPage(page)
            writer_pdf.write(out_obj)
            
            out_obj.close()

        pdf_obj.close()
