from tkinter import Tk, filedialog
import os
import re

root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

file_name, file_extension = os.path.splitext(file_path)

comment_patterns = {
    '.py': r'    '.sql': r'--.*?(?<!\\)\n|\/\*.*?(?<!\\)\*\/',                            '.go': r'\/\/.*?(?<!\\)\n|\/\*.*?(?<!\\)\*\/',                           '.cs': r'\/\/.*?(?<!\\)\n|\/\*.*?(?<!\\)\*\/',                            }

lines = []
with open(file_path, 'r') as file:
    content = file.read()
    pattern = comment_patterns.get(file_extension, '')
    cleaned_content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)
    lines = cleaned_content.splitlines(keepends=True)

new_file_path = file_name + '_comments_removed' + file_extension
with open(new_file_path, 'w') as new_file:
    new_file.writelines(lines)

print(f"Lines with comments removed. Saved as: {new_file_path}")
