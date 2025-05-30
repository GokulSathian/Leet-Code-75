class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # (start, end) inclusive indices of the longest palindrome found so far
        # Initialize with the first character, length 1
        longest_palindrome_start = 0
        max_len = 1

        # Helper function to expand around a center
        # It updates longest_palindrome_start and max_len if a longer palindrome is found
        def expand_around_center(left: int, right: int):
            nonlocal longest_palindrome_start, max_len # To modify variables in the outer scope
            
            # Expand while characters match and we are within bounds
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    longest_palindrome_start = left
                
                left -= 1
                right += 1

        # Iterate through all possible centers
        for i in range(n):
            # Odd length palindromes: center is s[i]
            # e.g., for "aba", center is 'b' (i)
            # left pointer starts at i, right pointer starts at i
            expand_around_center(i, i)

            # Even length palindromes: center is between s[i] and s[i+1]
            # e.g., for "abba", center is between 'b' and 'b' (i, i+1)
            # left pointer starts at i, right pointer starts at i+1
            # No need to check if i+1 is out of bounds for `right` initially,
            # because the `while right < n` in `expand_around_center` handles it.
            expand_around_center(i, i + 1)
            
        return s[longest_palindrome_start : longest_palindrome_start + max_len]


        """
        
        Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
        """
        