"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = list()
        return result
    

def test_Solution():
    assert Solution().kidsWithCandies([2,3,5,1,3], 3) == [True,False,False,False,False]