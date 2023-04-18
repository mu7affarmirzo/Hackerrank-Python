class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        temp = len(word1) if len(word1) > len(word2) else len(word2)
        new_word = ''
        for i in range(temp):
            if len(word1) > i:
                new_word += word1[i]
            if len(word2) > i:
                new_word += word2[i]
        print(new_word)
a = Solution()

a.mergeAlternately("sd43ghgj", "3sg")
