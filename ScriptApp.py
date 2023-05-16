import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Create the main window
window = tk.Tk()
window.title("Python Script Executor")

# Define the script directory
script_dir = os.path.join(os.getcwd(), "ScriptLib")

# Create and configure the script selection listbox
script_listbox_label = tk.Label(window, text="Available Scripts:")
script_listbox_label.pack()
script_listbox = tk.Listbox(window)
script_listbox.pack(fill=tk.BOTH, expand=True)

# Populate the script selection listbox with Python files in the script directory
for file_name in os.listdir(script_dir):
    if file_name.endswith(".py"):
        script_listbox.insert(tk.END, file_name)

# Create and configure the output text area
output_text = scrolledtext.ScrolledText(window, width=80, height=20)
output_text.pack()


def execute_script():
    # Get the selected script
    selected_script = script_listbox.get(tk.ACTIVE)
    if not selected_script:
        messagebox.showwarning("Script Selection", "Please select a script to execute.")
        return

    try:
        script_path = os.path.join(script_dir, selected_script)
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True)
        stdout, stderr = process.communicate()

        # Clear the output text area
        output_text.delete('1.0', tk.END)

        # Insert the output into the text area
        output_text.insert(tk.END, stdout)
        output_text.insert(tk.END, stderr)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Execution Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def quit_function():
    window.destroy()
    print("Exiting...")
    exit()


# Create and configure the execution button
execute_button = tk.Button(window, text="Execute Script", command=execute_script)
exit_button = tk.Button(window, text="Exit", command=quit_function)
exit_button.pack()
execute_button.pack()

# Start the GUI event loop
window.mainloop()
