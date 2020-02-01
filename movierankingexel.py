import requests
from bs4 import BeautifulSoup

from openpyexcel import load_workbook

work_book = load_workbook('movie.xlsx')
work_sheet = work_book['movie']
print(work_sheet.cell(row=1, column=1).value)

work_sheet.cell(row=1, column=1, value = '순위')
work_sheet.cell(row = 1, column = 2, value = '영화제목')
work_sheet.cell(row = 1, column = 3, value = '별점')
print(work_sheet.cell(row=1, column=1).value)


work_book.save('movie.xlsx')