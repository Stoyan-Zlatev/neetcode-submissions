from heapq import heappop, heappush, heapify

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #[4,2,3,1], k = 3
        #4,2,3 => 4
        # 2,3,1 => 3
        # use heap pop until something is in the list
        m_heap = []
        heapify(m_heap)
        curr_window = {}
        for i in range(k):
            curr_window[nums[i]] = curr_window.get(nums[i], 0) + 1
            heappush(m_heap, -(nums[i]))

        result = [-m_heap[0]]
        for i in range(k, len(nums)):
            curr_window[nums[i-k]]-=1
            curr_window[nums[i]] = curr_window.get(nums[i], 0) + 1
            heappush(m_heap, -nums[i])
            while not curr_window[-m_heap[0]] > 0:
                heappop(m_heap) 
            result.append(-m_heap[0])

        return result
