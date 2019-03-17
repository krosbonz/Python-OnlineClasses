# Return all examples of a specific string

import re

resume = '''Amanda K. Getajob 430 Park Ln., Milford, IL 60953      815-555-5555 852-996-9656 854-874-8535     getajob@msu.edu      www.linkedin.com/akgetajob 
 
EDUCATION  Michigan State University, East Lansing, MI        May 2018  Eli Broad College of Business Bachelor of Arts, Supply Chain Management  Minor in International Business Major GPA: 3.75/4.00; Cumulative GPA: 3.35/4.00               Sparty Foundation Scholarship Recipient; Dean’s List: 3 Semesters 
 
             International Business Study Abroad, Western Europe                                                                           May 2016  
 
PROFESSIONAL EXPERIENCE General Motors, Detroit, MI  June – Aug. 2016  Supply Chain Intern ● Increased next-day deliveries of dealer referral orders by 50 lines per month, impacting 100 dealers in North America through the creation of a new order pulling process ● Executed a regional $100,000 materials budget to reduce the expense of required materials ● Managed relationships with 3 suppliers to ensure a collaborative relationship and maximize the interactions ● Presented potential cost-savings plan to 12 upper level executives for further review  
 
 EY, Chicago, IL                    May – Aug. 2015  Core Tax Intern ● Collaborated with a team of 6 interns and professional staff to complete compliance work, finishing 4 weeks ahead of the budgeted schedule  ● Provided tax compliance services on an international, federal, state, and local to multiple clients, including trusts and multinational corporations  ● Developed an Excel workbook to expedite the preparation process resulting in time saving in excess of 150 hours 
 
OTHER RELATED EXPERIENCE Michigan State University Culinary Services, East Lansing, MI                Jan. 2015 – Present Student Cook  ● Provided courteous and prompt customer service to guests in a dining hall for approximately 7,500 ● Attained full responsibility for completion of daily projects of front-kitchen team and supervision of 4 other co-workers in the front kitchen ● Mentored a novice prep chef in basics of food preparation until she attained sufficient competence to be independent contributor to team ● Ensured all service and preparation areas were kept clean and met sanitation standards 
 
Lindow’s Lawns, Milford, IL              Summers 2014, 2015 Exterior Designer ● Increased revenue by over 9% by implementing “Sunday Special” lawn care promotion ● Designed and implemented a training program to onboard 4 new staff members  ● Managed and held responsibility for balancing daily cash flow of $300 
 
ACTIVITIES & SKILLS MSU Supply Chain Management Association, Vice President Aug. 2016 – Present Phi Chi Theta, Professional Business Fraternity, Member    Aug. 2014 – Present Deloitte Financial Accounting Case Competition, Participant   Aug. 2015 – June 2016 Chinese and English Language, Fluent Bloomberg Certified in Equities and Commodities '''

resume_reg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume_reg.findall(resume)

# Output
['815-555-5555', '852-996-9656', '854-874-8535']

# Break phone number into groups by area code and local number
resume_reg = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
[('815', '555-5555'), ('852', '996-9656'), ('854', '874-8535')]
# Using groups creates tuples

# Adding an overall group that includes the entire string as well as the group tuple
resume_reg = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
[('815-555-5555', '815', '555-5555'), ('852-996-9656', '852', '996-9656')
, ('854-874-8535', '854', '874-8535')]
# A tuple for each group will be created for each matching string
