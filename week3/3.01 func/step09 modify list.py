def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]
