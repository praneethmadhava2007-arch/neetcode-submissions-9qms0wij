class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=1
        n=len(nums)
        a=[]
        zero_count=nums.count(0)
        for i  in nums:
            if i !=0:
                m*=i
        for i in nums:
            if(zero_count>1):
                a.append(0)
            elif(zero_count==1):
                if i==0:
                    a.append(m)
                else:
                    a.append(0)
            else:
                a.append(m//i)
        return a