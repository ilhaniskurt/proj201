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

# Remove ghost courses out of the prerequisites (Not finisihed)
def fixGhosts(courses:dict, ghosts:dict):
    fixedDict = courses
    for course, conditions in courses.items():
        if course in ghosts.keys():
            for ghost in ghosts[course]:
                # If the only condition is a ghost
                if conditions == ghost:
                    fixedDict[course] = "N/A"
                    continue
                i = conditions.find(ghost)
                # If ghost course is isolated in parenthesis
                if ghost[i-1] == "(" and ghost[i+len(ghost)+1] == ")": 
                    fixedDict[course] = conditions[:i-2] + conditions[i+2:]
                    continue
                for operator in ["&","|"]:
                    # If ghost course is surrounded with same logic operators
                    if ghost[i-1] == operator and ghost[i+len(ghost)+1] == operator:
                        fixedDict[course] = conditions[:i-2] + conditions[i+1:]
                        continue
                        
                    #different case scenarios
                    #if ghost course between '(' and operator
                    if ghost[i-1] == "(" and ghost[i+len(ghost)+1] == operator:
                        fixedDict[course] = conditions[:i-1] + conditions[i+2:]
                        continue
                    #if ghost course between operator and ")"
                    if ghost[i-1] == operator and ghost[i+len(ghost)+1] == ")":
                        fixedDict[course] = conditions[:i-2] + conditions[i+1:]
                        continue
                    #if none of previous if are satisfiable it will check the last 2 
                    #if ghost course without "(", but just operator after it
                    if ghost[i+len(ghost)+1] == operator:
                        fixedDict[course] = conditions[i+2:]
                        continue
                    #if ghost course is in the end but without ")" and only operator before it
                    if ghost[i-1] == operator :
                        fixedDict[course] = conditions[:i-2]
                        continue
        # NOTE Remember to check for logic operators that does not have courses on both sides (parenthesis does not count) and remove them
    return fixedDict

def fixLoops(courses:dict, loops:dict):
    fixedDict = courses
    return fixedDict

# Entry Point
def main():
    pass

if __name__ == "__main__":
    main()
