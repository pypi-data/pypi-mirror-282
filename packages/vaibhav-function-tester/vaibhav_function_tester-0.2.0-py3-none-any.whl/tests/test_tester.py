import unittest
from vaibhav_function_tester.tester import FunctionTester

def sample_function(cards, query):
    return cards.index(query) if query in cards else -1

class TestFunctionTester(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7},
                "expected_output": 3
            },
            {
                "input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 5},
                "expected_output": -1
            }
        ]
        self.tester = FunctionTester(sample_function, self.test_cases)

    def test_run_tests(self):
        results = self.tester.run_tests()
        for result in results:
            self.assertEqual(result["result"], "PASSED")

    def test_run_test_case(self):
        case = self.test_cases[0]
        result = self.tester.run_test_case(case["input"], case["expected_output"])
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
