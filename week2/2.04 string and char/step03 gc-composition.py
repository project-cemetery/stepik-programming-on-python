def get_gc_composition(genome):
    c_cnt = genome.count('c')
    g_cnt = genome.count('g')

    return ((c_cnt + g_cnt) / len(genome)) * 100


print(get_gc_composition(input()))
