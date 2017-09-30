def encode(genome):
    sub_genome = list()
    sub_genome.append(genome[0])
    for i in range(1, len(genome)):
        if genome[i] != genome[i - 1]:
            sub_genome.append(genome[i])
    genome_encoded = ''
    prev_cnt = 0
    for c in sub_genome:
        genome_encoded += c
        cnt = 0
        for i in range(prev_cnt, len(genome)):
            if genome[i] != c:
                break
            else:
                cnt += 1
        prev_cnt += cnt
        genome_encoded += str(cnt)

    return genome_encoded


print(encode(input()))