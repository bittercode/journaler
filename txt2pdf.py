#Script for taking emails saved as text and creating pdf

from reportlab.pdfgen import canvas
import os, sys, codecs

#find out what platform we are on and whether accelerator is
#present, in order to print this as part of benchmark info.
try:
    import _rl_accel
    ACCEL = 1
except ImportError:
    ACCEL = 0


from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4

class Txt2Pdf(object):
    #precalculate some basics
    top_margin = A4[1] - inch
    bottom_margin = inch
    left_margin = inch
    right_margin = A4[0] - inch
    frame_width = right_margin - left_margin
    
    def drawPageFrame(self,canv):
        canv.line(self.left_margin, self.top_margin, self.right_margin, self.top_margin)
        canv.setFont('Times-Italic',12)
        canv.drawString(self.left_margin, self.top_margin + 2, "Homer's Odyssey") #I think this is the header.
        canv.line(self.left_margin, self.top_margin, self.right_margin, self.top_margin)
    
    
        canv.line(self.left_margin, self.bottom_margin, self.right_margin, self.bottom_margin)
        canv.drawCentredString(0.5*A4[0], 0.5 * inch,
                   "Page %d" % canv.getPageNumber())
    
    
    #textfile is coming in and pdfout is the file that will be created.
    def txtconvert(self,textfile,pdfout):
        if sys.platform[0:4] == 'java':
            impl = 'Jython'
        else:
            impl = 'Python'
    
        canv = canvas.Canvas(pdfout, invariant=1) #replace with proper output file name
        canv.setPageCompression(1)
    
        #on with the text...
        self.drawPageFrame(canv)
    
        canv.setFont('Times-Roman', 12)
        tx = canv.beginText(self.left_margin, self.top_margin - 0.5*inch)
    
    
        data = codecs.open(textfile,'r','utf-8').readlines()
        for line in data:
            #this just does it the fast way...
            tx.textLine(line)
    
            #page breaking
            y = tx.getY()   #get y coordinate
            if y < self.bottom_margin + 0.5*inch:
                canv.drawText(tx)
                canv.showPage()
                self.drawPageFrame(canv)
                canv.setFont('Times-Roman', 12)
                tx = canv.beginText(self.left_margin, self.top_margin - 0.5*inch)
    
                #page
                pg = canv.getPageNumber()
                if verbose and pg % 10 == 0:
                    print 'formatted page %d' % canv.getPageNumber()
    
        if tx:
            canv.drawText(tx)
            canv.showPage()
            self.drawPageFrame(canv)
    
        canv.save()