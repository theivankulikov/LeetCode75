from canPlaceFlowers import Solution

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