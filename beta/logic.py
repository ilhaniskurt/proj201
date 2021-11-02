#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#
#   Additions made by Muslim Malsagov
#

# Local Modules
import parser
import coursenodes

# Internal Libraries
import re
import collections

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
        courses[a[0].replace(" ", "")] = temp
    return courses

# Function to find ghost courses (if prerequesities don't exist in catalog)
def findGhosts(dict):
    ghosts = {}
    for course, conditions in dict.items():
        conditions = conditions.replace("(", "").replace(")", "").replace(" ","")
        if conditions not in dict.keys():
            if "|" in conditions or "&" in conditions:
                conditions = re.split('[&|]', conditions)
                for condition in conditions:
                    if condition not in dict.keys():
                        ghosts[course] = condition
                        break
    return ghosts

# Function to find errors (if prerequisites repeat itself in one course)
def findDuplicates(dict):
    duplicates = {}
    for course, conditions in dict.items():
        if "|" in conditions or "&" in conditions:
            conditions = re.findall(r"[\w']+", conditions)
            duplicates[course] = [item for item, count in collections.Counter(conditions).items() if count > 1]
            if not duplicates[course]: duplicates.pop(course, None)
    return duplicates

# Find courses that require themselves
def findLoops(dict):
    loops = {}
    for course, conditions in dict.items():
        if course in conditions:
            loops[course] = conditions
    return loops

# Find Imminent Dependencies
def findDependencies(dict):
    dependencies = {}
    for course, conditions in dict.items():
        if conditions.find("&") != -1 and conditions.find("|") == -1 and conditions.find("N/A") == -1:
            dependencies[course] = []
            for condition in conditions.replace("(", "").replace(")", "").split("&"):
                dependencies[course].append(condition)
    return dependencies

# Entry Point
def main():
    output = parser.getPickle(parser.PICKLE_NAME)
    courses = formatCourses(output)

    # parser.saveOutput("coursedict.txt", courses)

    dependencies = findDependencies(courses)
    # ghosts = findGhosts(courses)
    # loops = findLoops(courses)
    # duplicates = findDuplicates(courses)

    expendedDependencies = coursenodes.getExpandedPreqDict(dependencies)
    
    # displayDicts(expendedDependencies)
    print(coursenodes.checkPath(expendedDependencies, "MAT408", "NS101"))

if __name__ == "__main__":
    main()
