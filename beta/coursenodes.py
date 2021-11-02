#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

# Internal Libraries
from collections import deque

# Adding a course to the node dictionary (with first degree prerequisites) 
def addCourse(courseNodes:dict, courseName:str, *args):
    if courseName not in courseNodes:
        courseNodes[courseName] = []
    if args:
        for dependency in args:
            courseNodes[courseName].append(dependency)

def getExpandedPreqDict(courseNodes:dict):
    courses = courseNodes
    for course, dependencies in courses.items():
        if dependencies:
            for dependency in dependencies:
                if dependency in courses.keys():
                    [   courses[course].append(i) 
                        for i in courses[dependency] 
                        if i not in courses[course]     ]
    return courses

def checkPath(courseNodes:dict, courseName:str, coursePre:str):
    return (coursePre in courseNodes[courseName] if courseName in courseNodes.keys() else False)

def findReachableCourses():
    pass

# Entry Point
def main():
    pass

if __name__ == "__main__":
    main()