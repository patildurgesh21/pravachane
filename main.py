import calendar
import string

import requests
import xlsxwriter
from bs4 import BeautifulSoup

workbook = xlsxwriter.Workbook('Jan.xlsx')
worksheet = workbook.add_worksheet()
row=0
column=0


for m in range(1,2):
    for date in range(1, 32):

        month = calendar.month_abbr[m]
        month = month.lower()
        dateval=(month +format(date, '02d'))

        link = ("https://satsangdhara.net/shri/" + month + format(date, '02d') + ".htm")

        r = requests.get(link)
        r.encoding
        'ISO-8859-1'
        html = r.content.decode(r.apparent_encoding)
        soup = BeautifulSoup(r.content, 'html.parser')
        fileline = ""
        filelineh1=""
        filelineh4=""
        h33=""
        dw="Download"




        for data in soup.find_all("h1"):
            h1 = data.get_text()
            filelineh1 += (h1 + '\n' + '\n')

        for data in soup.find_all("h3"):
            h33 = data.get_text()
            if dw in h33:

                break
            else:
                h33 = data.get_text()
                filelineh1 += (h33 + '\n' + '\n')

        for data in soup.find_all("p"):
            para = data.get_text()
            fileline += (para + '\n')

        fileline += ('\n')

        for data in soup.find_all("h4"):
            h4 = data.get_text()
            filelineh4 += (h4 + '\n' + '\n')

       # print(dateval)
        worksheet.write(row,column ,dateval)
        worksheet.write(row,column + 1 ,h1,)
        worksheet.write(row,column + 2 ,fileline,)
        worksheet.write(row,column + 3 ,h4,)
#        worksheet.write(row, column, dateval)
        charcount=0
        charcount =h33.find("\n")
#        charcount *=-1
        answ=""
        answ = h33[:charcount]
  #      print(answ)
        worksheet.write(row, column+4, answ)

        row +=1
workbook.close()
