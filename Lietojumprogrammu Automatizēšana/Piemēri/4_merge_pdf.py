from PyPDF2 import PdfReader, PdfWriter

def merge_pdf(input_file, output_file):
    result=PdfWriter()
    for file in input_file:
        reader=PdfReader(file)
        for page in reader.pages:
            result.add_page(page)
    
    with open(output_file, "wb") as f:
        result.write(f)

input_file=['invoices/invoice_0.pdf','invoices/invoice_1.pdf', 'invoices/invoice_2.pdf']
output_file='result.pdf'

merge_pdf(input_file,output_file)
