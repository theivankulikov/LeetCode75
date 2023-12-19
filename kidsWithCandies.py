"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = list()
        maxCandies = max(candies)
        for i in range(len(candies)):
            if maxCandies <= candies[i] + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result


def test_Solution():
    assert Solution().kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True]
    assert Solution().kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False]
    assert Solution().kidsWithCandies([12,1,12], 0) == [True,False,True]