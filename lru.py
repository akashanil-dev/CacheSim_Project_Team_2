cache_size = int(input("Enter cache size: "))
cache = []
hits = 0
misses = 0
def access_page(page):
     global hits, misses
     if page in cache:
        cache.remove(page)   # remove old position
        cache.append(page)   # move to most recently used
        hits += 1
        print(f"Page {page} accessed → HIT")
     else:
        misses += 1
        print(f"Page {page} accessed → MISS")
        if len(cache) == cache_size:
            removed = cache.pop(0)   # remove least recently used
            print("Removed LRU page:", removed)
        cache.append(page)

# Example access sequence
pages = [1, 2, 3, 1, 4, 5]

for p in pages:
    access_page(p)
    print("Cache:", cache)
    total_requests = hits + misses
hit_ratio = hits / total_requests if total_requests != 0 else 0

#final results
print("\nTotal Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hit_ratio)
