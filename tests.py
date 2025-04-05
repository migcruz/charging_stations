import subprocess
import os
import glob

# Path to the tests directory
TESTS_DIR = "tests/"

# Find all input files that match input_*.txt but **exclude** output files
input_files = [f for f in glob.glob(os.path.join(TESTS_DIR, "input_*.txt")) 
               if "_expected_stdout" not in f]

# Separate files into two lists
low_inputs = []  # `input_0` to `input_9`
high_inputs = []  # `input_10` and above

for file in input_files:
    # Extract the number portion from the filename
    filename = os.path.basename(file)
    try:
        num = int(filename.split("_")[1].split(".")[0])  # Extract number from "input_X.txt"
        if num < 10:
            low_inputs.append(file)
        else:
            high_inputs.append(file)
    except ValueError:
        print(f"⚠️ Warning: Could not parse test number from {filename}")

# Sort the lists numerically
low_inputs.sort(key=lambda x: int(os.path.basename(x).split("_")[1].split(".")[0]))
high_inputs.sort(key=lambda x: int(os.path.basename(x).split("_")[1].split(".")[0]))

# Merge the sorted lists (low first, high last)
sorted_input_files = low_inputs + high_inputs

# Initialize counters
total_tests = len(sorted_input_files)
passed_tests = 0

# Iterate over sorted input files
for input_file in sorted_input_files:
    # Construct expected output file name
    expected_output_file = input_file.replace(".txt", "_expected_stdout.txt")

    # Check if the corresponding expected output file exists
    if not os.path.exists(expected_output_file):
        print(f"⚠️ Warning: Expected output file not found for {input_file}")
        continue

    # Run the main.py script with the input file
    result = subprocess.run(["python", "main.py", input_file], capture_output=True, text=True)
    script_output = result.stdout.strip()

    # Read expected output from file
    with open(expected_output_file, "r") as file:
        expected_output = file.read().strip()

    # Compare outputs
    if script_output == expected_output:
        print(f"✅ {input_file}: Match")
        passed_tests += 1  # Increment the counter for passed tests
    else:
        print(f"❌ {input_file}: Mismatch")
        print("\nExpected Output:")
        print(expected_output)
        print("\nScript Output:")
        print(script_output)

# Print the total passed test cases at the end
print(f"\n🎯 Total Passed Tests: {passed_tests}/{total_tests}")
