import sys
from helpers import parse_file

def main():
    """Main function to run the script."""

    status = 0
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    status = parse_file(file_path)

    sys.exit(status)

if __name__ == "__main__":
    main()
