def problem1_4(miles):
    if isinstance(miles, int):
        total_feet = miles * 5280
        print("There are "+ str(total_feet) + " feet in "+ str(miles) + " miles.")
    else:
        print("Enter a valid number")
