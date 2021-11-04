#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

# Local Modules
from parser import getPickle, savePickle, saveOutput
from logic import fixDuplicates, fixEmpty
from sorter import findDuplicates

def displayDicts(dict):
    for course, conditions in dict.items():
        print(f"{course} : {conditions}")

# Entry Point
def main():
    # Current course dictionary version 2 (applied fixEmpty & fixDuplicates)
    courses = getPickle("courses2")
    displayDicts(getPickle("ghosts"))

if __name__ == "__main__":
    main()