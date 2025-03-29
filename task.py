from datetime import datetime


def get_days_from_today(date: str):
    today = datetime.today()
    datetime_object = datetime.strptime(date, "%Y-%m-%d")
    result = today - datetime_object
    return result.days


res = get_days_from_today('2020-10-09')
print(res)
