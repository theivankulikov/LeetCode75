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
