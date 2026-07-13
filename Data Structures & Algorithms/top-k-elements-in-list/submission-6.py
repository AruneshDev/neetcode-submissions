class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count={}
        for num in nums:
            freq_count[num]=1+freq_count.get(num,0)
        return heapq.nlargest(k, freq_count.keys(), key=freq_count.get)