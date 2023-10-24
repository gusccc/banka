from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_name, prefix):
    pdf_read=PdfReader(file_name)

    for page in range(len(pdf_read.pages)):
        output=prefix+"_"+str(page)+".pdf"
        pdf_write=PdfWriter()
        pdf_write.add_page(pdf_read.pages[page])

        with (open(output, "wb")) as f:
            pdf_write.write(f)

split_pdf("result.pdf","datne")
