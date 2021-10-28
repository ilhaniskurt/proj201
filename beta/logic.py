#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

# Local Modules
import parser
import re

def displayDicts(dict):
    for course, conditions in dict.items():
        print(f"{course} : {conditions}")

# Format catalog into logic statements
def formatCourses(dict):
    courses = {}
    for a in dict:
        # Strip Unnecessary Words
        temp = a[2].replace(" ", "").replace("MinimumGradeofD","").replace("MinimumGradeofS","").replace("level","").replace("Undergraduate","").replace("Masters", "").replace("Doctorate","").replace(">Pre-requisite","").replace(">Pre-requiste","")
        # Add Logic Operators
        temp = temp.replace("or","|").replace("and","&")
        courses[a[0]] = temp
    return courses

#function to find errors (if prerequesities don't exist in catalog)
def findingErrors(dict):
  errors={}
  checker=0
  for course, conditions in dict.items():
    if conditions not in dict.keys():
      if "|" in conditions or "&" in conditions:
        conditions= re.findall(r"[\w']+", conditions)
        checker=1
        for condition in conditions:
          if condition not in dict.keys():
            errors[course]=conditions
            break
      if checker == 0:
        errors[course]=conditions
  return errors


#function to find errors (if prerequisites repeat itself in one course)
def findingDuplicates(dict):
  duplicates={}
  for course, conditions in dict.items():
    if "|" in conditions or "&" in conditions:
      conditions= re.findall(r"[\w']+", conditions)
      if conditions[0]==conditions[1]:
        duplicates[course]=conditions
  return duplicates

# Find Imminent Dependencies
def findDependencies(dict):
    dependencies = {}
    for course ,conditions in dict.items():
        if conditions.find("&") != -1 and conditions.find("|") == -1 and conditions.find("N/A") == -1:
            dependencies[course] = conditions
    return dependencies

# Entry Point
def main():
    output = parser.getPickle(parser.PICKLE_NAME)
    courses = formatCourses(output)

    dependencies = findDependencies(courses)
    displayDicts(dependencies)
    
    print('Courses containing prerequesite(s) that don\'t exist in Catalog: ')
    displayDicts(findingErrors(courses))
    print('Courses containing duplicates in "Prerequesite" sections: ')
    displayDicts(findingDuplicates(courses))

if __name__ == "__main__":
    main()
