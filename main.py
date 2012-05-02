#!/usr/bin/env python

import findfiles
import watermark
import spreads

def write_header(txtfile,header):
    
    with open(txtfile,'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(header.rstrip('\r\n') + '\n' + content)

def main():
    jpath = "/mnt/f002/jr/journals/"
    zeroes = ["","0","00"]
    myfile = findfiles.FileReader()
    
    for txtfile in myfile.find_text("/mnt/f002/jr/journals/new"):
        print txtfile + '\n'
        t_month = txtfile[:2]
        t_company = txtfile[4:7]
        t_year = txtfile[2:4]
        if t_company.upper() == "CON":
            comp = ["N","CO"]
        else:
            comp = ["E","EE"]
        print "tm: " + t_month + "tc: " + t_company + "ty: " + t_year + "c: " + comp[0]
        spread_name = jpath + "20" + t_year + t_month + " " + comp[0] + " " + "Journal.xls"
        print "SN: " + spread_name + '\n'
        
        spreadsheet = spreads.SpreadSheet()
        row_index = spreadsheet.last_empty(spread_name)
        
        rec = str(row_index - 7)
        zero_count = 3 - len(rec)
        t_num = comp[1] + t_year + t_month + "N" + zeroes[zero_count] + rec
        print t_num # this is really close - I'm off by one
        
        #Insert a record in the right spot
        
        #Finish up with the actual file
        
        
        
        
if __name__ == '__main__':
    main()