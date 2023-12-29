import PyPDF2
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog, simpledialog

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def select_text_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(filetypes=[("Text files", "*.txt")])
    return file_paths

def ask_for_digits():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    digits = simpledialog.askinteger("Input", "Enter the number of digits for numeric brute force:",
                                     minvalue=1, maxvalue=10)
    return digits

def try_password(reader, password):
    try:
        if reader.decrypt(password):
            return True
    except:
        pass
    return False

def read_passwords_from_files(file_paths):
    passwords = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            passwords += file.read().splitlines()
    return passwords

def brute_force_pdf_password(pdf_path, text_files, digits):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Try numeric passwords first
        max_num = 10**digits - 1
        for num in tqdm(range(max_num + 1), desc=f"Trying numeric passwords up to {digits} digits"):
            password = str(num).zfill(digits)
            if try_password(reader, password):
                print(f"\nSuccess! The password is: {password}")
                return

        # If dictionary files are provided, try passwords from them
        if text_files:
            dictionary_passwords = read_passwords_from_files(text_files)
            for password in tqdm(dictionary_passwords, desc="Trying dictionary passwords"):
                if try_password(reader, password):
                    print(f"\nSuccess! The password is: {password}")
                    return

        print("\nPassword not found.")

# Get the file path and number of digits from the user
pdf_path = select_pdf_file()
digits = ask_for_digits()
if digits is None:
    print("No digit number selected.")
else:
    text_files = select_text_files()

    # Run the brute force function if a file was selected
    if pdf_path:
        brute_force_pdf_password(pdf_path, text_files, digits)
    else:
        print("No PDF file selected.")
