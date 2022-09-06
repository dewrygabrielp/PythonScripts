import datetime

def generate_dates(start_date, end_date):
    td = datetime.timedelta(hours=24)
    current_date = start_date
    while current_date <= end_date:
        print current_date
        current_date += td

start_date = datetime.date(2021, 1, 25)
end_date = datetime.date(2022, 3, 5)
generate_dates(start_date, end_date)