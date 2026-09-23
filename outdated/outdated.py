def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                m,d,y = date.split("/")
                m = int(m)
                d = int(d)
                y = int(y)
            elif "," in date:
                m_d,y = date.split(",")
                m,d = m_d.split()

                if m.title() in months:
                    m = months.index(m.title()) + 1
                    d = int(d)
                    y = int(y)
                else:
                    continue
            else:
                continue
            if 1<=m<=12 and 1<=d<=31:
                print(f"{y:04}-{m:02}-{d:02}")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()

