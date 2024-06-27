import sys
import os  # Optional

def main():
    if len(sys.argv) != 2: #Checking to see if there is exactly 2 command line arguments
        #if there is more then 2 it is incorrect use of the script.
        #it should be script name('sys.argv[0] and sys.argv[1])
        print("Usage: python line_counter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1] #Extract the first command line argument to be able to count the number of lines

    if not os.path.isfile(filename):  # Optional file existence check
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
    except Exception as e:
        print(f"Error: Could not read the file '{filename}'. {e}")
        sys.exit(1)

    print(f"Total lines: {line_count}")

if __name__ == "__main__":
    main()


