#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#
#   Additions made by Muslim Malsagov
#

# External Libraries
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# Format catalog into logic statements
def formatCourses(list:list):
    courses = {}
    errors = {} 
    for a in list:
        # Strip Unnecessary Words
        temp = a[2].replace(" ", "").replace("MinimumGradeofD","").replace("MinimumGradeofS","").replace("level","").replace("Undergraduate","").replace("Masters", "").replace("Doctorate","").replace(">Pre-requisite","").replace(">Pre-requiste","")
        # HUM fixes
        temp = temp.replace("HUM>UNVMajorWorks", "")
        # Add Logic Operators
        temp = temp.replace("or","|").replace("and","&")
        temp = "N/A" if temp == "" or temp == " " or temp == "  " else temp
        try:
            if temp != "N/A": temp = parse_expr(temp)
        except:
            errors[a[0].replace(" ", "")] = temp
        else:
            courses[a[0].replace(" ", "")] = temp
    return courses, errors

# Find courses that require themselves
def fixLoops(courses:dict):
    for course, conditions in courses.items():
        if course in str(conditions):
            if course == str(conditions):
                courses[course] = "N/A"
            else:
                print("ERROR: Unexpected loops")
    return courses

# Fix 1: Remove ghost courses out of the prerequisites
def fixGhosts(courses:dict):
    errors = {}
    fixed = courses.copy()
    for course, conditions in courses.items():
        tmp = ""
        conditions = str(conditions)
        ghosts = []
        if conditions == "N/A": continue
        for t in str(conditions).replace(" ", "").replace("(",",").replace(")",",").replace("|",",").replace("&",",").replace(",,,",",").replace(",,",",").split(","):
            if t != "" and t not in courses.keys():
                tmp = conditions.replace(t, "False")
                ghosts.append(t)
        if tmp != "":
            if tmp == "False": 
                errors[course] = [conditions, ghosts]
                fixed.pop(course)
            else:
                fixed[course] = parse_expr(tmp)
    return fixed, errors

# Solve Redundancies
def fixRedundancies(courses:dict):
    exprs_dict = expressify(courses)
    for course, conditions in exprs_dict.items():
        tmp = checking(exprs_dict, course, conditions)
        if tmp: courses[course] = parse_expr(tmp)
    return courses

def expressify(courses:dict):
    symbol_dict = {}
    expr_dict = {}
    for course, conditions in courses.items():
        if conditions == "N/A":
            symbol_dict[course] = Symbol("")
        else:
            symbol_dict[course] = Symbol(course)
    for course, conditions in courses.items():
        conditions = str(conditions)
        if conditions == "N/A":
            continue
        else:
            try:
                expr_dict[course] = eval (conditions, symbol_dict)
            except NameError as e:
                ghost = str(e).split("'")[1]
            if "&" not in conditions and "|" not in conditions:
                expr_dict[course] = Symbol(conditions)
            else:
                expr_dict[course] = parse_expr(conditions)
    return expr_dict

def all_implifications(expr_dict, prerequisite, course = None, imp_list = set()):
    if course:
        imp_list.add(course >> prerequisite)
    for sub_course in prerequisite.atoms():
        if isinstance(sub_course, Symbol) and sub_course.name in expr_dict:
            all_implifications(expr_dict,expr_dict[sub_course.name],sub_course,imp_list)
    return imp_list

def checking(expr_dict, course, course_prerequisites):
    tmp = ""
    parts = course_prerequisites.args
    if course_prerequisites == "N/A": return "N/A"
    for i in range (len(parts)):
        a = parts[i]
        b = course_prerequisites.func(*parts[0:i], *parts[i+1: len(parts)])
        orChecker = False
        andChecker = False
        if course_prerequisites.func is Or:
            orChecker = not satisfiable(And(a & ~b, *(all_implifications(expr_dict, a) | all_implifications(expr_dict, b))))
        elif course_prerequisites.func is And:
            andChecker = not satisfiable(And(b & ~a, *(all_implifications(expr_dict, b) | all_implifications(expr_dict, a))))
        if orChecker: tmp = str(course_prerequisites).replace(str(a), "False")
        if andChecker: tmp = str(course_prerequisites).replace(str(a), "True")
    if tmp != "": 
        return tmp