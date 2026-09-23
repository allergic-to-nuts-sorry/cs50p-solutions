import sys

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Invalid CLA")
        filename = sys.argv[1].strip()
        if not filename.endswith(".py"):
            sys.exit("Not a valid filename")

        count = 0

        with open(filename,"r") as f:
            for line in f:
                stripped_line = line.strip()

                if not stripped_line or stripped_line.startswith("#"):
                    continue
                count += 1

    except FileNotFoundError:
        sys.exit("File Not Found")

    print(count)

if __name__ == "__main__":
    main()

