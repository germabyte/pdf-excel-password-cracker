# PDF and Excel Password Cracker

## Description

This Python script is capable of cracking password-protected PDF and Excel files using brute-force and dictionary attack methods. The script utilizes various libraries including `msoffcrypto`, `PyPDF2`, `openpyxl`, and `tkinter` for a graphical user interface. It offers flexibility in handling both numeric and dictionary-based attacks, making it versatile for different cracking scenarios.

## Features

- **Support for Multiple File Types**: Works with both PDF and Excel files.
- **Numeric Brute Force**: Attempts passwords using numeric combinations up to a specified number of digits.
- **Dictionary Attack**: Utilizes provided text files containing potential passwords.
- **File Dialog Interface**: Enables easy file selection for both the target file and the dictionary files.
- **Progress Tracking**: Progress of the brute-forcing attempt is displayed using tqdm.
- **Flexible Password Testing**: Handles different methods for testing passwords on PDF and Excel files.

## Requirements

- Python 3.x
- Libraries: `msoffcrypto`, `PyPDF2`, `openpyxl`, `tqdm`, `tkinter`
- Tkinter is generally included in standard Python installations.

## Installation

1. Clone the repository or download the script.
2. Install the necessary libraries:
   ```
   pip install msoffcrypto PyPDF2 openpyxl tqdm
   ```

## Usage

1. Execute the script in a Python environment.
2. Select the PDF or Excel file you want to crack through the file dialog.
3. Enter the maximum number of digits for the numeric brute force attack.
4. Optionally, choose text files that contain possible passwords for the dictionary attack.
5. The script will first try numeric brute-forcing and then proceed to the dictionary attack if dictionary files are provided.
6. The script will notify you of the successful password discovery and save the decrypted file.

## Caution

This tool is intended strictly for educational purposes and legitimate use cases like recovering lost passwords for files you legally own. Utilizing this tool for unauthorized access to files can be illegal in many jurisdictions and is strongly discouraged.
