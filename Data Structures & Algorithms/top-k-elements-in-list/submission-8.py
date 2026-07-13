class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        total_freq = {}
        for num in nums:
            total_freq[num] = total_freq.get(num, 0) + 1

        # Sort the dictionary by frequency in descending order
        sorted_freq = sorted(total_freq.items(), key=lambda x: x[1], reverse=True)

        # Extract the top k keys
        return [item[0] for item in sorted_freq[:k]]