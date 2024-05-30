import requests

page = requests.get("https://themultiverse.school/classes")

html_doc = page.text
# print(html_doc)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

for heading in soup.find_all('h2'):
    heading_text = heading.get_text()
    if heading_text[0:3] == "TBD":
        first_part = heading_text[0:9]
        second_part = heading_text[9:]
    else:
        first_part = heading_text[0:19]
        second_part = heading_text[19:]
    print(first_part)
    print(second_part)

    