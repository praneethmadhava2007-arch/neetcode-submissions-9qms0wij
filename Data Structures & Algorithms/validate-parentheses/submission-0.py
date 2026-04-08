class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={")":"(","}":"{","]":"["}
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic:
                if not stack or stack[-1]!=dic[i]:
                    return False
                stack.pop()  
        return not stack