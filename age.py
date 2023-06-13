from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year


    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age


birth_date = date(1990, 5, 20)
age = calculate_age(birth_date)
print(f"The user's age is {age} years.")