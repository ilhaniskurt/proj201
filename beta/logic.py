#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

# Local Modules
import parser

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

if __name__ == "__main__":
    main()