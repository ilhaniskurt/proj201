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
                if isinstance(t,list):
                    for i in text:
                        parsed_doc.writelines(str(i) + "\n")
                else:
                    parsed_doc.writelines(str(t) + "\n")
        else:
            parsed_doc.write(str(text))
        parsed_doc.close()

# Parse the html
def getSoup():
    start = perf_counter()
    print("[Log]: Parsing the html...")
    with open(f"{FILE_DIR}/{FILE_NAME}", "r", encoding="utf-8") as html:
        soup = BeautifulSoup(html, "html.parser")
        html.close()
    print("[Log]: Parsing the html completed in {:.2f} secs!".format(perf_counter() - start))
    return soup

# Get & Filter Links
def getLinks(soup):
    start = perf_counter()
    print("[Log]: Getting relevant links...")
    links = []
    for link in soup.find_all("a"):
        if LINK_FILTER in str(link.get("href")):
            links.append(link.get("href"))
    print("[Log]: Relevant links gathered in {:.2f} secs!".format(perf_counter() - start))
    return links

# Get Course Titles
def getCourseTitles(links):
    start = perf_counter()
    print("[Log]: Getting course titles...")
    courses = []
    counter = 0
    for l in links:
        r = requests.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for c in soup.find_all("td",attrs={"class":"nttitle"}):
            course = (c.string[:c.string.find("-") - 1])
            #course = (c.string)
            courses.append(course)
            counter += 1
    print("[Log]: {} course titles gathered in {:.2f} secs!".format(counter, perf_counter() - start))
    return courses

# Get Courses
def getCourses(links, courses):
    # Course Name, Prerequisites, Corequisites
    output = []
    output.append(["COURSE NAMES", "COREQUISTES", "PREREQUISTES"])
    start = perf_counter()
    print("[Log]: Getting course infos...")
    counter = 0
    for l in links:
        r = requests.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        sites = soup.text.replace('\n\n','\n').strip('\n').split("EXIT")
        for site in sites:
            linecounter = -1
            course = "N/A"
            corenum = 0
            prenum = 0
            lines = site.split("\n")
            for line in lines:
                linecounter += 1
                if line[:line.find("-")-1] in courses:
                    course = line[:line.find("-")-1]
                if "Corequisites:" in line:
                    corenum = linecounter
                if "Prerequisites:" in line:
                    prenum = linecounter
            if course != "N/A":
                counter += 1
                thiscourse = ["N/A", "N/A", "N/A"]
                #print("Course: " + course)
                thiscourse[0] = course
                if corenum > 0:
                    #print("Coreq: " + lines[corenum + 1])
                    thiscourse[1] = lines[corenum + 1]
                if prenum > 0:
                    #print("Preq: " + lines[prenum + 1])
                    thiscourse[2] = lines[prenum + 1]
                #print("\n\n")
                output.append(thiscourse)
    print("[Log]: {} course infos gathered in {:.2f} secs!".format(counter, perf_counter() - start))
    return output


# Entry Point
def main():
    soup = getSoup()
    links = getLinks(soup)
    courses = getCourseTitles(links)
    output = getCourses(links, courses)
    saveOutput("output.txt", output)

if __name__ == "__main__":
    main()
