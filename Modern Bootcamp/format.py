# Format

"The age of Jim is {0} and the age of Mick is {1}".format(34, 25)
# Output
'The age of Jim is 34 and the age of Mick is 25'
# NOTE: The numbering method can be used more than once in a string

# If the required format is already in order, no num necessary
"The age of jim is {} and the age of Mick is {}.format(34,25)"

# Option 2
"Current position {lat} {long}".format(lat="23N", long="5E")

# Option 3
grd = (65.2, 23.1, 54.6)
'Average grades are student1={grd[0]} student2={grd[1]} student3={grd[2]}'.format(grd=grd)
# Output
'Average grades are student1=65.2 student2=23.1 student3=54.6'

# Option 4
import math
"Math constants: pi={m.pi}, e={m.e}".format(m=math)
# Output
'Math constants: pi=3.141592653589793, e=2.718281828459045'

