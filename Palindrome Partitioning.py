# Time Complexity : O(n * 2^n)
# Space Complexity : O(length of nums array)

# The code ran on LeetCode

# Start pivot at index 0. Check for all the palindromic sub strings that start at index 0. Add all these to the path and move pivot to the index that comes after the palindrome string ends. Repeat the process from the new pivot. When pivot is at len(nums), append the path to result, and backtract to find other possible solutions

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def check_palindrome(st):
        
            l = 0; r = len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                l+=1
                r-=1
            return True

        def helper(s, pivot, path):
            nonlocal res
            # Base
            if pivot == len(s):
                copy = [p for p in path]
                res.append(copy)
                return

            # Logic
            # Search for palindromes starting at the pivot
            for i in range(pivot, len(s)):
                sub = s[pivot:i+1]

                if check_palindrome(sub):
                    path.append(sub)
                    helper(s, i+1, path)
                    path.pop()
        helper(s, 0, [])                    
        return res