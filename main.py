
from application.Salary import calculate_salary
from application.db.People import get_employees
from datetime import datetime, date, time

if __name__ == '__main__':
    calculate_salary()
    print(datetime.now())
    get_employees()
    print(datetime.today())