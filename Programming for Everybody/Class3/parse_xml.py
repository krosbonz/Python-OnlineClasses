
import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide ="yes"/>
    </person>'''
#The "fromstring" function takes the XML and puts it into a format in memory Python can use
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
#"tree.find('name')" looks for the XML structure tag "name"
#The ".text" gets the actual information between the tags. In this case "Chuck"
print('Attr:', tree.find('email').get('hide'))
#Same as the print line above for the "tree.find('email')"
#".get('hide')" retrieves the attribute for "email" and returns "yes"



