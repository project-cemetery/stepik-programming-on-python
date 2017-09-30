def get_word(n, word_base):
    endings = {
        'nominative':      '',
        'genitive':        'а',
        'plural_genitive': 'ов'
    }

    result = str(n) + ' ' + word_base

    if 11 <= n % 100 <= 19 or n % 10 > 4:
        result += endings['plural_genitive']
    elif n % 10 == 1:
        result += endings['nominative']
    elif 2 <= n % 10 <=4:
        result += endings['genitive']

    return result


print(get_word(int(input()), 'программист'))
