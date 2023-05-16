from tkinter import Tk, filedialog
import os
import re

# Open file selector dialog
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Get file extension
file_name, file_extension = os.path.splitext(file_path)

# Define comment patterns for different file types
comment_patterns = {
    '.py': r'#.*?(?<!\\)\n|\'\'\'.*?(?<!\\)\'\'\'|\"\"\".*?(?<!\\)\"\"\"',  # Python (single-line and multi-line comments)
    '.sql': r'--.*?(?<!\\)\n|\/\*.*?(?<!\\)\*\/',                        # SQL (single-line and multi-line comments)
    '.go': r'\/\/.*?(?<!\\)\n|\/\*.*?(?<!\\)\*\/',                       # Go (single-line and multi-line comments)
    '.cs': r'\/\/.*?(?<!\\)\n|\/\*.*?(?<!\\)\*\/',                        # C# (single-line and multi-line comments)
    # Add more file extensions and comment patterns as needed
}

# Process file and remove lines with comments
lines = []
with open(file_path, 'r') as file:
    content = file.read()
    pattern = comment_patterns.get(file_extension, '')
    cleaned_content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)
    lines = cleaned_content.splitlines(keepends=True)

# Save modified content to a new file
new_file_path = file_name + '_comments_removed' + file_extension
with open(new_file_path, 'w') as new_file:
    new_file.writelines(lines)

print(f"Lines with comments removed. Saved as: {new_file_path}")
