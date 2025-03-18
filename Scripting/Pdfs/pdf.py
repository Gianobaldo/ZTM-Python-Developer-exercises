import PyPDF2
import sys

inputs = sys.argv[1:] #grabs pdfs and store as list

def pdf_merger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

pdf_merger(inputs)