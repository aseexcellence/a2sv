class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        total_shifts = sum(shifts) % 26  # Calculate total shifts needed, wrapping around 26
        result = []
        for i in range(n):
            shifted_char = chr((ord(s[i]) - ord('a') + total_shifts) % 26 + ord('a'))
            result.append(shifted_char)
            total_shifts = (total_shifts - shifts[i]) % 26  # Adjust total shifts for next character
        return ''.join(result)
