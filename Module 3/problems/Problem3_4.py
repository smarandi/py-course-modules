def problem3_4(mon, day, year):
    month_dictionary = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    date = str(month_dictionary[mon]) + "/"+ str(day) + "/" +str(year)
    print(date)
