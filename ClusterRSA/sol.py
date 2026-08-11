import math

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m if g == 1 else None

def decrypt_multi_prime_rsa(primes, ciphertext, e=65537):
    n = math.prod(primes)
    phi = math.prod([p - 1 for p in primes])
    d = modinv(e, phi)

    return pow(ciphertext, d, n)

if __name__ == "__main__":
    primes = [ 9671406556917033397931773,9671406556917033398314601,9671406556917033398439721,9671406556917033398454847]
    e = 65537
    ciphertext = 3891662771105467488888140657249806558204248580982414398721303729411975827561400201060615350757604497

    plaintext = decrypt_multi_prime_rsa(primes, ciphertext, e)
    text = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big').decode('utf-8')
    print(text)
