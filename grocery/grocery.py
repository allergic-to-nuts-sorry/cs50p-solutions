def main():
    # Keep variables inside function scope rather than global scope
    d = {}

    while True:
        try:
            item = input().strip().upper()

            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

        except EOFError:
            # Print a newline for clean terminal exit
            print()

            # Sort keys and print frequency count
            for item in sorted(d.keys()):
                print(f"{d[item]} {item}")
            break

if __name__ == "__main__":
    main()
