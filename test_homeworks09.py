import unittest

from Homework_09.homeworks import number_addition, reverse_string, longest_word,views_func,find_substring


class MyTest(unittest.TestCase):
    def test_number_addition_positive(self):
        result = number_addition(5, 9)
        expected_result = 14
        self.assertEqual(result, expected_result)

    def test_assertion_error(self):
        with self.assertRaises(TypeError):
            result = number_addition(10, "30")

    def test_reverse_string(self):
        s = 'Hello world'
        expected_result = reverse_string(s)
        self.assertEqual(reverse_string(s), expected_result)

    def test_reverse_string_error(self):
        with self.assertRaises(TypeError):
            result = reverse_string(53)

    def test_longest_word(self):
        lw = ["apple", "banana", "cherry", "watermelon", "blueberry"]
        expected_result = longest_word(lw)
        self.assertEqual(longest_word(lw), expected_result)

    def test_longest_word_error(self):
        with self.assertRaises(TypeError):
            result = longest_word(["a",7,5.35])


    def test_views_func(self):
        n = 1272
        expected_result = views_func(n)
        self.assertEqual(views_func(n), expected_result)

    def test_views_func_error(self):
        with self.assertRaises(Exception):
            result = views_func("asd")


    def test_find_substring(self):
        s1 = "Hello world"
        s2 = "world"
        expected_result = 6
        self.assertEqual(find_substring(s1,s2),expected_result)

    def test_find_substring_error(self):
        s1 = "The quick brown fox jumps over the lazy dog"
        s2 = "cat"
        result = find_substring("The quick brown fox jumps over the lazy dog", "cat")
        self.assertEqual(-1, result)



if __name__ == '__main__':
    unittest.main()