#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

import parser

def displayCourses(array):
    for key, value in array.items():
        print(f"{key} : {value}")

def formatCourses(array):
    courses = {}
    for a in array:
        # Strip Unnecessary Words
        temp = a[2].replace(" ", "").replace("MinimumGradeofD","").replace("level","").replace("Undergraduate","").replace("Masters", "").replace("Doctorate","")
        # Add Logic Operators
        temp = temp.replace("or","|").replace("and","&")
        courses[a[0]] = temp
    return courses

# Entry Point
def main():
    output = parser.getPickle(parser.PICKLE_NAME)
    displayCourses(formatCourses(output))

if __name__ == "__main__":
    main()