#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

# Replaces empty values in the dictionary with "N/A"
def fixEmpty(courses:dict):
    fixedDict = courses
    for course, conditions in courses.items():
        if conditions == "" or conditions == " " or conditions == "  ": fixedDict[course] = "N/A"
    return fixedDict

# Replaces consecutive courses with single course (Does not work perfectly need to run it several times)
def fixDuplicates(courses:dict, duplicates:dict):
    fixedDict = courses
    for course, conditions in courses.items():
        if course in duplicates.keys():
            for duplicate in duplicates[course]:
                res = [i for i in range(len(conditions)) if conditions.startswith(duplicate, i)]
                if len(res) == 2:
                    fixedDict[course] = conditions[:res[0]] + conditions[res[1]:]
    return fixedDict

def fixGhosts():
    pass

def fixLoops():
    pass

# Entry Point
def main():
    pass

if __name__ == "__main__":
    main()