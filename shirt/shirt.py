import os
import sys
from PIL import Image, ImageOps


def main():
    # 1. Validate argument counts
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # 2. Validate file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # 3. Process images
    try:
        # Open shirt overlay and input photo
        shirt = Image.open("shirt.png")
        user_image = Image.open(input_path)

        # Fit user image to the exact dimensions of shirt.png
        fitted_image = ImageOps.fit(user_image, shirt.size)

        # Overlay shirt onto fitted image using shirt as the transparency mask
        fitted_image.paste(shirt, (0, 0), shirt)

        # Save output
        fitted_image.save(output_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
