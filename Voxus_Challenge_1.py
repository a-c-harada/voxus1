#Error codes and their warning for the user
def return_error(error_code):
    match error_code:
        case 1:
            print("Input not formatted as date")
        case 2:
            print("- Invalid value for year\n")
        case 3:
            print("- Invalid value for month\n")
        case 4:
            print("- Invalid value for day\n")

#Returns how many days in each month of an year, checking for leap years
def days_in_months(year):
    months = []
    for month in range(1,12):
        if month in [1,3,5,7,10,12]:
            months.append(31)
        elif month in [4,6,8,9,11]:
            months.append(30)
        elif (year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)):
            months.append(29)
        else:
            months.append(28)
    return months



format_example = "\nDate format expected:\nYYYY-MM-DD\nYear between 1900 and 2022\n"
errors_found = []

#Gets user input and splits it in three
raw_date = input("Input: ")
split_date = raw_date.split("-")

#Not obtaining three parts causes an error
if (len(split_date) != 3):
    return_error(1)
    print(format_example)
    exit()

#Checks if input was all digits before processing them
year = -1
month = -1
day = -1
if (len(split_date[0]) != 4 or not split_date[0].isdigit()):
    errors_found.append(2)
else:
    year = int(split_date[0])

if (len(split_date[1]) != 2 or not split_date[1].isdigit()):
    errors_found.append(3)
else:
    month = int(split_date[1])

if (len(split_date[2]) != 2 or not split_date[2].isdigit()):
    errors_found.append(4)
else:
    day = int(split_date[2])

#Validates if values are within range
if (year != -1 and ()):
    errors_found.append(2)
if (month != -1 and (month < 1 or month > 12)):
    errors_found.append(3)
else:
    month_days = days_in_months(year)
    if (day != -1 and (day < 1 or day > month_days[month-1])):
        errors_found.append(4)

#Any errors found are returned to the user at the same time
if (len(errors_found) > 0):
    print("Invalid input. Errors found:\n")
    for error in errors_found:
        return_error(error)
    print(format_example)
else:
    #Calculates how many days passed since the start of the year
    total_days = day
    for month_index in range(month-1):
        total_days += month_days[month_index]
    print("Output: " + str(total_days))
