from tabulate import tabulate
import sys
import csv

def main():
    try:
        if not len(sys.argv) == 2:
            sys.exit("Invalid CLA")

        filename = sys.argv[1]

        if not filename.endswith(".csv"):
            sys.exit("Invalid Filename")

        table = []

        with open(filename,"r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                table.append(row)

            print(tabulate(table, headers = "keys", tablefmt = "grid"))



    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
