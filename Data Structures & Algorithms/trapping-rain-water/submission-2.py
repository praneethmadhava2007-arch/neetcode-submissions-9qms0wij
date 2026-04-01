class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n
        leftmax[0]=height[0]
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i])
        rightmax[n-1]=height[n-1]
        for i in range(n-2,0,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        total=0
        for i in range(n):
            if(height[i]<leftmax[i] and height[i]<rightmax[i]):
                total+=min(leftmax[i],rightmax[i])-height[i]
        return total
