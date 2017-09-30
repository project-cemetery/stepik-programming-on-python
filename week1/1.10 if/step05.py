def get_sleep_status(min_hours, max_hours, sleep_hours):
    status = ''

    if min_hours <= sleep_hours <= max_hours:
        status = 'Это нормально'
    elif sleep_hours < min_hours:
        status = 'Недосып'
    elif sleep_hours > max_hours:
        status = 'Пересып'

    return status


print(get_sleep_status(int(input()), int(input()), int(input())))
