import PyPDF2

pdFiles=["First1.pdf","Second2.pdf"]
merger=PyPDF2.PdfMerger()
for files in pdFiles:
    readBinary=open(files,'rb') #rb stands for read-binary of the files. open is used to open files and read it.
    pdFFiles=PyPDF2.PdfMerger(readBinary)
    merger.append(pdFFiles)
pdFFiles.close()
merger.write('merged12.pdf')

