Notes: 'CD' command allows you to change into specific directories. Example: 'CD ~' command gets you to the home folder where you will start your installs

Need to install PIP and Python to use this script 
Type "python" into a Command Prompt window to install Python

To launch the Command Prompt window:
Press Windows Key + X.
Click Run.
Type in cmd.exe and hit enter.

(curl https://www.python.org/ftp/python/3.7.0/python-3.7.0-embed-amd64.zip)


Step 1: Download PIP get-pip.py. Enter the following command in a Command Prompt window:
(curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py)

Step 2: To install PIP type in the following in a Command Prompt window:
python get-pip.py

PIP installation should start. If the file isn’t found, double-check the path to the folder where you saved the file.

Step 3: Download zip from GitHub

Step 4: Resolve dependency issues: 'CD' into setup.py location, and run the following command:
python setup.py install --home=~

--------------------------------------------------------------------------------------------------------------

RUNNING THE PYTHON SCRIPT:

Step 1: Download zip from GitHub (Green "Download Code" box in repo home)

Step 2: Extract files from zip using File Explorer

Step 3: Run the Python command in a Command Prompt window
'python C:\Users\<YOUR USER NAME>\Downloads\rf-main\rf-main\src\recency_frequency.py'

NOTE: If you have downloaded this before, it will append the rf-main folder with '(1)', make sure the 'rf-main' folder after the 'Downloads' folder reads the same (no need to chnage second 'rf-main' folder name

Once complete, find the MembershipRecencyFrequency_w_Product.csv in the src folder (C:\Users\<YOUR USER NAME>\Downloads\rf-main\rf-main\src>)



