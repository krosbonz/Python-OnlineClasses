import requests
# Requests is an HTTP library for HTTP requests 

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code)
print(len(res.text))

open_file = open('temptxt.txt', 'wb')
# Create a file 
for chunk in iter_content(100000):
    open_file.write(chunk)
# Breaks contents of website into chunks and writes them to file
open_file.close()
# Closes the open file

