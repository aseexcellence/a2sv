class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0 # count the number of 1s
        consecutive_1s = [] # list to put the time 1s appear consecutively
        for num in nums:
            if (num == 1):
                count += 1
            else:
                consecutive_1s.append(count)
                count = 0   # reset the count
        consecutive_1s.append(count) # append the last count
        
        # find the maximum number of consecutive 1s
        max = consecutive_1s[0]
        for c in consecutive_1s:
            if (max < c):
                max = c
        return max

if __name__ == '__main__':
    # Create an instance of the Solution class
    solution = Solution()

    # Provide a sample input list (replace with your desired input)
    nums = [1, 1, 0, 1, 1, 1]

    # Call the findMaxConsecutiveOnes method and print the result
    max_consecutive_ones = solution.findMaxConsecutiveOnes(nums)
    print("Maximum consecutive ones:", max_consecutive_ones)
