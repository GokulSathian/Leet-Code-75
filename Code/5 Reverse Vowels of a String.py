class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set of vowels for quick lookup
        s_list = list(s)  # Convert string to a list for in-place modification
        left, right = 0, len(s_list) - 1  # Initialize two pointers

        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]  # Swap vowels
                left += 1
                right -= 1
            elif s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1

        return "".join(s_list)  # Convert list back to a string
    



""""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""