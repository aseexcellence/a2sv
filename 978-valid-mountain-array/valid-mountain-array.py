class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr.count(max(arr)) > 1:
            return False
        peak = max(arr)
        peakIndex = arr.index(peak)
        l = r = True
        if peakIndex == len(arr) - 1 or peakIndex == 0:
            return False
        for i in range(len(arr) - 1):
            if i < peakIndex:
                if arr[i] >= arr[i + 1]:
                    l = False
            elif i > peakIndex:
                if arr[i] <= arr[i + 1]:
                    r = False
        return l and r