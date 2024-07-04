# Vaibhav Function Tester

Vaibhav Function Tester is a comprehensive Python package designed to test functions with specified inputs and expected outputs. This package streamlines the process of validating functions, providing detailed test results, and offering a convenient command-line interface (CLI) for easy testing directly from the terminal.

## Features

- **Automated Testing**: Seamlessly run multiple test cases on a specified function.
- **Detailed Results**: Receive thorough information on each test case, including input, expected output, actual output, execution time, and the test result.
- **Command-Line Interface**: Effortlessly run tests from the terminal with the CLI.
- **Customizable**: Easily integrate with any function and test case format.

## Installation

You can install the Vaibhav Function Tester package using pip:

```sh
pip install vaibhav_function_tester



## Usage

### Importing and Using in a Script

To use the package, define the function you want to test and create a list of test cases. Each test case should be a dictionary with `input` and `expected_output` keys.

#### Sample Function

Suppose you have a function that finds the index of a query element in a list of cards:

```python
def sample_function(cards, query):
    return cards.index(query) if query in cards else -1
```

#### Test Cases

Create a list of test cases:

```python
test_cases = [
    {
        "input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7},
        "expected_output": 3
    },
    {
        "input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 5},
        "expected_output": -1
    }
]
```

#### Running the Tests

Use the `FunctionTester` class to run the tests and print the results:

```python
from vaibhav_function_tester.tester import FunctionTester

tester = FunctionTester(sample_function, test_cases)
results = tester.run_tests()

for result in results:
    print(f"Input: {result['input']}")
    print(f"Expected Output: {result['expected_output']}")
    print(f"Actual Output: {result['actual_output']}")
    print(f"Execution Time: {result['execution_time']:.3f} ms")
    print(f"Test Result: {result['result']}\n")
```

### Using the CLI

The Vaibhav Function Tester package includes a command-line interface (CLI) for running tests directly from the terminal.

1. **Create a JSON file** with your test cases. Save it as `test_cases.json`:

    ```json
    [
        {
            "input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7},
            "expected_output": 3
        },
        {
            "input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 5},
            "expected_output": -1
        }
    ]
    ```

2. **Run the CLI** with the function module and test cases file as arguments:

    ```sh
    function_tester sample_module.sample_function test_cases.json
    ```

    The CLI will output the detailed results for each test case.

## Examples

Here are some example usages of the Vaibhav Function Tester:

### Example 1: Testing a Simple Addition Function

#### Function to Test

```python
def add(a, b):
    return a + b
```

#### Test Cases

```python
test_cases = [
    {
        "input": {"a": 1, "b": 2},
        "expected_output": 3
    },
    {
        "input": {"a": -1, "b": 1},
        "expected_output": 0
    }
]
```

#### Running the Tests

```python
from vaibhav_function_tester.tester import FunctionTester

tester = FunctionTester(add, test_cases)
results = tester.run_tests()

for result in results:
    print(f"Input: {result['input']}")
    print(f"Expected Output: {result['expected_output']}")
    print(f"Actual Output: {result['actual_output']}")
    print(f"Execution Time: {result['execution_time']:.3f} ms")
    print(f"Test Result: {result['result']}\n")
```

### Example 2: Using the CLI to Test a Function

1. **Function Module (math_operations.py)**

    ```python
    def multiply(a, b):
        return a * b
    ```

2. **Test Cases JSON File (multiply_test_cases.json)**

    ```json
    [
        {
            "input": {"a": 3, "b": 4},
            "expected_output": 12
        },
        {
            "input": {"a": -1, "b": -1},
            "expected_output": 1
        }
    ]
    ```

3. **Running the CLI**

    ```sh
    function_tester math_operations.multiply multiply_test_cases.json
    ```

    The CLI will output the detailed results for each test case.

