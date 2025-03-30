from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list[dict]:
    result = []
    now = datetime.today().date()
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=now.year)
        if birthday < now :
            birthday = birthday.replace(year=now.year+1)
        
        if (birthday - now).days <= 7:
            if birthday.weekday() == 5:
                birthday += timedelta(days=2)
                
            if birthday.weekday() == 6:
                birthday += timedelta(days=1)
            birthday = birthday.strftime("%Y.%m.%d")

            result.append({'name': user["name"], 'congratulation_date': birthday})

    return result            


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "XXXX Smith", "birthday": "1991.04.05"},
    {"name": "YYYY Smith", "birthday": "1991.04.06"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)



