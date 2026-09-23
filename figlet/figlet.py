import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Step 1: Validate Command-Line Arguments FIRST
    if len(sys.argv) == 1:
        # Zero arguments: select a random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3:
        # Two arguments: check flag (-f or --font) and valid font name
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")  # Exits with status 1
    else:
        sys.exit("Invalid usage")      # Exits with status 1

    # Step 2: Set the validated font
    figlet.setFont(font=font)

    # Step 3: Prompt for input AFTER argument validation
    text = input("Input: ")

    # Step 4: Output formatted result
    print("Output:")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
