# Certificate Generator✨

A simple Python script to automatically generate participation certificates from a CSV file.

## Features

- Generate certificates for multiple participants automatically
- Read participant names from a CSV file
- Automatically resize text to fit within a defined name area
- Save certificates as PNG or PDF
- Uses the Montserrat Bold font for clean and professional-looking certificates

---

## Project Structure

```text
certificate-generator/
│
├── assets/
│   ├── certificate_template.png
│   └── Montserrat-Bold.ttf
│
├── data/
│   └── names.csv
│
├── output/
│
├── generate_certificates.py
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd certificate-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the required directories

Create the following folder in the project root:

```text
output/
```

### 4. Add your files

#### Certificate Template

Place your certificate template inside:

```text
assets/certificate_template.png
```

#### Font

Place the Montserrat Bold font file inside:

```text
assets/Montserrat-Bold.ttf
```

#### Participant Names

Create:

```text
data/names.csv
```


---

## Run

```bash
python generate_certificates.py
```

Generated certificates will be saved inside:

```text
output/
```

---

## Output Formats

The script contains code for generating both PNG and PDF certificates.

You can enable either option by commenting or uncommenting the corresponding save statements in `generate_certificates.py`.

---

## Sample image

<div align =center>
  

<img width=50% alt="image" src="https://github.com/user-attachments/assets/f7b61933-02d9-4576-9073-64b21b1cb177" />

</div>  

## Notes

- If a participant has a long name, the script automatically reduces the font size until the name fits within the configured maximum width.
- Adjust the name position and maximum width values in `generate_certificates.py` to match your certificate template.
- The script has been tested using Montserrat Bold (`Montserrat-Bold.ttf`).

---
