#!/usr/bin/python3

# ANSI escape codes for bright colors
BRIGHT_GREEN = "\033[1;92m"  # Bright Green
BRIGHT_RED = "\033[1;91m"    # Bright Red
RESET = "\033[0m"            # Reset to default color

def main():
    # Prompt for the first hash
    hash1 = input("Specify the first value: ")

    # Prompt for the second hash
    hash2 = input("Specify the second value: ")

    # Compare the hashes
    if hash1 == hash2:
        print(f"{BRIGHT_GREEN}It's a match {RESET}")
    else:
        print(f"{BRIGHT_RED}The sums do not match. Please check your inputs.{RESET}")

if __name__ == "__main__":
    main()
