cache_size = int(input("Enter cache size: "))
cache = []

def access_page(page):
    if page in cache:
        cache.remove(page)   # remove old position
        cache.append(page)   # move to most recently used
        print(f"Page {page} accessed → HIT")
    
    