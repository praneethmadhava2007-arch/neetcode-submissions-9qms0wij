class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, open_count, close_count):
            # If we've used all 2*n brackets
            if len(s) == 2 * n:
                ans.append(s)
                return

            # Add '(' if we still have some left
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans