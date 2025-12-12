START

Input: cache_size, block_size, associativity, mapping_type, replacement_policy, memory_reference_list

IF mapping_type = DIRECT:
    sets = cache_size
    associativity = 1
ELSE IF mapping_type = SET_ASSOCIATIVE:
    sets = cache_size / associativity
ELSE IF mapping_type = FULLY_ASSOCIATIVE:
    sets = 1
    associativity = cache_size

Initialize cache as 2D list of sets

FOR each address in memory_reference_list:
    block = address // block_size
    set_index = block % sets
    tag = block // sets

    IF tag exists in cache[set_index]:
        HIT++
        Update replacement data (LRU/LFU)
    ELSE:
        MISS++
        IF cache[set_index] has free space:
            Insert tag
        ELSE:
            Replace block using selected replacement policy
                FIFO → remove oldest
                LRU → remove least recently used
                LFU → remove least frequently used
    PRINT cache contents

Compute hit_ratio = hits / total_access

PRINT hits, misses, hit_ratio

STOP
