class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()
        i, k, n = 0, 0, len(s)

        while i < n:
            # Find the starting pos of the next word
            while i < n and s[i] == " ": i += 1

            if i != n and k > 0: # Still have the next word, add " " here
                s[k] = " "
                k += 1

            start_index = k
            # Find the ending pos of that word
            while i < n and s[i] != " ":
                s[k] = s[i]
                i += 1
                k += 1
                
            # Reverse that word
            self.reverse(s, start_index, k-1)
            
        s = s[:k]
        return "".join(s)
    
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

""""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""
"""