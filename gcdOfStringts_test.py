import gcdOfStrings

def test_positive_values():
    test_object = gcdOfStrings.gcdOfStringsSolution()
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
    test_object = gcdOfStrings.gcdOfStringsSolution()
    assert test_object.checkStringForDivider("ab", "ab") == True
    assert test_object.checkStringForDivider("abab", "ab") == True
    assert test_object.checkStringForDivider("abc", "ab") == False
    assert test_object.checkStringForDivider("ac", "ab") == False
    assert test_object.checkStringForDivider("abababa", "ab") == False
    assert test_object.checkStringForDivider("ac", "a") == False
    assert test_object.checkStringForDivider("ab", "abab") == False