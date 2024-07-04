import importlib
import os
import json

import importlib
import time

class FunctionTester:
    def __init__(self, function, test_cases):
        """
        Initialize the FunctionTester with a function and test cases.

        :param function: Function to be tested
        :param test_cases: List of test cases, each test case is a dictionary
                           with 'input' and 'expected_output' keys
        """
        self.function = function
        self.test_cases = test_cases

    def run_tests(self):
        """
        Run all the tests in the test cases.

        :return: List of dictionaries with test details and results
        """
        results = []
        for i, case in enumerate(self.test_cases):
            input_data = case['input']
            expected_output = case['expected_output']
            result = self.run_test_case(input_data, expected_output)
            results.append(result)
        return results

    def run_test_case(self, input_data, expected_output):
        """
        Run a single test case.

        :param input_data: Input data for the function
        :param expected_output: Expected output from the function
        :return: Dictionary with test case details and result
        """
        try:
            start_time = time.time()
            result = self.function(**input_data)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # in milliseconds

            test_result = {
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": result,
                "execution_time": execution_time,
                "result": "PASSED" if result == expected_output else "FAILED"
            }
            return test_result
        except Exception as e:
            return {
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": None,
                "execution_time": None,
                "result": f"ERROR: {e}"
            }


