# picoCTF 2022 — credstuff 🔐

| | |
|---|---|
| **Category** | Cryptography |
| **Difficulty** | Medium |
| **Author** | Will Hong / LT `syreal` Jones |
| **CTF** | picoCTF 2022 |

## 📝 Challenge Description

We found a leak of a blackmarket website's login credentials. The goal is to find the password belonging to the user `cultiris` and decrypt it.

The challenge provides two files:

- `usernames.txt` — the leaked usernames
- `passwords.txt` — the corresponding encrypted passwords

> The first username corresponds to the first password, the second username to the second password, and so on.

## 🧠 Approach

1. Find the position (index) of `cultiris` in `usernames.txt`.
2. Use that same index to retrieve the corresponding password from `passwords.txt`.
3. Decrypt the password using **ROT13**.

ROT13 is a simple substitution cipher that rotates each letter 13 positions in the alphabet. Since applying ROT13 twice returns the original text, the same function can be used for both encryption and decryption.

## 💻 Solution

```python
import string

# Step 1 & 2: Find the matching password by index
with open("usernames.txt", "r") as file:
    content = file.readlines()

for i in range(len(content)):
    if content[i] == "cultiris\n":
        with open("passwords.txt", "r") as f:
            passd = f.readlines()
        pico = passd[i]


# Step 3: ROT13 decryption
def rot13(text: str) -> str:
    """Encrypts or decrypts text using the ROT13 cipher."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    shifted_lower = lower[13:] + lower[:13]
    shifted_upper = upper[13:] + upper[:13]
    rot13_table = str.maketrans(
        lower + upper,
        shifted_lower + shifted_upper
    )
    return text.translate(rot13_table)


if __name__ == "__main__":
    original_text = pico
    decrypted = rot13(original_text)
    print(decrypted)
```

## 🔍 Explanation

- The usernames and passwords are **positionally related** — if `cultiris` is found at index `i`, then `passwords.txt[i]` contains the corresponding encrypted password.
- The password is encrypted with ROT13, so calling `rot13()` on it decrypts it.

**Example:**

| Stage | Value |
|---|---|
| Encrypted | `...` |
| ROT13'd | `...` |
| Decrypted | `...` |

## 🎯 Key Takeaways

- Use matching indexes to associate usernames with passwords in parallel files.
- Recognize ROT13 as a common, easily reversible substitution cipher.
- ROT13 is its own inverse: `ROT13(ROT13(x)) = x`.
- Python's `str.translate()` and `str.maketrans()` provide a clean way to implement character substitutions.
