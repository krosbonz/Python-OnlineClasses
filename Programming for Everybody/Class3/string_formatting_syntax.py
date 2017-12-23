name_for_userid = {
    214:'bruce',
    344:'steve',
    567:'james',
    }

#Using "%s"
def greeting(userid):
    return "Hi %s!" % name_for_userid[userid]

greeting(214)
#Output
'Hi Bruce!'
#Notice the "%s" is replaced by whatever is passed after the "%" symbol

#Other options
"Hello %s, my name is %s" % ('john', 'mike')
#Output
'Hello john, my name is mike'

#Using %d - for integers instead of strings
"Hello %s, I am %d years old" % ('Steve', 12)


#The %s has actually been replaced by the str.format method
"Hello {}, my name is {}".format('john', 'mike')
#Output
'Hello john, my name is mike'.

"{1}, {0}".format('world', 'Hello')
#Output
'Hello, world'

"{greeting}, {}".format('world', greeting='Hello')
#Output
'Hello, world'
