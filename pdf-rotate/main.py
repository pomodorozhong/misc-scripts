import PyPDF2

angle = 90
in_file_name = 'original.pdf'
out_file_name = 'rotated.pdf'

pdf_in = open(in_file_name, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(angle)
    pdf_writer.addPage(page)
pdf_out = open(out_file_name, 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
