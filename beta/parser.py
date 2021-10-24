#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#
#   Original Script: kkkk.py

from bs4 import BeautifulSoup 
import requests
import os.path
from time import perf_counter

# Environment Variables
FILE_DIR = "beta/files"
FILE_NAME = "catalog.html"
LINK_FILTER = "https://suis.sabanciuniv.edu/prod/bwckctlg.p_disp_course_detail"

# Save it as a file
def saveOutput(printName, text):
  with open(f"{FILE_DIR}/{printName}", "a" if os.path.exists(f"{FILE_DIR}/{printName}") else "x") as parsed_doc:
    if isinstance(text,list):
      for t in text:
        parsed_doc.writelines(t + "\n")
    else:
      parsed_doc.write(text)
    parsed_doc.close()

# Parse the html
start = perf_counter()
print("[Log]: Parsing the html...")
with open(f"{FILE_DIR}/{FILE_NAME}", "r", encoding="utf-8") as html:
  soup = BeautifulSoup(html, "html.parser")
  html.close()
print("[Log]: Parsing the html completed in {:.2f} secs!".format(perf_counter() - start))

# Get & Filter Links
start = perf_counter()
print("[Log]: Getting relevant links...")
links = []
for link in soup.find_all("a"):
  if LINK_FILTER in str(link.get("href")):
    links.append(link.get("href"))
print("[Log]: Relevant links gathered in {:.2f} secs!".format(perf_counter() - start))

# Get Courses
start = perf_counter()
print("[Log]: Getting courses...")
courses = []
for l in links:
  r = requests.get(l)
  csoup = BeautifulSoup(r.content, "html.parser")
  for c in csoup.find_all("td",attrs={"class":"nttitle"}):
    #course = (c.string[:c.string.find("-") - 1])
    course = (c.string)
    courses.append(course)
print("[Log]: Courses gathered in {:.2f} secs!".format(perf_counter() - start))

saveOutput("courses.txt", courses)