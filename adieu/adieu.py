import inflect
p = inflect.engine()

def main():
    names=[]
    while True:
        try:
            name = input("Name:").strip()
            if name:
                names.append(name)
        except EOFError:
            print()
            break
    if not names:
        sys.exit()

    print("Adieu, adieu, to", p.join(names))

if __name__ == "__main__":
    main()
