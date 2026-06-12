class Solution:

    def encode(self, strs: List[str]) -> str:
        r=''
        for i in strs:
            r+='-'+i
        return r
    def decode(self, s: str) -> List[str]:
        d=s.split('-')[1:]
        return d