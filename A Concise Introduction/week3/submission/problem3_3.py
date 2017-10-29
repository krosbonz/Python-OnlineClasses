def problem3_3(month, day, year):
    day_ = str(day)
    year_ = str(year)
    
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "December")
    
    stuff = month - 1
    month_ = str(months[stuff])
    print(month_,day_+", "+year_)