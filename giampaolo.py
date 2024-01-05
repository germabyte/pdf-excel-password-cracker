import msoffcrypto
import PyPDF2
import openpyxl
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog, simpledialog
import os

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF and Excel files", "*.pdf;*.xlsx")])
    return file_path

def select_text_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(filetypes=[("Text files", "*.txt")])
    return file_paths

def ask_for_digits():
    root = tk.Tk()
    root.withdraw()
    digits = simpledialog.askinteger("Input", "Enter the number of digits for numeric brute force:",
                                     minvalue=1, maxvalue=10)
    return digits

def try_pdf_password(reader, password):
    try:
        if reader.decrypt(password):
            return True
    except:
        pass
    return False

def try_xlsx_password(file_path, password):
    try:
        file = msoffcrypto.OfficeFile(open(file_path, "rb"))
        file.load_key(password=password)
        decrypted_file_path = "temporary_decrypted.xlsx"
        file.decrypt(open(decrypted_file_path, "wb"))
        return decrypted_file_path
    except:
        pass
    return None

def read_passwords_from_files(file_paths):
    passwords = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            passwords += file.read().splitlines()
    return passwords

def brute_force_password(file_path, text_files, digits):
    file_extension = file_path.split('.')[-1].lower()
    password_found = False

    if file_extension == 'pdf':
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            try_password = lambda password: try_pdf_password(reader, password)
    elif file_extension == 'xlsx':
        try_password = lambda password: try_xlsx_password(file_path, password)
    else:
        print("Unsupported file type.")
        return

    max_num = 10**digits - 1
    for num in tqdm(range(max_num + 1), desc=f"Trying numeric passwords up to {digits} digits"):
        password = str(num).zfill(digits)
        result = try_password(password)
        if result:
            if file_extension == 'pdf':
                print(f"\nSuccess! The password is: {password}")
                password_found = True
                break
            else:
                decrypted_file_path = result
                print(f"\nSuccess! The password is: {password}")
                new_file_name = f"decrypted_{os.path.basename(file_path)}"
                os.rename(decrypted_file_path, new_file_name)
                print(f"File decrypted as {new_file_name}")
                return

    if text_files and not password_found:
        dictionary_passwords = read_passwords_from_files(text_files)
        for password in tqdm(dictionary_passwords, desc="Trying dictionary passwords"):
            result = try_password(password)
            if result:
                if file_extension == 'pdf':
                    print(f"\nSuccess! The password is: {password}")
                    password_found = True
                    break
                else:
                    decrypted_file_path = result
                    print(f"\nSuccess! The password is: {password}")
                    new_file_name = f"decrypted_{os.path.basename(file_path)}"
                    os.rename(decrypted_file_path, new_file_name)
                    print(f"File decrypted as {new_file_name}")
                    return

    if file_extension == 'pdf' and password_found:
        print(f"\nFile password for PDF found: {password}")
    elif not password_found:
        print("\nPassword not found.")

file_path = select_file()
digits = ask_for_digits()
if digits is None:
    print("No digit number selected.")
else:
    text_files = select_text_files()
    if file_path:
        brute_force_password(file_path, text_files, digits)
    else:
        print("No file selected.")
