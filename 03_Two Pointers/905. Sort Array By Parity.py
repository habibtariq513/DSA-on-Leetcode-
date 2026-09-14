class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            # If the left number is even, it's correctly placed. Move right.
            if nums[l] % 2 == 0:
                l += 1
            # If the right number is odd, it's correctly placed. Move left.
            elif nums[r] % 2 != 0:
                r -= 1
            # Both are out of place (left is odd, right is even). Swap them.
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        return nums
