import string

with open("usernames.txt", "r") as file:
    content = file.readlines()

for i in range(len(content)):
    if content[i]=="cultiris\n":
        with open("passwords.txt","r") as f:
            passd = f.readlines()
        pico = passd[i]

def rot13(text: str) -> str:
    """Encrypts or decrypts text using the ROT13 cipher."""
    # Create the standard alphabet mapping
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    # Create the shifted (rotated by 13 places) mapping
    shifted_lower = lower[13:] + lower[:13]
    shifted_upper = upper[13:] + upper[:13]

    # Build a translation table
    rot13_table = str.maketrans(lower + upper, shifted_lower + shifted_upper)

    # Apply the translation map
    return text.translate(rot13_table)

# --- Example Usage ---
if __name__ == "__main__":
    original_text = pico

    # Encrypt the text
    encrypted = rot13(original_text)
    print(encrypted)
