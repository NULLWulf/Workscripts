# import os
# import subprocess
# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext
#
# def execute_script():
#     script_path = script_var.get()
#     if not script_path:
#         messagebox.showwarning("Script Selection", "Please select a script to execute.")
#         return
#
#     try:
#         process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                    universal_newlines=True)
#         stdout, stderr = process.communicate()
#
#         output_text.configure(state='normal')
#         output_text.delete('1.0', tk.END)
#         output_text.insert(tk.END, stdout)
#         output_text.insert(tk.END, stderr)
#         output_text.configure(state='disabled')
#
#     except subprocess.CalledProcessError as e:
#         messagebox.showerror("Execution Error", str(e))
#     except Exception as e:
#         messagebox.showerror("Error", str(e))
#
#
# def select_script():
#     script_path = filedialog.askopenfilename(filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))
#     script_var.set(script_path)
#
#
# # Create the main window
# window = tk.Tk()
# window.title("Python Script Executor")
#
# # Create and configure the script selection button and label
# script_var = tk.StringVar()
# script_label = tk.Label(window, text="Select Script:")
# script_label.pack()
# script_button = tk.Button(window, text="Browse", command=select_script)
# script_button.pack()
# script_entry = tk.Entry(window, textvariable=script_var, state='readonly')
# script_entry.pack()
#
# # Create the execution button
# execute_button = tk.Button(window, text="Execute Script", command=execute_script)
# execute_button.pack()
#
# # Create and configure the output text area
# output_text = scrolledtext.ScrolledText(window, width=80, height=20, state='disabled')
# output_text.pack()
#
# # Start the GUI event loop
# window.mainloop()
