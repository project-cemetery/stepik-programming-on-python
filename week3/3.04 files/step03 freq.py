def get_cool_word(l):
    d = dict()

    for s in l:
        words = s.lower().split()
        for w in words:
            if w in d.keys():
                d[w] += 1
            else:
                d[w] = 1
        m_key = w

    m_val = d[m_key]

    for key, value in d.items():
        if value > m_val:
            m_key = key
            m_val = value
        if value == m_val:
            if key < m_key:
                m_key = key
                m_val = value

    result = m_key + ' ' + str(m_val)

    return(result)


lst = list()
with open('data/step03.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lst.append(line)

s = get_cool_word(lst)

with open('output/step03.txt', 'w') as f:
    f.write(s)
