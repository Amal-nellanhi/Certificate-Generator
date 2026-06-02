from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# ==========================
# CONFIGURATION
# ==========================

TEMPLATE_PATH = "assets/certificate_template.png"
FONT_PATH = "assets/Montserrat-Bold.ttf"

CSV_PATH = "data/names.csv"
OUTPUT_DIR = "output"

# Name placement settings
NAME_CENTER_X = 960
NAME_CENTER_Y = 640

MAX_NAME_WIDTH = 1200

START_FONT_SIZE = 72
MIN_FONT_SIZE = 20

TEXT_COLOR = (0, 0, 0)

# ==========================
# SETUP
# ==========================

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(CSV_PATH)

# ==========================
# GENERATE CERTIFICATES
# ==========================

for _, row in df.iterrows():

    name = str(row["Name"]).strip()

    image = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(image)

    font_size = START_FONT_SIZE

    while font_size >= MIN_FONT_SIZE:

        font = ImageFont.truetype(FONT_PATH, font_size)

        bbox = draw.textbbox((0, 0), name, font=font)

        text_width = bbox[2] - bbox[0]

        if text_width <= MAX_NAME_WIDTH:
            break

        font_size -= 1

    # Final font
    font = ImageFont.truetype(FONT_PATH, font_size)

    bbox = draw.textbbox((0, 0), name, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = NAME_CENTER_X - text_width / 2
    y = NAME_CENTER_Y - text_height / 2

    draw.text(
        (x, y),
        name,
        font=font,
        fill=TEXT_COLOR
    )

    safe_name = "".join(
        c for c in name if c.isalnum() or c in (" ", "_", "-")
    ).strip()

    filename = safe_name.replace(" ", "_") + ".png"

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    image.save(output_path)
    # uncomment the following lines to also save as PDF
    # comment lines above that save as PNG if you only want PDF output
#     pdf_filename = safe_name.replace(" ", "_") + ".pdf"

#     pdf_path = os.path.join(
#     OUTPUT_DIR,
#     pdf_filename
# )

#     image.convert("RGB").save(pdf_path, "PDF")

    print(
        f"Generated: {filename}"
        f" | font size: {font_size}"
    )

print("\nDone!")