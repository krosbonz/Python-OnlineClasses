# Join
test = ''.join(['stuff', ' and ', 'things'])
print(test)
# Output
# stuff and things

test2 = 'ing'.join(['turkeystuff', ''])
print(test2)
# Output
# turkeystuffing


# Split
test = 'wacka-wacka-wacka'
test.split('-')
# Output
# ['wacka', 'wacka', 'wacka']


# Partition - Breaks a string down into three parts
'unforgettable'.partition('forget')
# Output
# ('un', 'forget', 'table')

departure, separator, arrival = "London:Edinburgh".partition(':')
# Output
>>> departure
'London'
>>> arrival
'Edinburgh'

# NOTE: '_' can be used instead of separator