class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        count = 0

        # Helper function to expand from a center and count palindromes
        # It modifies the 'count' variable in the outer scope
        def expand_and_count(left: int, right: int):
            nonlocal count # Allows modification of 'count' from the outer scope
            
            while left >= 0 and right < n and s[left] == s[right]:
                # s[left...right] is a palindrome
                count += 1
                
                # Expand outwards
                left -= 1
                right += 1

        # Iterate through all possible centers
        for i in range(n):
            # Odd length palindromes: center is s[i]
            # e.g., for "aba", center is 'b' (i)
            # left pointer starts at i, right pointer starts at i
            expand_and_count(i, i)

            # Even length palindromes: center is between s[i] and s[i+1]
            # e.g., for "abba", center is between 'b' and 'b' (i, i+1)
            # left pointer starts at i, right pointer starts at i+1
            # The check `right < n` in expand_and_count handles the case where i+1 is out of bounds.
            expand_and_count(i, i + 1)
            
        return count
    
    """"
    Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
    """