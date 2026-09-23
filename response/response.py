import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    # Check if the string 's' is a valid email address
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
