from xlrd import open_workbook
from xlwt import easyxf
from xlutils.copy import copy

class SpreadSheet(object):
    
    def last_empty(self,wkbook_name):
        wb = open_workbook(wkbook_name)

        sh = wb.sheet_by_name('Journal')
        
        i=7
        ccell='init'

        while ccell:
            ccell = sh.cell_value(i,6)
            i += 1
        
        return i
    
    def write_link(self,wkbook_name,cell_row,ref):
        rb = open_workbook(wkbook_name,formatting_info=True)
        rs = rb.sheet_by_index(0)
        wb = copy(rb)
        ws = wb.get_sheet(0)

        style = easyxf('font: underline single')
        
        ws.write(cell_row,6,Formula(ref),link)

        ws.write(22,4,2345)

        wb.save(wkbook_name)