Autorev 1 — picoCTF 2026 Write-up
Autorev 1 — picoCTF 2026

Category: Reverse Engineering
Difficulty: Medium
Author: SkrubLawd
Challenge: Autorev 1

Challenge Description

You think you can reverse engineer? Let's test out your speed.

The challenge provides a remote service:

nc mysterious-sea.picoctf.net 54107


The goal is to communicate with the service and provide a sequence of correct secrets quickly enough to complete the challenge.

Solution

The service initially sends a secret, then repeatedly asks:

What's the secret?:


The important observation is that the secret is provided directly by the server. We don't need to reverse engineer or calculate anything—the script simply needs to:

Connect to the remote service.
Read the first secret.
Send it back.
Read the next secret.
Repeat this process 19 more times.
Read the final response containing the flag.
Exploit Script
from pwn import *

host = "mysterious-sea.picoctf.net"
port = 54107

p = remote(host, port)

p.recvuntil(b">:)\n")

secret = p.recvline().strip()

p.recvuntil(b"What's the secret?:")
p.sendline(secret)

for i in range(19):
    p.recvuntil(b"\n")
    secret = p.recvline().strip()

    p.recvuntil(b"What's the secret?:")
    p.sendline(secret)

p.recvuntil(b"Woah, how'd you do that??\n")
print(p.recvline())

Explanation
Connecting to the service

Pwntools' remote() function establishes a connection to the challenge server:

p = remote(host, port)

Receiving the first secret

After waiting for the initial prompt, the script reads the secret:

p.recvuntil(b">:)\n")
secret = p.recvline().strip()


The .strip() removes the trailing newline.

Sending the secret

The server then asks for the secret:

p.recvuntil(b"What's the secret?:")
p.sendline(secret)


Since the correct answer is already provided by the server, we simply echo it back.

Repeating the process

The service requires multiple rounds. The loop handles the remaining 19 secrets:

for i in range(19):
    p.recvuntil(b"\n")
    secret = p.recvline().strip()

    p.recvuntil(b"What's the secret?:")
    p.sendline(secret)


Each iteration:

waits for the next secret,
reads it,
waits for the question,
sends the secret back.

This avoids manually responding to every round and allows the interaction to happen quickly.

Getting the flag

After all rounds are completed, the server responds with:

Woah, how'd you do that??


The next line contains the flag:

p.recvuntil(b"Woah, how'd you do that??\n")
print(p.recvline())

Key Takeaway

The trick is recognizing that the challenge gives us every secret before asking us to provide it. There is no need to predict or decode the values.

The challenge is primarily testing whether you can:

interact with a remote service,
automate repetitive input/output,
use Pwntools effectively,
correctly synchronize with the server's prompts.
Requirements

Install Pwntools:

pip install pwntools


Then run:

python3 solve.py

Flag

Running the script against the challenge server prints the flag after successfully completing all 20 rounds.

Note: The flag is intentionally not included here; run the exploit to retrieve it from the service.
