import unittest
from my_project import secure_function_1, secure_function_2, vulnerable_function

class TestSecureFunctions(unittest.TestCase):
    def test_secure_function_1(self):
        # Test for expected output
        self.assertEqual(secure_function_1("input"), "expected_output")

    def test_secure_function_2(self):
        # Test for expected output
        self.assertEqual(secure_function_2("input"), "expected_output")

    def test_vulnerable_function(self):
        # Test for potential vulnerabilities
        self.assertRaises(ValueError, vulnerable_function, "malicious_input")

if __name__ == '__main__':
    unittest.main()
