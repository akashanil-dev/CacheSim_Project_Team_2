# Direct Mapping Cache Simulation

def direct_mapping_cache(blocks, cache_size):
    cache = [-1] * cache_size
    hits = 0
    misses = 0

    print("Initial Cache State:", cache)
    print("-" * 50)

    for block in blocks:
        index = block % cache_size

        if cache[index] == block:
            hits += 1
            status = "HIT"
        else:
            misses += 1
            cache[index] = block
            status = "MISS"

        print(f"Block {block} -> Cache Line {index} : {status}")
        print("Cache:", cache)
        print("-" * 50)

    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    print("Final Results")
    print("Total Hits   :", hits)
    print("Total Misses :", misses)
    print("Hit Ratio    :", round(hit_ratio, 2))


# Sample Input
cache_size = 4
block_sequence = [0, 4, 1, 4, 2, 3, 4]

direct_mapping_cache(block_sequence, cache_size)
