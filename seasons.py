""" Get user input of a month and day and
print the season of that day"""
# 16 Nay 2023

months = {'January': 31,
          'February': 28,
          'March': 31,
          'April': 30,
          'May': 31,
          'June': 30,
          'July': 31,
          'August': 31,
          'September': 30,
          "October": 31,
          "November": 30,
          'December': 31}

# Get user input
month = input()
day = int(input())

# Validate input
if (month in months and  # Input is a valid month
        1 <= day <= months[month]):  # Day number is in range for that month

    # Identify the days in winter
    if ((month == 'December' and day >= 21) or  # Some of the month is in winter
            (month == 'January') or  # All the days are in winter
            (month == 'February') or  # All the days are is in winter
            (month == 'March' and day <= 19)):  # Some of the month is in winter
        print('Winter')  # Print season

    # Repeat for each season
    if ((month == 'March' and day >= 20) or
            (month == 'April') or
            (month == 'May') or
            (month == 'June' and day <= 20)):
        print('Spring')

    if ((month == 'June' and day >= 21) or
            month == 'July' or
            month == 'August' or
            (month == 'September' and day <= 21)):
        print('Summer')

    if ((month == 'September' and day >= 22) or
            month == 'October' or
            month == 'November' or
            (month == 'December' and day <= 20)):
        print('Autumn')
else:
    print('Invalid')
