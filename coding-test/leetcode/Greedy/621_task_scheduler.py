from typing import List
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)

        max_count = max(counter.values())
        max_item_count = list(counter.values()).count(max_count)
        
        return max(len(tasks), max_count + n*(max_count-1) + max_item_count - 1)