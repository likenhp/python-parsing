from bs4 import BeautifulSoup
import PyPDF2
import tabula

####################################################################
# HTML
####################################################################

html_file = open('index.html', 'r')
html_contents = html_file.read()

soup = BeautifulSoup(html_contents, 'lxml')

# print(soup.div) #<-the first div
# print(soup.div.name) #<- the first div html tag
# print(soup.div.string) #<-the first div contents
# print(soup.div.parent.name) #<-the first div parent html tag
# print(soup.find_all('div')) #<-find all divs
# print(soup.find_all(attrs={'class': 'test'})) #<-find all divs with class test
# print(soup.find(attrs={'class': 'test'})) #<-find first div where class test
# print(soup.get_text()) #<-all text in html

####################################################################
# Text PDF
####################################################################

pdf_file = open('lorem-ipsum.pdf', 'rb')
pdf_contents = PyPDF2.PdfFileReader(pdf_file) # <- the pdf object

# numPages = pdf_contents.numPages #<- number of pages
# first_page_object = pdf_contents.getPage(0) #<- get the first page
# page_one_text = first_page_object.extractText() #<- get the text, saved as a string
# if 'lorem' in page_one_text: #<- find the string contents
#   print('works')
search_word = 'lorem'
search_word_count = 0
for page in range(0, pdf_contents.numPages):
  page_object = pdf_contents.getPage(page)
  raw_text = page_object.extractText()
  search_text = raw_text.lower().split()
  for word in search_text:
    if search_word in word:
      search_word_count += 1
print(search_word_count)
  
# pdf_file.close() #<- close the file

####################################################################
# Table PDF
####################################################################
