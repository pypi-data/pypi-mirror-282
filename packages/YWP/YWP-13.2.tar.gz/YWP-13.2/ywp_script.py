import os
import sys
import tkinter as tk
from tkinter import messagebox
import YWP

# Function to get commands from help function
def get_commands():
    return [
        "install_packages", "install_libraries", "upgrade_libraries", "upgrade_library",
        "Audios.play_sound", "Audios.play_audio", "Audios.record_audio", "Audios.transcribe_audio_offline",
        "Audios.transcribe_audio", "Audios.text_to_speech", "Audios.text_to_speech_offline", "Audios.play_audio_online",
        "Files.create_file", "Files.open_file", "Files.delete_all_files", "Websites.open_website",
        "Crypto.token_information", "VideosCreator.Basic.basic_video_creator", "endecrypt.aes.encrypt",
        "endecrypt.aes.decrypt", "endecrypt.BlowFish.encrypt", "endecrypt.BlowFish.decrypt", "endecrypt.Base64.encrypt",
        "endecrypt.Base64.decrypt", "endecrypt.Hex.encrypt", "endecrypt.Hex.decrypt", "Libraries.Basic.init_creator",
        "Libraries.Basic.basic_setup_file_creator", "Libraries.Basic.upload_file_creator", "Files.delete_file"
    ]

def quit_application():
    sys.exit(0)

def get_terminal_command():
    if sys.platform.startswith('win'):
        return "cmd.exe"
    elif sys.platform.startswith('linux'):
        terminals = ["gnome-terminal", "xterm", "konsole", "xfce4-terminal", "lxterminal", "terminator", "tilix", "mate-terminal"]
        available_terminals = [term for term in terminals if os.system(f"which {term} > /dev/null 2>&1") == 0]
        if available_terminals:
            return available_terminals[0]
        else:
            return None
    elif sys.platform.startswith('darwin'):
        return "Terminal"
    else:
        return None

def run_command(command):
    terminal = get_terminal_command()
    if terminal:
        if terminal == "cmd.exe":
            os.system(f'start cmd /c "{command}"')
        elif terminal in ["gnome-terminal", "terminator", "tilix"]:
            os.system(f"{terminal} -- bash -c '{command}; read -p \"Press Enter to close...\"'")
        elif terminal == "konsole":
            os.system(f"{terminal} -e bash -c \"{command}; read -p 'Press Enter to close...'\"")
        elif terminal == "Terminal":
            os.system(f"open -a {terminal} '{command}'")
        else:
            os.system(f"{terminal} -hold -e bash -c \"{command}; read -p 'Press Enter to close...'\"")
    else:
        return "No supported terminal found."

def call_command(command):
    try:
        parts = command.split('.')
        if len(parts) == 1:
            run_command(f"python3 -c 'import YWP; YWP.inuser.{parts[0]}_inuser()'")
        elif len(parts) == 2:
            run_command(f"python3 -c 'import YWP; YWP.inuser.{parts[0]}.{parts[1]}_inuser()'")
        elif len(parts) == 3:
            run_command(f"python3 -c 'import YWP; YWP.inuser.{parts[0]}.{parts[1]}.{parts[2]}_inuser()'")
        else:
            messagebox.showerror("Error", f"Invalid command: {command}")
    except AttributeError:
        messagebox.showerror("Error", f"Command not found: {command}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to execute {command}: {str(e)}")

def main():
    root = tk.Tk()
    root.title("YWP Commands")
    root.configure(background="#333333")  # لون خلفية داكن
    root.geometry("650x650")  # تعيين حجم النافذة الافتراضي

    label = tk.Label(root, text="Select an option:", bg="#333333", fg="#ffffff", font=("Helvetica", 16))
    label.pack(pady=20)
    
    button_frame = tk.Frame(root, bg="#333333")
    button_frame.pack(expand=True, fill=tk.BOTH)

    commands = get_commands()
    buttons_per_page = 10
    current_page = 0

    def update_buttons():
        for widget in button_frame.winfo_children():
            widget.destroy()

        start = current_page * buttons_per_page
        end = start + buttons_per_page
        for command in commands[start:end]:
            btn = tk.Button(button_frame, text=command, font=("Helvetica", 14), bg="#555555", fg="#ffffff", command=lambda cmd=command: call_command(cmd))
            btn.pack(pady=5, padx=10, fill=tk.X)

        if current_page > 0:
            prev_button = tk.Button(button_frame, text="Previous", command=previous_page, font=("Helvetica", 14), bg="#ff5733", fg="#ffffff")
            prev_button.pack(side=tk.LEFT, pady=10, padx=10, ipadx=10)

        if end < len(commands):
            next_button = tk.Button(button_frame, text="Next", command=next_page, font=("Helvetica", 14), bg="#ff5733", fg="#ffffff")
            next_button.pack(side=tk.RIGHT, pady=10, padx=10, ipadx=10)

    def next_page():
        nonlocal current_page
        current_page += 1
        update_buttons()

    def previous_page():
        nonlocal current_page
        current_page -= 1
        update_buttons()

    quit_button = tk.Button(root, text="Quit", command=quit_application, font=("Helvetica", 14), bg="#ff5733", fg="white")
    quit_button.pack(pady=10, padx=20, ipadx=10)

    update_buttons()
    root.mainloop()

if __name__ == "__main__":
    main()
