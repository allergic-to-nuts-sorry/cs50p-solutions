def main():
    time = convert(input("What time is it?: ").strip())

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    is_am = "a.m." in time
    is_pm = "p.m." in time

    time_clean = time.replace("a.m.","").replace("p.m.","").strip()

    h, m = time_clean.split(":")
    h = float(h)
    m = float(m)

    if is_pm and h!=12:
        h+=12
    elif is_am and h==12:
        h=0

    return (h) + (m)/60


if __name__ == "__main__":
    main()

