cache_size = int(input("Enter cache size: "))
cache = []

def access_page(page):
    if page in cache:
        cache.remove(page)   # remove old position
        cache.append(page)   # move to most recently used
        print(f"Page {page} accessed → HIT")
    else:
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
