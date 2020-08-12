from bs4 import BeautifulSoup

html_file = open('pge_meter_details.html', 'r')
html_contents = html_file.read()

soup = BeautifulSoup(html_contents, 'lxml')
address_container = soup.find(attrs={'class': 'module-body sa-info'})

address = ''
rate_name = ''

for item in address_container:
  if item.name == 'ul':
    for tag in item:
      if tag.name == 'li':
        if tag.string != None:
          address += ' '.join(tag.string.replace('\n','').strip().split())


rate = soup.find(attrs={'class': 'module-body', 'style': 'padding-bottom: 60px;'}).findChildren('h3', recursive=False)
for item in rate:
  rate_name = ' '.join(item.string.replace('\n','').strip().split())

print(address)
print(rate_name)