import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("pdfs")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
  if ".pdf" in arquivo:
    merger.append(f"pdfs/{arquivo}")

merger.write("PDF final.pdf")
