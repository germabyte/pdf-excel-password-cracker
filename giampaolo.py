import PyPDF2
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def try_password(reader, password):
    try:
        if reader.decrypt(password):
            return True
    except:
        pass
    return False

def brute_force_pdf_password(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for num in tqdm(range(10000), desc="Trying passwords"):
            password = str(num).zfill(4)
            if try_password(reader, password):
                print(f"\nSuccess! The password is: {password}")
                return
        print("\nPassword not found.")

# Get the file path from the user
pdf_path = select_pdf_file()

# Run the brute force function if a file was selected
if pdf_path:
    brute_force_pdf_password(pdf_path)
else:
    print("No file selected.")
