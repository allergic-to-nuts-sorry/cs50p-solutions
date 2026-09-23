from emoji import emojize

def main():
    x = input("Input:")
    print(emojize(x, language = "alias"))

if __name__ == "__main__":
    main()

