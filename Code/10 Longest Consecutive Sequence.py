class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle the edge case of an empty list.
        if not nums:
            return 0

        # Convert the list to a set for O(1) average time complexity for lookups.
        # This step takes O(n) time and space.
        num_set = set(nums)
        
        longest_streak = 0

        # Iterate through each unique number.
        # The key idea is that we only start counting a sequence from its smallest element.
        for num in num_set:
            # Check if the current number is the start of a sequence.
            # A number 'num' is a start of a sequence if 'num-1' is not in num_set.
            # This check ensures that we only build sequences from their smallest element,
            # avoiding redundant computations.
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # If 'num' is a start, then count the length of the consecutive sequence
                # by checking for 'current_num + 1', 'current_num + 2', and so on.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak found so far.
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
    


    """"
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
    """
    ""