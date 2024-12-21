# PDF Master

PDF Master is a Python program that converts PDF files to audio.

## Features

- Convert PDF files to audio
- Simple and easy to use

## Requirements

- Python 3.x
- `PyPDF2` library
- `gTTS` library

## How it works

- `PyMuPDF (fitz)` is used to open and extract the text content from the PDF
- `gTTS` library is used to convert the generated text to audio, for this you'll need access to the internet.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Unrealrojo234/pdf_master
   ```
2. Navigate to the project directory:
   ```bash
   cd PDF_MASTER
   ```
3. Install the required libraries:
   ```bash
   pip install PyPDF2 gTTS
   ```

## Usage

1. Place your PDF file in the project directory.
2. Run the program:
   ```bash
   python main.py
   ```
3. The audio file will be generated in the same directory.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact otienoryan812@gmial.com.
