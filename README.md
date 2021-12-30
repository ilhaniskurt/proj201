# User Manual
## Using juypter notebook:
* Run this repo from mybinder.com and execute run.py (by python ./run.py)

## Running the script locally
* __For macOS users:__
  * Open the terminal (Press space + command and search "terminal")
  * Get to the directory where the repo is located by typing "cd" in the terminal. Ex: "cd /Users/(username)/Documents/proj"
  * Activate the virtual environment by typing "source penv/bin/activate" in the terminal.
  * Execute the python script run.py by "python run.py

* __For Windows Users:__
  * Open the PowerShell  (Press Windows + R and search "powershell")
  * Get to the directory where the repo is located by typing "cd" in the powershell. Ex: "c:\Users\(username)\Documents\proj201"
  * Activate the virtual environment by typing "./penv/bin/Activate.ps1" in the powershell. If doesn't allow look up online how to allow powershell to run remote scripts online.
  * Execute the python script run.py by "python run.py

## __Modifications:__
  * Change the html file in "files/" with the catalog you want to work with. (Do not forget to name it "catalog.html". You can change the default names and directory from the environment variables inside "parser.py")
  * Change the variable inside the displayDicts inside the "scripts/root.py" with the below variables to change the output of the file
    * catalog_dict # Catalog without any alterations
    * catalog_dict2 # Catalog with looping prerequisites removed
    * catalog_dict_with_ghosts # Catalog with redundancies removed
    * catalog_dict_without_ghosts # Catalog with prerequisites that does not exist removed
    * syntax_errors # Courses with prerequisites with broken syntax
    * ghost_errors # Courses that are unable to be taken without ghost courses 


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
  * PICKLE_NAME = "course_list"

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

