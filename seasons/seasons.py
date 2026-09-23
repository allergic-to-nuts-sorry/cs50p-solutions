from datetime import date
import sys
import inflect

p = inflect.engine()


def mins(dob):
    today = date.today()
    age = today - dob
    minutes = age.days * 60 * 24
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


def parse_date(dob_str):
    try:
        # Convert YYYY-MM-DD string into a date object
        return date.fromisoformat(dob_str)
    except ValueError:
        return None


def main():
    user_input = input("Date of Birth: ").strip()
    dob = parse_date(user_input)

    if dob is None:
        # Exit with error message
        sys.exit("Invalid Date")

    print(mins(dob))


if __name__ == "__main__":
    main()
