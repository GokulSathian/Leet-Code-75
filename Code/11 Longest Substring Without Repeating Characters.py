    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        max_length = 0
        start_index = 0
        char_index_map = {}  # Stores the last seen index of each character

        for end_index in range(n):
            current_char = s[end_index]

            # If the character is already in our map AND its last seen index
            # is within the current window (i.e., >= start_index),
            # we need to move the start_index of our window.
            if current_char in char_index_map and char_index_map[current_char] >= start_index:
                # Move start_index to the right of the previous occurrence
                # of the current_char to exclude the duplicate.
                start_index = char_index_map[current_char] + 1
            
            # Update the last seen index of the current character
            char_index_map[current_char] = end_index
            
            # Calculate the length of the current window and update max_length
            current_length = end_index - start_index + 1
            max_length = max(max_length, current_length)
            
        return max_length


"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
