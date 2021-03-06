#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

# Local Modules
from .parser import getPickle, parseCatalog, savePickle, saveOutput
from .logic import formatCourses, fixRedundancies, fixLoops, fixGhosts

# Internal Libraries
from time import perf_counter

def displayDicts(dict):
    for course, conditions in dict.items():
        print(f"-----------------\nCourse Name: {course}\nPrerequisites: {conditions}\n-----------------")

# This is the function called from run.py
def main():
    # Start Runtime
    start = perf_counter()
    
    parseCatalog() # Parse the html and save it as "course_list". You can comment out this code if you ran it once.
    catalog_list = getPickle("catalog_list") # Parsed html output from the function: "parseCatalog".
    catalog_dict, syntax_errors = formatCourses(catalog_list) # Format courses into logic statements.
    catalog_dict2 = fixLoops(catalog_dict) # Fix courses that require themselves without recursive search.
    catalog_dict_with_ghosts = fixRedundancies(catalog_dict2) # Remove redundant prerequisites.
    catalog_dict_without_ghosts, ghost_errors = fixGhosts(catalog_dict_with_ghosts) # Solve courses involving ghost prerequisites.
    
    
    # Display the catalog dictionary to the terminal
    displayDicts(catalog_dict_with_ghosts) # Replace with the catalog dictionary you want to display.
    
    
    # End Runtime
    print("Script have finished in {:.4f} sec(s).".format(perf_counter() - start))
