"""
https://leetcode.com/problems/merge-strings-alternately/
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedword = ""
        for i in range(min(len(word1),len(word2))):
            mergedword = mergedword + word1[i] + word2[i]
        if len(word1) < len(word2):
            mergedword = mergedword + word2[i+1: len(word2)]
        if len(word1) > len(word2):
            mergedword = mergedword + word1[i+1: len(word1)]
        return mergedword