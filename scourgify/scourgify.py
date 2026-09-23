import sys
import csv

def main():
    try:
        if not len(sys.argv) == 3:
            sys.exit("Invalid CLA")
        filename = sys.argv[1]
        writefile = sys.argv[2]
        if not filename.endswith(".csv") or not writefile.endswith(".csv"):
            sys.exit("Invalid filename")

        with open(filename,"r") as f, open(writefile,"w") as w:
            reader = csv.DictReader(f)
            writer = csv.DictWriter(w, fieldnames = ["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                fn, ln = row["name"].split(",")
                writer.writerow({"first":ln.strip(),"last":fn.strip(),"house":row["house"].strip()})

    except FileNotFoundError:
        sys.exit("File Not Found")

if __name__ == "__main__":
    main()
