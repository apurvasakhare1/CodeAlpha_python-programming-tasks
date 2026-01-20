import re
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the input file
with open(os.path.join(script_dir, "input.txt"), "r") as file:
    text = file.read()

# Find all email addresses using regex
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

# Write emails to output file
with open(os.path.join(script_dir, "emails.txt"), "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
