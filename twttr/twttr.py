def main():
    inp = input("Input: ")
    text = "".join(ch for ch in inp if ch not in "aeiouAEIOU")
    print(f"Output: {text}")

if __name__ == "__main__":
    main()
