class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        sorted_items=sorted(count.items(),key=lambda x:x[1],reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result