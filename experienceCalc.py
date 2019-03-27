"""
    This program calculates the age/experience in years, months, and days format

    Input:
    Asks the user to enter a date in YYYY-MM-DD format

    Output:
    Calculates and prints the experience in years, months, and days
"""


from datetime import date
from dateutil.relativedelta import relativedelta


def exp_calc():
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    from_date = date(year, month, day)
    now = date.today()
    r_delta = relativedelta(now, from_date)
    print("Your experience is: {} years, {} months, and {} days".format(r_delta.years, r_delta.months, r_delta.days))


if __name__ == "__main__":
    exp_calc()
