def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_year_status(year):
    if is_leap_year(year):
        year_status = 'Високосный'
    else:
        year_status = 'Обычный'

    return year_status


print(get_year_status(int(input())))
