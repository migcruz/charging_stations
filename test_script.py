import sys
from tests import test_list

def run_tests():

    total_tests = len(test_list)
    passed_tests = 0

    for test in test_list:
        ret = test()

        if ret == 0:
            passed_tests += 1

    print(f"\n🎯 Total Passed Tests: {passed_tests}/{total_tests}")

    return 0

def main():
    """Main function to run the script."""

    status = 0

    status = run_tests()

    sys.exit(status)

if __name__ == "__main__":
    main()