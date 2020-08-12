import PyPDF2

pdf_file = open('sdge_bill.pdf', 'rb')
pdf_contents = PyPDF2.PdfFileReader(pdf_file)

meter_number = ''
tax_total = ''

numPages = pdf_contents.numPages

search_word_meter = 'meter number:'
search_word_tax = 'total taxes & fees on electric charges'
search_word_count = 0
for page in range(0, pdf_contents.numPages):
  page_object = pdf_contents.getPage(page)
  raw_text = page_object.extractText()
  search_text = raw_text.lower().split('\n')
  for index, string in enumerate(search_text):
    if search_word_meter in string and page == 2:
      meter_raw = search_text[index + 1]
      try:
          meter_number = int(meter_raw)
      except ValueError:
        pass
    elif search_word_tax in string:
      tax_total = ' '.join(search_text[index + 1].split())

print(tax_total)
print(meter_number)