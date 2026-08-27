#!/usr/bin/python3
import sys

GREEN, RED, RESET = "\033[1;92m", "\033[1;91m", "\033[0m"

def main():
    h1, h2 = input("First md5sum: "), input("Second md5sum: ")
    print(f"{GREEN if h1 == h2 else RED}{'It\'s a match' if h1 == h2 else 'Does not match'}{RESET}")

if __name__ == "__main__":
    main()
