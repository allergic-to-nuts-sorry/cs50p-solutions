def main():

    while True:
        try:
            x,y = input("Fraction: ").strip().split("/")
            x = int(x)
            y = int(y)

            if x>y or x<0 or y<0:
                continue

            percentage = round((x / y) * 100)
            break

        except (ValueError, ZeroDivisionError):
            continue
    if percentage >= 99:
                print(f"F")
    elif percentage <= 1:
                print(f"E")
    else:
                print(f"{percentage}%")

if __name__ == "__main__":
    main()
