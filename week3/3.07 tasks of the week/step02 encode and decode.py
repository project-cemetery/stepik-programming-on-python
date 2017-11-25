def ende_code(s, encode, a_from, a_to):
    code = dict()

    if encode:
        tmp = a_from
        a_from = a_to
        a_to = tmp

    for i in range(len(a_from)):
        code[a_from[i]] = a_to[i]

    result = ''

    for c in s:
        result += code[c]

    return result

or_alf = input()
co_alf = input()

or_str = input()
co_str = input()

print(ende_code(or_str, False, or_alf, co_alf))
print(ende_code(co_str, True, or_alf, co_alf))
