from pwn import *


host = "mysterious-sea.picoctf.net"

port = 54107

p = remote(host,port)

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
