from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}                 # key -> value (just storing the block)
        self.freq = defaultdict(int)    # key -> frequency count
        self.use_order = OrderedDict()  # maintains LRU for same frequency
    
    def access(self, block):
        # Block Hit
        if block in self.cache:
            self.freq[block] += 1
            # Update order (move to most recent)
            if block in self.use_order:
                self.use_order.move_to_end(block)
            return True  # hit
        
        # Block Miss
        if len(self.cache) < self.capacity:
            # Just insert
            self.cache[block] = block
            self.freq[block] = 1
            self.use_order[block] = True
            return False
        
        # Cache is full → apply LFU replacement
        # Step 1: find minimum frequency
        min_freq = min(self.freq.values())
        # Step 2: find all candidates with this frequency
        candidates = [b for b in self.cache if self.freq[b] == min_freq]
        # Step 3: use LRU among candidates
        for b in self.use_order:
            if b in candidates:
                victim = b
                break
        
        # Remove victim
        del self.cache[victim]
        del self.freq[victim]
        del self.use_order[victim]
        
        # Insert new block
        self.cache[block] = block
        self.freq[block] = 1
        self.use_order[block] = True
        
        return False

    def print_state(self):
        print("Cache:", list(self.cache.keys()))
        print("Frequency:", dict(self.freq))
        print("--------------------------------")

def simulate_lfu(cache_size, reference_string):
    lfu = LFUCache(cache_size)
    
    hits = 0
    misses = 0

    print("\n=== LFU Cache Simulation ===\n")
    print("Cache Size:", cache_size)
    print("Reference Sequence:", reference_string)
    print("--------------------------------\n")

    for block in reference_string:
        print(f"Accessing Block: {block}")
        hit = lfu.access(block)
        if hit:
            hits += 1
            print("Result: HIT")
        else:
            misses += 1
            print("Result: MISS")
        lfu.print_state()

    
    print("Total Hits:", hits)
    print("Total Misses:", misses)
    print("Hit Ratio:", round(hits / len(reference_string), 2))
    


# Sample Run
simulate_lfu(cache_size=3, reference_string=[2, 3, 2, 1, 5, 2, 4, 5, 3])
