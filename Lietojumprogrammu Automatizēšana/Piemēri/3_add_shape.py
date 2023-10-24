import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

input_pdf = PdfReader(open('./invoices/invoice_0.pdf', 'rb'))

buffer = io.BytesIO()
c = canvas.Canvas(buffer)

rgb = (255,255,255)
c.setFillColor(rgb)
c.rect(50,680,120,45,stroke=0,fill=1)

c.save()
buffer.seek(0)

text_pdf = PdfReader(buffer)

output_pdf = PdfWriter()
for i in range(len(input_pdf.pages)):
    page = input_pdf.pages[i]
    if i == 0:
        page.merge_page(text_pdf.pages[0])
    output_pdf.add_page(page)

with open('output.pdf', 'wb') as f:
    output_pdf.write(f)
