from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = 'file1.pdf'
pdf = PdfFileReader(pdf_file_path)

pages = [0,2,4]
pdfwriter = PdfFileWriter()

for page_num in pages:
    pdfwriter.addPage(pdf.getPage(page_num))

with open('output.pdf', 'wb') as out:
    pdfwriter.write(out)

print('PDF file has been split')
