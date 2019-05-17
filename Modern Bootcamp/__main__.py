# Running this script in python using this method;
# python3 import scriptName 


from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

# Will produce no output until you call the defined function;
# scriptName.fetch_words()
# Or
# from scriptName import fetch_words
# Then run;
# fetch_words()

# This doesn't produce output if you run it from command line;
# c:\> python scriptName.py


# In Python, underscore name equals underscore main when a .py file is run directly from
# the local .py file. When a .py is imported from another .py file it is no longer underscore name. It is
# instead the name of the imported .py file 
if __name__ == '__main__':
    fetch_words()
# In this instance, run as the current file, the fetch_words()function will run.
# If this is imported by a different .py file it will not run until the function
# is specifically called. 

# Standard format;
# def main():


# if __name__ == '__main__':
#     main()


