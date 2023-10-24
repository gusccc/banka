import os

folder="invoices"

for count, filename in enumerate(os.listdir(folder)):
    dst=f"invoice_{str(count)}.pdf"
    src = f"{folder}/{filename}"
    dst=f"{folder}/{dst}"
    os.rename(src,dst)
