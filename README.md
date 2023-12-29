# PDF Password Cracker

## Description
This Python script provides a simple yet effective way to perform a brute force attack on password-protected PDF files. It attempts to unlock a PDF by trying passwords ranging from 0000 to 9999.

## Features
- **File Selection GUI**: Easily select your target PDF file through a graphical file picker.
- **Brute Force Attack**: Automatically tries all possible four-digit combinations as passwords.
- **Progress Display**: Shows the progress of the password cracking process.
- **Efficient and User-friendly**: The script is straightforward to use, with minimal setup required.

## Requirements
- Python 3.x
- PyPDF2
- tqdm
- tkinter

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required packages using pip:
   ```bash
   pip install PyPDF2 tqdm
   ```

## Usage
1. Run the script:
   ```bash
   python pdf_password_cracker.py
   ```
2. A file dialog will open. Select the PDF file you wish to crack.
3. The script will start attempting to crack the password, showing the progress in the console.
4. Once the password is found, it will be displayed in the console.

## Important Note
This tool is intended for educational purposes or for recovering passwords of your own files. Using this tool on files you do not have permission to access is illegal and unethical.
