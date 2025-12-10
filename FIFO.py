def simulate_fifo_cache(cache_size, references):
    cache = []
    hits = 0
    misses = 0

    print("\n--- FIFO Cache Simulation ---")
    print(f"Cache size: {cache_size}")
    print(f"Reference string: {references}")
    print("-" * 40)
    print("{:<8} {:<8} {:<6} {:<20}".format("Step", "Block", "Result", "Cache Content"))
    print("-" * 40)

    for step, block in enumerate(references, start=1):
        if block in cache:
            # HIT
            hits += 1
            result = "HIT"
        else:
            # MISS
            misses += 1
            result = "MISS"

            if len(cache) < cache_size:
                # There is still space, just add it
                cache.append(block)
            else:
                # FIFO: remove the oldest (front of list) and then add new block
                cache.pop(0)
                cache.append(block)

        print("{:<8} {:<8} {:<6} {:<20}".format(step, block, result, str(cache)))

    total = len(references)
    hit_ratio = hits / total if total > 0 else 0

    print("-" * 40)
    print(f"Total references : {total}")
    print(f"Total hits       : {hits}")
    print(f"Total misses     : {misses}")
    print(f"Hit ratio        : {hit_ratio:.2f}")

    # Return values if you want to use programmatically
    return hits, misses, hit_ratio, cache


if __name__ == "__main__":
    # Take user input
    cache_size = int(input("Enter cache size: "))

    ref_str = input(
        "Enter sequence of memory block references (space-separated, e.g. '1 2 3 1 4 5'): "
    )
    references = [int(x) for x in ref_str.split() if x.strip() != ""]

    simulate_fifo_cache(cache_size, references)
