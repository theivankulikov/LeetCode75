"""
https://leetcode.com/problems/can-place-flowers/
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        i = 2
        while i < len(flowerbed):
            if flowerbed[i - 2] != 1 and flowerbed[i - 1] != 1 and flowerbed[i] != 1:
                n -= 1
                i += 2
                if n <= 0:
                    return True
            elif flowerbed[i - 2] == 1:
                i += 1
            elif flowerbed[i - 1] == 1:
                i += 2
            elif flowerbed[i] == 1:
                i += 3
            else:
                i += 1
        return False
    
Solution().canPlaceFlowers(["a",0,0,1,0], 1)

def test_canPlaceFlowers():
    assert Solution().canPlaceFlowers([1,0,0,0,1], 1) == True
    assert Solution().canPlaceFlowers([1,0,0,0,1], 2) == False
    assert Solution().canPlaceFlowers([1,0,1,0,1], 1) == False
    assert Solution().canPlaceFlowers([0,0,1,0,1], 1) == True
    assert Solution().canPlaceFlowers([0,1,0,0,1], 1) == False
    assert Solution().canPlaceFlowers([0,1,0,0,1], 2) == False
    assert Solution().canPlaceFlowers([0,0,0,0,1], 2) == True
    assert Solution().canPlaceFlowers([0,0,0,0,1], 3) == False
    assert Solution().canPlaceFlowers([1,0,0,0,0], 1) == True
    assert Solution().canPlaceFlowers([1,0,0,0,0], 2) == True
    assert Solution().canPlaceFlowers([1,0,0,0,0], 3) == False
    assert Solution().canPlaceFlowers([1,0,0,0,0,0], 3) == False
    assert Solution().canPlaceFlowers([1,0,0,0,0,0], 2) == True
    assert Solution().canPlaceFlowers([1,0], 1) == False
    assert Solution().canPlaceFlowers([1,0], 0) == True
    assert Solution().canPlaceFlowers([1,0,0], 1) == True
    assert Solution().canPlaceFlowers([1,0,1], 1) == False
    assert Solution().canPlaceFlowers([1,0,0,0], 1) == True
    assert Solution().canPlaceFlowers([1,0,0,1], 1) == False
    assert Solution().canPlaceFlowers([1,0,0,0,0], 1) == True
    assert Solution().canPlaceFlowers([1,0,0,0,1], 1) == True
    assert Solution().canPlaceFlowers([1,1,0,0,1], 1) == False
    assert Solution().canPlaceFlowers([1,1,0,1,1], 1) == False
    assert Solution().canPlaceFlowers([1,0,0,1,1], 1) == False
    assert Solution().canPlaceFlowers([0,1,0,0,1], 1) == False
    assert Solution().canPlaceFlowers([1,0,0,1,0], 1) == False
    assert Solution().canPlaceFlowers(["a",0,0,1,0], 1) == True
    assert Solution().canPlaceFlowers(["a",0,0,"a",0], 1) == True

    