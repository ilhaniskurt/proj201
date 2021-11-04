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

## "sorter.py"
* __Function:__ The script that creates additional dictionaries depending on context

* __Local Modules Used:__
  * "parser.py"
  * "coursenodes.py"

## "coursesnodes.py"
* __Function:__ Systematize the courses

# Credits:
* "parser.py" - İlhan Yavuz İskurt
* "sorter.py" - İlhan Yavuz İskurt & Muslim Malsagov
* "coursenodes.py" - İlhan Yavuz İskurt

# Acknowledgements:
"parser.py" is based and improved upon "kkkk.py" which was written by Mete Harun Akçay (meteharun@sabanciuniv.edu)

