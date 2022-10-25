from openpyxl import Workbook
import xlsxwriter

from Constant import FORMAT_CELL, TYPE_URL, LENGTH_COLORS
from Functions import getPositionHeader, getTextHeader, createTag, createEvent, hasClickURL

from Scrapper import getInfo

wb = xlsxwriter.Workbook('Case.xlsx')
ws = wb.add_worksheet('Sheet')

infoCompanies = getInfo()

cell_format = wb.add_format(FORMAT_CELL)

for c in infoCompanies:

    nameCompany = c['name']

    urls = [c['google_url'], c['yelp_url'], c['book_url'], c['telf']]

    pos, pos_col = getPositionHeader()
    
    for i in range(len(TYPE_URL)):
        col = pos + (i + 1)
        t = createTag(nameCompany, TYPE_URL[i])
        e = createEvent(nameCompany, TYPE_URL[i])

        ws.write(f"A{col}", TYPE_URL[i])
        ws.write(f'C{col}', urls[i])
        ws.write(f"G{col}", t)
        ws.write(f"J{col}", e)
    
    for i in range(LENGTH_COLORS):
        text = getTextHeader(i, nameCompany)  
        ws.write(pos_col, i, text, cell_format)
    
    g = hasClickURL(c['google_url'])

    if g:
        ws.write(f"B{pos+1}", 'Click URL')    
    
    ws.write(f"B{pos+2}", 'Click URL')

wb.close()