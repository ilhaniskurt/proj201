from bs4 import BeautifulSoup

with open("catalogsoup.html", "r") as parsed_doc:
  soup = BeautifulSoup(parsed_doc, "html.parser")
  parsed_doc.close()

def printOut():
  pass

def getText():
  global soup
  return soup.get_text()

def getCourses():
  global soup
  return soup.find_all(("td", {"class":"nttitle"}))

print(getCourses())