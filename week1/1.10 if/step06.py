def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_year_status(year):
    return 'Високосный' if is_leap_year(year) else 'Обычный'


print(get_year_status(int(input())))
