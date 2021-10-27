#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

import parser

def displayCourses(array):
  for course in array:
    for index in course:
      print(index, end="/ | /")
    print("")

def formatCourses(array):
  newarray = array
  for courses in newarray:
    courses.append(courses[2][courses[2].find("level") + 7:courses[2].find("Minimum") - 1])
  return newarray

# Entry Point
def main():
  output = parser.getPickle(parser.PICKLE_NAME)
  displayCourses(formatCourses(output))

if __name__ == "__main__":
    main()