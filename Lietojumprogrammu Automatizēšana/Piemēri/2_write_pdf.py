from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import io
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont('DejaVu_Lv','fonts/DejaVuSans.ttf'))

input_pdf=PdfReader(open("invoices/invoice_0.pdf", "rb"))
buffer = io.BytesIO()
c = canvas.Canvas(buffer)
text = "Apmaksāts"
c.setFont("DejaVu_Lv", 16)
c.setFillColorRGB(1,0,0)
c.drawString(450,800, text)
c.setFillColorRGB(1,1,0)
c.rect(100,800,300,150,stroke=0,fill=1)
c.save()

text_pdf=PdfReader(buffer)

output_pdf=PdfWriter()

for i in range(len(input_pdf.pages)):
    page=input_pdf.pages[i]
    if i == 0:
        page.merge_page(text_pdf.pages[0])
    output_pdf.add_page(page)

with open("output.pdf", "wb") as f:
    output_pdf.write(f)
