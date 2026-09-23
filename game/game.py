import random as rd

def main():
    while True:
        try:
            level = int(input("Enter level:"))
            if level>0:
                break
        except ValueError:
            continue

    x = rd.randint(1,level)
    while True:
        try:
            guess = int(input("Guess:"))
            if guess<=0:
                continue
            if guess < x:
                print("Too small!")
                continue
            if guess > x:
                print("Too Large!")
                continue
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()
