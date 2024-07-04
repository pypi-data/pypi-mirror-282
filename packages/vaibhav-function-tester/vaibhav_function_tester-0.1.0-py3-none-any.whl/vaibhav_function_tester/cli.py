import argparse
import json
from .tester import FunctionTester

def main():
    parser = argparse.ArgumentParser(description="Function Tester CLI")
    parser.add_argument("function_module", help="Module containing the function to test (e.g., sample_module.sample_function)")
    parser.add_argument("test_cases_file", help="JSON file containing the test cases")

    args = parser.parse_args()

    with open(args.test_cases_file, "r") as f:
        test_cases = json.load(f)

    module_name, function_name = args.function_module.rsplit('.', 1)
    module = __import__(module_name, fromlist=[function_name])
    function = getattr(module, function_name)

    tester = FunctionTester(function, test_cases)
    results = tester.run_tests()

    for result in results:
        print(f"Input: {result['input']}")
        print(f"Expected Output: {result['expected_output']}")
        print(f"Actual Output: {result['actual_output']}")
        print(f"Execution Time: {result['execution_time']:.3f} ms")
        print(f"Test Result: {result['result']}\n")

if __name__ == "__main__":
    main()
