def is_lucky(ticket_number):
    even = sum([int(ticket_number[i]) for i in range(len(ticket_number) // 2)])
    odd = sum([int(ticket_number[i]) for i in range(len(ticket_number) // 2, len(ticket_number))])

    return even == odd


def get_ticket_status(ticket_number):
    return 'Счастливый' if is_lucky(ticket_number) else 'Обычный'


print(get_ticket_status(input()))
