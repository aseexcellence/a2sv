class Solution:
    def compress(self, chars: List[str]) -> int:
        i, index = 0, 0
        while i < len(chars):
            char = chars[i]
            count = 0
            # Count occurrences of the same char
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            chars[index] = char
            index += 1
            # Store the count if more than 1
            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1
    
        return index
