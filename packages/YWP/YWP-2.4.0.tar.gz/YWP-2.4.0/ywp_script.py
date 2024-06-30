import os
import sys
import tkinter as tk
from tkinter import messagebox
from YWP import install_system_packages

def quit_application():
    sys.exit(0)

def install_packages():
    try:
        result = install_system_packages()
        messagebox.showinfo("Success", "Packages installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to install packages: {str(e)}")

def main():
    root = tk.Tk()
    root.title("YWP Commands")
    root.configure(background="#333333")  # لون خلفية داكن
    root.geometry("500x400")  # تعيين حجم النافذة الافتراضي

    label = tk.Label(root, text="Select an option:", bg="#333333", fg="#ffffff", font=("Helvetica", 16))
    label.pack(pady=20)

    install_button = tk.Button(root, text="Install packages", command=install_packages, font=("Helvetica", 14), bg="#555555", fg="#ffffff")
    install_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=quit_application, font=("Helvetica", 14), bg="#ff5733", fg="white")
    quit_button.pack(pady=10, padx=20, ipadx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
