from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(open("beta/catalog.html", encoding="utf-8"), "html.parser")
linkler = soup.find_all("a")
necessary_links = []

courses = []
for link in linkler:
    if "https://suis.sabanciuniv.edu/prod/bwckctlg.p_disp_course_detail" in str(link.get("href")):
        necessary_links.append(link.get("href"))



counter = 0;
for x in necessary_links:
    r = requests.get(x)
    newsoup = BeautifulSoup(r.content, "html.parser")
    newlinks = newsoup.find_all("td")
    for l in newsoup.find("td",attrs = {"class":"nttitle"}):


        counter += 1
        mycourse = l.string[:l.string.find("-")-1]

        print(str(counter) + ". " + mycourse)
        courses.append(mycourse)

print("Ders sayısı: ")
print(counter)



print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
newcounter = -1
for l in necessary_links:
    prelinks = requests.get(l)
    prerequisite_soup = BeautifulSoup(prelinks.content, "html.parser")
    otherlinks = prerequisite_soup.find_all("a")
    newcounter += 1
    sentences = prerequisite_soup.text
    sentences = sentences.replace('\n\n', '\n')
    sentences = sentences.strip('\n')
    sites = sentences.split("EXIT")

    for site in sites:
        lines = site.split("\n")
        linecounter = -1
        thecourse = "None"
        corenum = 0
        prenum = 0
        for line in lines:
            linecounter += 1
            if line[:line.find("-")-1] in courses:
                thecourse = line[:line.find("-")-1]
            if "Corequisites:" in line:
                corenum = linecounter
            if "Prerequisites:" in line:
                prenum = linecounter
        if thecourse != "None":
            print("Course: " + thecourse)
            if corenum > 0:
                print("Coreq: " + lines[corenum + 1])
            if prenum > 0:
                print("Preq: " + lines[prenum + 1])
            print("\n\n")










print(newcounter)
print("bitti")
