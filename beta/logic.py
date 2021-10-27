#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

import parser

def displayCourses(array):
    for course, conditions in array.items():
        print(f"{course} : {conditions}")

def formatCourses(array):
    courses = {}
    for a in array:
        # Strip Unnecessary Words
        temp = a[2].replace(" ", "").replace("MinimumGradeofD","").replace("level","").replace("Undergraduate","").replace("Masters", "").replace("Doctorate","")
        # Add Logic Operators
        temp = temp.replace("or","|").replace("and","&")
        courses[a[0]] = temp
    return courses

# Find Imminent Dependencies
def findDependencies(array):
    dependencies = {}
    for course ,conditions in array.items():
        if "&" in conditions:
            if "|" not in conditions:
                dependencies[course] = conditions
        if conditions.find("&") != -1 and conditions.find("|") != -1 and conditions.find("N/A")!= -1:
            dependencies[course] = conditions
    return dependencies

# Entry Point
def main():
    output = parser.getPickle(parser.PICKLE_NAME)
    courses = formatCourses(output)
    displayCourses(findDependencies(courses))

if __name__ == "__main__":
    main()