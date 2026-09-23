import requests
import sys
import json

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        res = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ce8043358909d873c7e3fa9a2cc03ccc49be1e94f9f6ecdb69c1223c2689f86b", data={})
        s = res.json()
        amount = float(s["data"]["priceUsd"])*bitcoins
        print(f"${amount:,.4f}")

    except requests.RequestException:
        print("Invalid request")

if __name__ == "__main__":
    main()
