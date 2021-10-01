This test has been completed as a part of a screening process for a software development company.

Few notes about the code in QA-Test file: 

The test case for "Bad Password" scenario was implemented before the "Correct Password" scenario
In total 5 test cases were written up  - please refer to the comments sections in the code before each test case for more information
For all the elements found by Xpath, an explicit wait time method could be used to wait until each element becomes .clickable(), yet for the sake of simplicity and making the code more neat, implicit wait time (5) was used
For the last 3 test cases, the assert method was used for the page title since no matter what info was entered in the search section for Hotels, 'No Results' were showing. 

You may find below the instructions in order to set up the environment:

Step 1
*To be ran on Windows OS*
Install Python 3
Install Pycharm

Set the environment variable PATH to location where Python 3 is installed (including separate paths for root, scripts and lib folders) 

Install prereq Python modules by:

1) command line - 
		>python -m pip install selenium
OR
2) instal selenium module through PyCharm in settings


Step 2
Install browser drivers.

To download the Chrome driver, go to https://sites.google.com/a/chromium.org/chromedriver/downloads.

(Unzip and) Move the executable driver file to a location that PATH env variable points to (such as /usr/local/bin).

Step 3
Run the QA-Test.py file with Pycharm and execute the code