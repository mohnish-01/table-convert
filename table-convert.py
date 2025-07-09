import sys
import re

def convert(infile, outfile):
    try:
        with open(infile, 'r') as inputobj:
            print(inputobj.readline())
    except FileNotFoundError as e:
        print(f"Exception Occured: {e}")
        sys.exit(2)
    except IOError as e:
        print(f"Exception Occured: {e}")
        sys.exit(2)


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print(f"Usage: {sys.argv[0]} inputfile outputfile")
        sys.exit(2)
    else:
        convert(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
