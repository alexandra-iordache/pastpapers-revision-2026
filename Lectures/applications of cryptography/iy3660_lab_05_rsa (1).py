# Functions for Part 1. You need to implement these functions - follow the lab sheet for a description on how.

"""
The aim of this exercise is to implement RSA key generation, 
encryption and decryption correctly. A function, test_RSA, is 
provided: this returns true if a run of your implementation at the 
provided bit size satisfies the "Decrypt is inverse to Encrypt"  
property.

The goal is to implement them such that running the module causes the message "Your naive RSA works!" to print from main().

Do not modify main() or test_RSA().

You may find yourself needing randbelow from the secrets module, 
already imported, or functions from the sympy module like igcd, 
mod_inverse, and randprime. You should look up the documentation of 
these modules to figure out what these do. They should be imported in 
the normal way.

"""


def key_gen(bit_size):
    """
    Return a random RSA public key ``pk = (N, e)`` and RSA secret key 
    ''sk = d'' such that ``N`` is a number of about ``bit_size`` bits 
    in length.

    In other words, key_gen should return an RSA public key and an RSA secret key.
    :param bit_size an integer > 0
    :returns (N, e), d
    
    """
    raise NotImplementedError("Implement key generation!")


def enc(pk, m):
    """
    Return encryption of ``m`` under ``pk``

    :param pk: an RSA public key
    :param m: an RSA message
    :returns: an RSA ciphertext

    In other words, enc takes a public key pk and a message m (a positive integer < N)
    and returns the encryption of m under pk.

    """
    raise NotImplementedError("Implement encryption!")


def dec(pk, sk, c):
    """
    Return decryption of ``c`` under ``sk``

    :param pk: An RSA public key
    :param sk: An RSA secret key
    :param c: An RSA ciphertext
    :returns: An RSA message

    In other words, dec takes a public key pk, a secret key sk and a ciphertext c
    and returns the decryption of c under sk.

    """
    raise NotImplementedError("Implement decryption!")

def test_RSA(bit_size=512):
    """
    Test your RSA implementation at a specified bit size.
    
    :param bit_size: Bitsize to test at. Default is 512, which is low-security.

    """
    e, N, d = key_gen(bit_size)
    pk = (e, N)
    sk = d
    # Generate a random element modulo pk
    m = random.randint(0, pk[1] - 1)

    c = enc(pk, m)
    m2 = dec(pk, sk, c)

    return m2 == m  # If all works, this will be True

def main():
  print("Your naive RSA", "works!" if test_RSA() else "doesn't work!")

if __name__ == "__main__":
  main()
