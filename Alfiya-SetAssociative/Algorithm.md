
START
Initialize cache[S][K] = EMPTY
hit = 0
miss = 0

FOR each block B in reference_list:
    set_index = B % S
    target_set = cache[set_index]

    IF B in target_set:
        hit = hit + 1
        UPDATE replacement order
    ELSE:
        miss = miss + 1
        IF target_set has empty slot:
            INSERT B into empty slot
        ELSE:
            REPLACE block using LRU/FIFO
            INSERT B

    PRINT cache state

END FOR

hit_ratio = hit / (hit + miss)
PRINT hit, miss, hit_ratio
END
