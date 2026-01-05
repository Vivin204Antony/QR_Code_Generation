# 🧩 QR Code Generation

A simple, lightweight Python program to generate custom QR codes using the `qrcode` library. This project is designed with clean code principles to help you quickly encode URLs, text, or any other data into a scannable QR image.



## 🚀 Features
- **Easy Generation:** Create a QR code in just a few lines of code.
- **Customizable:** Adjust the size, border, and colors of your QR codes.
- **Versatile:** Supports encoding of URLs, plain text, and more.

## 🛠️ Installation

**Clone the repository:**
   ```bash
   git clone [https://github.com/Vivin204Antony/QR_Code_Generation.git](https://github.com/Vivin204Antony/QR_Code_Generation.git)
   cd QR_Code_Generation

Install dependencies: This project requires the qrcode library and Pillow for image processing.
   pip install qrcode[pil]

💻 Usage
Run the program to generate your QR code:

Bash

python main.py
Basic Code Example
Python

import qrcode

# Data to be encoded
data = "[https://github.com/Vivin204Antony](https://github.com/Vivin204Antony)"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data and generate
qr.add_data(data)
qr.make(fit=True)

# Create and save image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated successfully!")
📂 Project Structure
main.py: The core script for generating QR codes.

README.md: Project documentation.

🤝 Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas to improve this generator.

