from string_utils import reverse_words, count_vowels, is_palindrome

class TestReverseWords:

    # 正常情况
    def test_two_words(self):
        assert reverse_words("Hello World") == "World Hello"

    def test_three_words(self):
        assert reverse_words("A B C") == "C B A"

    # 边界情况
    def test_single_word(self):
        assert reverse_words("Hello") == "Hello"

    def test_empty_string(self):
        assert reverse_words("") == ""

    # 异常情况
    def test_multiple_spaces(self):
        assert reverse_words("Hello  World") == "World Hello"

    def test_with_numbers(self):
        assert reverse_words("Hello 123") == "123 Hello"

class TestCountVowels:
    
    # 正常情况
    def test_all_vowels(self):
        assert count_vowels("aeiouAEIOU") == 10

    def test_mixed_characters(self):
        assert count_vowels("Hello World") == 3

    # 边界情况
    def test_no_vowels(self):
        assert count_vowels("bcdfg") == 0

    def test_empty_string(self):
        assert count_vowels("") == 0

    # 异常情况
    def test_with_numbers_and_symbols(self):
        assert count_vowels("H3ll0!") == 0
    
    def test_uppercase_vowels(self):
        assert count_vowels("AEIOU") == 5
    
    def test_mixed_case_vowels(self):
        assert count_vowels("aEiOu") == 5


class TestIsPalindrome:
    
    # 正常情况
    def test_is_palindrome(self):
        assert is_palindrome("racecar") == True
    
    def test_not_palindrome(self):
        assert is_palindrome("hello") == False
    
    # 边界情况
    def test_single_character(self):
        assert is_palindrome("a") == True
    
    def test_empty_string(self):
        assert is_palindrome("") == True

    # 异常情况
    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") == True
    
    def test_palindrome_with_mixed_case(self):
        assert is_palindrome("RaceCar") == True
    
    def test_uppercase_palindrome(self):
        assert is_palindrome("MADAM") == True
