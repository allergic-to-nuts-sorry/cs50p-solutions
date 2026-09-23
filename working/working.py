import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex captures hours, optional minutes (without requiring extra spaces), and AM/PM
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)\s+to\s+([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)$"

    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid Input")

    h1, m1, a1, h2, m2, a2 = match.groups()

    # Default missing minutes to "00"
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    h1, h2 = int(h1), int(h2)

    # 12-hour to 24-hour conversion logic
    if a1 == "PM" and h1 != 12:
        h1 += 12
    elif a1 == "AM" and h1 == 12:
        h1 = 0

    if a2 == "PM" and h2 != 12:
        h2 += 12
    elif a2 == "AM" and h2 == 12:
        h2 = 0

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
