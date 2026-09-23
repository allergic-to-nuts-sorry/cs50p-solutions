import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Match exactly 4 octets separated by dots, each in range 0-255
    pattern = r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$"
    if re.search(pattern, ip.strip()):
        return True
    return False

if __name__ == "__main__":
    main()
