from bs4 import BeautifulSoup 

# Environment Variables
HTML_DIR = "beta/files"
HTML_DOC_NAME = "catalog.html"
LINK_FILTER = "https://suis.sabanciuniv.edu/prod/bwckctlg.p_disp_course_detail"

# Save it as a file
def saveOutput(printName, text):
  with open(f"{HTML_DIR}/{printName}", "x") as parsed_doc:
    parsed_doc.write(text)
    parsed_doc.close()

# Parse the html
with open(f"{HTML_DIR}/{HTML_DOC_NAME}", "r", encoding="utf-8") as html_doc:
  soup = BeautifulSoup(html_doc, "html.parser")
  html_doc.close()

# Get Links
links = soup.find_all("a")

# Filter Links
filteredLinks = []
for link in links:
  if LINK_FILTER in str(link.get("href")):
    filteredLinks.append(link.get("href"))



