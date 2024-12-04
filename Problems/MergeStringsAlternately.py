class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        longest_word = max(word1, word2, key=len)
        shortest_word = min(word1, word2, key=len)

        for i in range(len(shortest_word)):
            merged += word1[i]
            merged += word2[i]

        merged += longest_word[len(shortest_word):]

        return merged
    
    
if __name__ == '__main__':
    word1 = 'abcd'
    word2 = 'pq'
    
    print(Solution().mergeAlternately(word1, word2)) # Output: 'apbqcd'