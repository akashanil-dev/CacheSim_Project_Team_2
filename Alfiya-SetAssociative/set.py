from collections import deque, defaultdict

class SetAssociativeCache:
    def __init__(self, cache_size, block_size, associativity):
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        
        self.num_sets = cache_size // associativity
        
        self.cache = [deque(maxlen=associativity) for _ in range(self.num_sets)]
        self.lru_counter = [defaultdict(int) for _ in range(self.num_sets)]
        
        self.hits = 0
        self.misses = 0

    def access(self, address):
        block = address // self.block_size
        set_index = block % self.num_sets
        tag = block // self.num_sets
        
        current_set = self.cache[set_index]
        lru = self.lru_counter[set_index]
        
        if tag in current_set:
            self.hits += 1
            print(f"Address {address}: HIT (Set {set_index}, Tag {tag})")
            current_set.remove(tag)
            current_set.append(tag)
            lru[tag] += 1
        else:
            self.misses += 1
            print(f"Address {address}: MISS (Set {set_index}, Tag {tag})")
            if len(current_set) == self.associativity:
                evicted = current_set.popleft()
                print(f"  Evicted Tag: {evicted}")
                del lru[evicted]
            current_set.append(tag)
            lru[tag] += 1

        self.print_cache()

    def print_cache(self):
        print("\nCache State:")
        for i, s in enumerate(self.cache):
            print(f" Set {i}: {list(s)}")
        print("-------------------------------")

    def summary(self):
        total = self.hits + self.misses
        print("\n===== SUMMARY =====")
        print("Total Hits :", self.hits)
        print("Total Misses :", self.misses)
        print("Hit Ratio :", round(self.hits / total, 3))
        print("====================")


# -----------------------
# USER INPUT SECTION
# -----------------------

cache_size = int(input("Enter cache size: "))
block_size = int(input("Enter block size: "))
associativity = int(input("Enter associativity: "))
# create cache
cache = SetAssociativeCache(cache_size, block_size, associativity)

# address input
addresses = list(map(int, input("Enter memory addresses separated by space: ").split()))

# process addresses
for address in addresses:
    cache.access(address)

cache.summary()
