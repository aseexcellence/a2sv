class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Get the number of words in the list
        num_words = len(words)
        # Create a list to store the bitmask representation of each word
        masks = [0] * num_words
      
        # Generate a bitmask for each word where bit i is set if the 
        # word contains the i-th letter of the alphabet
        for i, word in enumerate(words):
            for ch in word:
                masks[i] |= 1 << (ord(ch) - ord('a'))
      
        # Initialize max_product to 0
        max_product = 0
      
        # Compare every pair of words to find the maximum product of lengths
        # of two words which have no characters in common (no common bits in the bitmask).
        for i in range(num_words - 1):
            for j in range(i + 1, num_words):
                if masks[i] & masks[j] == 0:  # No common characters
                    # Update max_product if this pair has a larger product
                    max_product = max(max_product, len(words[i]) * len(words[j]))
                  
        # Return the maximum product found
        return max_product