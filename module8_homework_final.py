'''
Вам нужно реализовать полезную функцию для вывода списка коллег, которых надо поздравить с днём рождения на неделе.

У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday. Такая структура представляет модель списка пользователей с их именами и днями рождения. name — это строка с именем пользователя, а birthday — это datetime объект, в котором записан день рождения.

Ваша задача написать функцию get_birthdays_per_week, которая получает на вход список users и выводит в консоль (при помощи print) список пользователей, которых надо поздравить по дням.

Условия приёмки
get_birthdays_per_week выводит именинников в формате:
Monday: Bill, Jill
Friday: Kim, Jan

Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник.
Для отладки удобно создать тестовый список users и заполнить его самостоятельно.
Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
Неделя начинается с понедельника.
'''

from datetime import datetime, timedelta

users = {
    'Nancy': '05/26/1988',
    'Malcolm': '05/28/1974',
    'Sydney': '05/22/1991',
    'Rose': '05/23/1986',
    'Felix': '05/23/1985',
    'Grayson': '04/23/1987',
    'Mila': '05/01/1994',
    'Timothy': '05/02/1994',
    'Eric': '05/01/1984',
    'Alice': '05/25/1988',
    'Jack': '04/25/1993',
    'Jhon': '04/27/1994',
    'Tom': '05/26/1988',
    'Jason': '05/22/1989',
    'Alex': '05/23/1991',
    'Mike': '05/24/1985'    
}

def get_birthdays_per_week(users):
    
    # створюємо словник, де ключ - дні поточного тижня, значення - імена юзерів з ДН поточного тижня
    birthdays_by_weekday = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
           
    # отримуємо поточну дату
    today = datetime.today().date()    
    # визначаємо день тижня поточної дати (понеділок = 0, вівторок = 1, і т.д.)
    today_day_of_week = today.weekday()
    
    # отримуємо дату понеділка поточного тижня
    current_monday = today - timedelta(days=(4 - today_day_of_week))
    # print(current_monday)

    # отримуємо дату п'ятниці поточного тижня
    current_friday = current_monday + timedelta(days=4)
    # print(current_friday)    

    # отримуємо дату суботи попереднього тижня
    previous_saturday = current_monday - timedelta(days=2)
    # print(previous_saturday)

    # отримуємо дату неділі попереднього тижня
    previous_sunday = current_monday - timedelta(days=1)
    # print(previous_sunday)
    
    # ітеруємося по кожному юзеру в словнику users
    for user, birthday in users.items():
        # перетворюємо рядок з датою народження в об'єкт datetime
        bday_datetime = datetime.strptime(birthday, '%m/%d/%Y')
        # щоб порівнювати дні народження з поточною датою, встановлюємо рік народження таким же, як поточний рік
        bday_datetime = bday_datetime.replace(year=today.year)
        # обчислюємо день тижня дня народження
        bday_weekday = bday_datetime.strftime('%A')
        if bday_datetime.date() >= current_monday and bday_datetime.date() <= current_friday:
            birthdays_by_weekday[bday_weekday].append(user)
        elif bday_datetime.date() == previous_saturday or bday_datetime.date() == previous_sunday:
            birthdays_by_weekday['Monday'].append(user)
        
    # виводимо список юзерів за днями тижня
    for weekday, users in birthdays_by_weekday.items():
        if users:
            print(f'{weekday}: {", ".join(users)}')             
    

get_birthdays_per_week(users)