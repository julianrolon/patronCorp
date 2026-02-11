# This suite of tests is written to run against your code
# so that we can check its correctness.

import caesar_cipher as program
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "hello"
        offset = 3
        expected = "ebiil"
        result = program.caesar_cipher(string, offset)
        self.assertEqual(expected, result)

    def test_case_2(self):
        string = "apple"
        offset = 0
        expected = "apple"
        result = program.caesar_cipher(string, offset)
        self.assertEqual(expected, result)

    def test_case_3(self):
        string = "abc"
        offset = 20
        expected = "ghi"
        result = program.caesar_cipher(string, offset)
        self.assertEqual(expected, result)

    def test_case_4(self):
        string = ""
        offset = 3
        expected = ""
        result = program.caesar_cipher(string, offset)
        self.assertEqual(expected, result)

    def test_case_5(self):
        string = "a"
        offset = 26
        expected = "a"
        result = program.caesar_cipher(string, offset)
        self.assertEqual(expected, result)

    def test_case_6(self):
        string = "hagshsah"
        offset = 8
        expected = "zsykzksz"
        result = program.caesar_cipher(string, offset)
        self.assertEqual(expected, result)