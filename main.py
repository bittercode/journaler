#!/usr/bin/env python

import findfiles
import txt2pdf

def write_header(txtfile,header):
    
    with open(txtfile,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(header.rstrip('\r\n') + '\n' + content)

myfile = findfiles.FileReader()

for txtfile in myfile.find_text("/mnt/f002/jr"):
    #Get the appropriate spreadsheet
    
    #pdfout = txtfile[:-3] + "pdf"
    #pdfconvert = txt2pdf.Txt2Pdf()
    #pdfconvert.txtconvert(txtfile,pdfout)