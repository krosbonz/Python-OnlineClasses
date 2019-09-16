#! python3

# Line above should be added for each .py file. it is called a "shebang".

# Run Python as batch file;
# @py c:\blah\blah...\something.py %*

# The "@py" tells Windows to run Python and the .py file without printing anything out to the command window
# The "%*" tells Windows to allow the passing of any arguments

# The below script will run a .py which will open a browser to Google Maps and pass in the arguments for an address
# mapit.py 120 main st
import sys, webbrowser, pyperclip

sys.argv 
# "sys.argv" tells the py script to accept arguments after the .py file 

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
# So the above line says if more than one argument passed, concatinate into a single string with a space separating each
# We start at "[1:]" because we don't want to include mapeit.py
# mapit.py '120' 'main' 'st' concatinates into mapit.py '120 main st'
else:
    address = pyperclip.paste()
# If no address is passed as an argument paste the information from the clipboard  

webbrowser.open('https://google.com/maps/place/' + address)
# Open browser and add the address either from passed arguments or from the clipboard

