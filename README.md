Welcome to SI507 Project 1 repository!

Project Overview:
  This project is mainly to test the skills of writing test cases in Python.
Implementation of the rubrics are already given. Students only need to write test
cases for all functions. Test cases should be written before looking at the implementation of code.


Description of the files:
 1. SI507F17_projects1_tests.py
    All test cases are contained in this file.

 2. code_description_507F17project1
    The description of each class and function in SI507F17_project1_cards.py.

 3. SI507F17_project1_cards.py
    Implementation of code.

 4. helper_functions.py
    All helper functions used in implementation are included here.

 5. requirements.txt
    All libraries except standard library that need to be installed before running this code. 


Other things to notice:
  This code is written and implemented under python version 3.6. I suggest using virtual environment to run this code. See below to follow the instructions of setting up virtual environment and running the test file.

   $ cd to-the-directory-that-contains-files-for-this-project
 //set-up
   $ virtualenv --python=python3.6 name-of-the-virtual-environment

 //activate the virtual environment
   $ source name-of-the-virtual-environment/bin/activate

 //You are in the virtual environment. First, install all libraries needed  
   (virtualenv)$ pip install -r requirements.txt 

 //Run the test files to see the bug of the original implementation 
   (virtualenv)$ python SI507F17_projects1_tests.py  
   .
   .
   .
 //deactivate the virtual environment
   (virtualenv)$ deactivate 

