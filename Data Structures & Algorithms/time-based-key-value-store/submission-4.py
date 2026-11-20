class TimeMap:

    # {"alices": [("1", "happy"), ("3", "sad")]}
    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # We want to find the max smaller number
        # So we need to set the window as left as possible
        current_list = self.kv[key]
        l, r = 0, len(current_list) - 1
        result = ""
        mid = l + (r - l) // 2
        while l <= r:
            mid = l + (r - l) // 2
            if current_list[mid][0] == timestamp:
                return current_list[mid][1]
            elif timestamp > current_list[mid][0]:
                result = current_list[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result
        
