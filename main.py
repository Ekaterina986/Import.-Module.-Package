from application import salary
from application.db import people
from datetime import date

def get_datetime():
    curent_date = date.today()
    print(curent_date)

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    get_datetime()
