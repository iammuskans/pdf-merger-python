from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

# Automatically get all PDFs in folder
pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]

for file in pdf_files:
    merger.append(file)

merger.write("merged-pdf.pdf")
merger.close()

print("✅ All PDFs merged automatically!")