from bs4 import BeautifulSoup 

with open("catalog.html", "r") as html_doc:
  soup = BeautifulSoup(html_doc, "html.parser")
  html_doc.close()

with open("catalogsoup.html", "x") as parsed_doc:
  parsed_doc.write(soup.prettify())
  parsed_doc.close()