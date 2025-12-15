## Algorithm: FIFO Cache Replacement Simulation

**Step 1:** Start

**Step 2:** Read the cache size `cache_size`

**Step 3:** Read the sequence of memory block references into an array `references`

**Step 4:** Initialize  
- An empty list `cache`  
- Variables `hits = 0` and `misses = 0`

**Step 5:** Set `i = 0`

**Step 6:** Repeat steps **7 to 11** until `i = length of references`

**Step 7:** If `references[i]` is present in `cache`  
- Increment `hits` by 1

**Step 8:** Else  
- Increment `misses` by 1

**Step 9:** If the cache is not full  
- Insert `references[i]` at the end of the cache

**Step 10:** Else  
- Remove the oldest block from the cache (FIFO)  
- Insert `references[i]` at the end of the cache

**Step 11:** Display the current memory block, HIT or MISS, and cache contents  
- Increment `i` by 1

**Step 12:** Compute the hit ratio as  
`hit_ratio = hits / total number of references`

**Step 13:** Display total hits, total misses, and hit ratio

**Step 14:** Stop
