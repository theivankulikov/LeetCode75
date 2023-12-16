"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""

class gcdOfStringsSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        starting_intersection = ""

        for i in range(0, min(len(str1), len(str2)) + 1):
            if str1[:i] == str2[:i]:
                starting_intersection = str1[:i]
            else:
                break
        
        if len (starting_intersection) == 0:
            return ""
        
        gcd = ""
        for k in range(1, len(starting_intersection) + 1):
            if self.checkStringForDivider(str1, starting_intersection[:k]) and self.checkStringForDivider(str2, starting_intersection[:k]):
                gcd = starting_intersection[:k]

        return gcd


    def checkStringForDivider(self, in_str:str, divider:str):
        if len(in_str) % len(divider) != 0:
             return False
        l_divider = len(divider)
        j = 0
        while j < len(in_str):
            if divider != in_str[j:j + l_divider]:
                return False
            j = j + l_divider
        return True
    


def test_positive_values():
    test_object = gcdOfStringsSolution()
    assert test_object.gcdOfStrings("abcdef", "abcdef") == "abcdef"
    assert test_object.gcdOfStrings("abcdefg", "abcdef") == ""
    assert test_object.gcdOfStrings("abcdef", "abcdefg") == ""
    assert test_object.gcdOfStrings("", "") == ""
    assert test_object.gcdOfStrings("a", "") == ""
    assert test_object.gcdOfStrings("", "a") == ""
    assert test_object.gcdOfStrings("ab", "abab") == "ab"
    assert test_object.gcdOfStrings("abab", "ab") == "ab"
    assert test_object.gcdOfStrings("ab", "aba") == ""
    assert test_object.gcdOfStrings("aba", "ab") == ""
    assert test_object.gcdOfStrings("ababa", "ab") == ""
    assert test_object.gcdOfStrings("ab", "ababa") == ""
    assert test_object.gcdOfStrings("ababab", "abab") == "ab"

def test_checkStringForDivider():
    test_object = gcdOfStringsSolution()
    assert test_object.checkStringForDivider("ab", "ab") == True
    assert test_object.checkStringForDivider("abab", "ab") == True
    assert test_object.checkStringForDivider("abc", "ab") == False
    assert test_object.checkStringForDivider("ac", "ab") == False
    assert test_object.checkStringForDivider("abababa", "ab") == False
    assert test_object.checkStringForDivider("ac", "a") == False
    assert test_object.checkStringForDivider("ab", "abab") == False