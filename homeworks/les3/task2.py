"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def contact_form(first_name, second_name, year, city, email, phone):
    """
    print contacts of user
    :param first_name: string
    :param second_name: string
    :param year: int
    :param city: string
    :param email: string
    :param phone: int
    :return: None
    """
    print(f'Имя: {first_name} Фамилия: {second_name} Год рождения: {year} Город:{city} email:{email} Телефон:{phone}')
    

contact_form(first_name='Test', second_name='Testov', year=2000, city='Irkutsk', email='test@mail.ru', phone='88888333')