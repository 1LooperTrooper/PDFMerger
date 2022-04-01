import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

def img2pdf(path):
	#List to store PDFs
	pdf_list = []

	#Grab all PDFs
	for filename in glob.glob(path):
	    pdf_list.append(filename)

	merger = PdfFileMerger()

	for pdf in pdf_list:
		merger.append(PdfFileReader(open(pdf, 'rb')))

	file_name = input("File Name: ")
	merger.write(file_name + ".pdf")

img2pdf('*.pdf')

