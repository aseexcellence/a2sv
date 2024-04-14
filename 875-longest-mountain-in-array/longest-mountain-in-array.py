class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        i = 1  # start from the second element

        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                right = i
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                max_len = max(max_len, right - left + 1)
                i = right
            else:
                i += 1

        return max_len
