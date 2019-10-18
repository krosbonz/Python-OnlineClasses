import bs4, requests
# Import Beautifulsoup and Requests(see web_requests_module)

def temp(tempUrl):
    res = requests.get(tempUrl)
    # Gets the URL
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Scrapes the text from the website
    degrees = soup.select('#current_conditions-summary > p.myforecast-current-lrg')
    local = soup.select('#seven-day-forecast > div.panel-heading > h2')
    # "degrees" and "local" select the CSS element for each webpart from the website (see below for more info)
    return f"The temperature for location: {local[0].text.strip()} is {degrees[0].text.strip()}"
    # soup.select returns a list such as "[<h2 class="panel-title">  3 Miles WSW Exeter NH       </h2>]"
    # Using "[0]" pulls the string from the list, so you have "<h2 class="panel-title">  3 Miles WSW Exeter NH       </h2>"
    # "text.strip()" removes all white space either side of the string

forcast = temp('https://forecast.weather.gov/MapClick.php?lat=42.96436190000003&lon=-70.99677309999998#.XaTK4PmSng')
print(forcast)

# The "soup.select" data comes from the CSS selector of an element of a webpage
# Right click any element and select "Inspect", this will open the browser 's developer tools.
# In the Elements section of the dev tools open find the website element > Right click > Select "Copy Selector"

# Note: This information can be found here;
# https://automatetheboringstuff.com/chapter11/
