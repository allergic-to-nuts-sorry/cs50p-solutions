import random as rd

def main():
    level = get_level()
    score = 0  # Start score at 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3

        while tries > 0:
            try:
                res = int(input(f"{x} + {y} = "))
                if res == x + y:
                    score += 1  # Add point for correct answer
                    break
                else:
                    print("EEE")
                    tries -= 1
            except ValueError:
                print("EEE")
                tries -= 1

        # If 3 incorrect attempts, print correct answer
        if tries == 0:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return rd.randint(0, 9)
    elif level == 2:
        return rd.randint(10, 99)
    elif level == 3:
        return rd.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2 or 3")


if __name__ == "__main__":
    main()
