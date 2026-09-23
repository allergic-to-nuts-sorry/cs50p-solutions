import sys
from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.name = name

    def generate(self):
        self.add_page()
        self.set_auto_page_break(auto=False, margin=0)

        # Title at the top of the PDF
        self.set_font("Helvetica", "B", 36)
        self.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

        # Shirt Image (Centered on A4 page: width 210mm, image width 170mm -> x = 20mm)
        self.image("shirtificate.png", x=20, y=70, w=170)

        # Name text overlaid in white on the shirt
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(130)
        self.cell(0, 10, f"{self.name} took CS50", align="C")

        # Output to PDF file
        self.output("shirtificate.pdf")


def main():
    name = input("Name: ").strip()
    if not name:
        sys.exit("Name cannot be empty")

    pdf = Shirtificate(name)
    pdf.generate()


if __name__ == "__main__":
    main()
