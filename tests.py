import subprocess
import os
import inspect

# Path to the tests directory
TESTS_DIR = "tests/"

def run_test(input_file, expected_output, test_name):

    merged_expected_output = "\n".join(expected_output)

    test_path = os.path.join(TESTS_DIR, input_file)

    # Run the main.py script with the input file
    result = subprocess.run(["python", "main.py", test_path], capture_output=True, text=True)
    script_output = result.stdout.strip()
    # Compare outputs
    if script_output == merged_expected_output:
        print(f"✅ {test_name}: Match")
        return 0
    else:
        print(f"❌ {test_name}: Mismatch")
        print("\nExpected Output:")
        print(merged_expected_output)
        print("\nScript Output:")
        print(script_output)
        return 1
    
# Define all the tests here

# Valid inputs
def valid_input_1():

    status = 0

    expected_output = [
        "0 100", 
        "1 0", 
        "2 75"
    ]

    status = run_test("input_1.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def valid_input_2():

    status = 0

    expected_output = [
        "0 66", 
        "1 100",
    ]

    status = run_test("input_2.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def valid_input_random_start_end_time():

    status = 0

    expected_output = [
        "0 96", 
        "1 0",
        "2 75",
    ]

    status = run_test("input_7.txt", expected_output,inspect.currentframe().f_code.co_name)
    return status

def valid_input_no_availability():

    status = 0

    expected_output = [
        "0 0", 
        "1 0",
        "2 0",
    ]

    status = run_test("input_8.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

# Invalid inputs
def invalid_input_randomstring():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_3.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_bad_start_end_time():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_4.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_bad_report_chargerid():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_5.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_bad_charger_availability():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_6.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_start_biggerthan_end():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_9.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_missing_chargerid():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_10.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_bad_charger_report_title():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_11.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_bad_stations_title():

    status = 0

    expected_output = [
        "ERROR",
    ]

    status = run_test("input_12.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

def invalid_input_empty_input():

    status = 0
    expected_output = [
        "ERROR",
    ]

    status = run_test("input_13.txt", expected_output, inspect.currentframe().f_code.co_name)
    return status

test_list = [
    valid_input_1,
    valid_input_2,
    valid_input_random_start_end_time,
    valid_input_no_availability,
    invalid_input_randomstring,
    invalid_input_bad_start_end_time,
    invalid_input_bad_report_chargerid,
    invalid_input_bad_charger_availability,
    invalid_input_start_biggerthan_end,
    invalid_input_missing_chargerid,
    invalid_input_bad_charger_report_title,
    invalid_input_bad_stations_title,
    invalid_input_empty_input,
]