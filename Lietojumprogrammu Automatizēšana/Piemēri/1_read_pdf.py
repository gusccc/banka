import PyPDF2

import pathlib
from tabulate import tabulate
data=[]
adrese = pathlib.Path("invoices")
visi_faili=list(adrese.glob("*.pdf"))
for f in range(len(visi_faili)):
    row=[]
    pdf_file=PyPDF2.PdfReader(open(visi_faili[f],"rb"))
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]

    text1=page1.extract_text()
    text2=page2.extract_text()

    pos1 = text1.find("Apmaksai:")
    pos2 = text1.find("Elektroenerģijas patēriņš kopā")

    summa = text1[pos1+10:pos2].rstrip()
    row.append(summa)
    pos1 = text2.find("Apjoms Mērv. Cena,")
    per = text2[pos1-23:pos1]
    row.append(per)
    data.append(row)

print(tabulate(data,headers=["Summa", "Periods"], tablefmt="github"))
