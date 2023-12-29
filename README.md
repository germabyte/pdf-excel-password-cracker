# PDF Password Cracker

## Description

This Python script is designed to perform a brute-force attack to unlock password-protected PDF files. It uses a combination of numeric and dictionary-based approaches to try and crack the password. The script is built using the PyPDF2 library for handling PDF files and tkinter for a basic graphical user interface to select files and input parameters.

## Features

- **Numeric Brute Force**: Attempts to unlock the PDF by trying numeric passwords up to a specified number of digits.
- **Dictionary Attack**: Uses a list of passwords from provided text files to attempt to unlock the PDF.
- **Graphical File Selection**: Easily select your target PDF file and text files containing potential passwords through a file dialog interface.
- **Progress Display**: Shows the progress of the brute-forcing process using tqdm.

## Requirements

- Python 3.x
- PyPDF2
- tqdm
- tkinter (usually included in standard Python installations)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:
   ```
   pip install PyPDF2 tqdm
   ```

## Usage

1. Run the script in a Python environment.
2. A file dialog will appear. Select the PDF file you wish to unlock.
3. Input the maximum number of digits for the numeric brute force attempt.
4. Select text files containing possible passwords for the dictionary attack (optional).
5. The script will first attempt numeric brute forcing, followed by the dictionary attack if text files were provided.
6. If the password is found, it will be displayed in the console.

## Warning

This tool is intended for educational purposes and for recovering passwords of PDFs you are legally entitled to access. Using this tool for cracking passwords of files you do not own or have permission to access may be illegal in your jurisdiction.
