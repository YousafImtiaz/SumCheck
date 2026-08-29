#!/usr/bin/python3
import sys, re, signal

GREEN, RED, RESET = "\033[1;92m", "\033[1;91m", "\033[0m"

def signal_handler(sig, frame):
    print(f"\n\n{RED}Exiting SumCheck...{RESET}")
    sys.exit(0)

def banner():
    print(f"""{GREEN}
SumCheck         
{RESET}""")

def is_valid_md5(s):
    s = s.strip()
    if len(s) != 32 or not re.match(r'^[a-fA-F0-9]{32}$', s):
        return False, "MD5 must be 32 hex characters"
    return True, s

def get_hash(prompt):
    while True:
        try:
            valid, result = is_valid_md5(input(prompt).strip())
            if valid:
                return result
            print(f"{RED}Error: {result}{RESET}")
        except EOFError:
            print(f"\n{RED}Input cancelled.{RESET}")
            sys.exit(0)
        except KeyboardInterrupt:
            print(f"\n{RED}Exiting SumCheck...{RESET}")
            sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    banner()
    
    try:
        h1 = get_hash("First md5sum: ")
        h2 = get_hash("Second md5sum: ")
        print(f"{GREEN}It's a match{RESET}" if h1 == h2 else f"{RED}Values do not match{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting SumCheck...{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
