This branch is currently being worked upon.

# Details about the scripts
## "parser.py"
* __Function:__ Scrap data from a html file

* __External Libraries Used:__
  * BeautifulSoup4, 
  * requests

* __Default Environment Variables:__
  * FILE_DIR = "beta/files",
  * FILE_NAME = "catalog.html",
  * LINK_FILTER = "https://suis.sabanciuniv.edu/prod/bwckctlg.p_disp_course_detail"
  * PICKLE_NAME = "course_data"

## "logic.py"
* __Function:__ Algorithms for logical operations

* __External Libraries Used:__
  * SymPy

## "root.py"
* __Function:__ Main module

* __Local Modules Used:__
  * "parser.py"
  * "logic.py"

# Credits:
* "parser.py" - İlhan Yavuz İskurt
* "logic.py" - İlhan Yavuz İskurt & Muslim Malsagov
* "root.py" - İlhan Yavuz İskurt

# Acknowledgements:
"parser.py" is based and improved upon "kkkk.py" which was written by Mete Harun Akçay (meteharun@sabanciuniv.edu)

