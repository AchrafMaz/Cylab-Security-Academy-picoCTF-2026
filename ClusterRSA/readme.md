A message has been encrypted using RSA, but this time something feels... more crowded than usual. Can you decrypt it?

Download the message.

Hints
1

RSA usually means two primes... but what if someone got greedy?
2

Prime factors decomposition

We download the message using wget , then we display it :

cat message.txt 

n = 8749002899132047699790752490331099938058737706735201354674975134719667510377522805717156720453193651
e = 65537
ct = 3891662771105467488888140657249806558204248580982414398721303729411975827561400201060615350757604497

<img width="1279" height="568" alt="screen" src="https://github.com/user-attachments/assets/8b329db4-3455-4e4e-9381-b7700b3fd125" />

using factordb.com we can find the 4 factors of n
then we use the python script above to decrypt the cipher :
picoCTF{mul71_rsa_c5d0a11c}
