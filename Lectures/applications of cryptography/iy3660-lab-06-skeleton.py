#!/urs/bin/env python
#-*- coding: utf-8 -*-

"""
WARNING:

We suggest you use the AES-GCM implementation from the Cryptodome
library. This allows us to get AEAD encryption off-the-shelf (which is
not possible using PyCrypto only). Yet, it requires installing the
Cryptodome module.

The linux.cim.rhul.ac.uk machines come with PyCrypto pre-installed
(which is the predecessor of Cryptodome). Whilst they expose a similar
interface (and are both imported with the name "Crypto"), this code
will not work with that library. You can install Cryptodome by
running:
    python3 -m pip install pycryptodome.

This works on the linux.cim.rhul.ac.uk machines (and should also work
on your own computer).

Note that if you are using Sage this should not be a problem for you. 
"""

import argparse
import os.path
from Crypto.PublicKey import RSA

block_size = 16
key_size = 16
rsa_key_length = 2048
rsa_signature_length = rsa_key_length/8

class SignError(Exception):
    """
    We raise a ``SignError`` if the Signature does not verify correctly.
    """
    pass

class DecryptionError(Exception):
    """
    We raise a ``SignError`` if the Signature does not verify correctly.
    """
    pass

def public_key_generation(filename, key_len=rsa_key_length):
    """ Generates an RSA-`key_len` keypair file, and stores it
    at `filename`.

    :param key_len:     length in bits of the RSA modulus
    :param filename:    file path where the keypair will be stored
    """
    print("Key generation")
    key = RSA.generate(key_len)
    with open(filename,'wb') as f:
        f.write(key.export_key('PEM'))

def encrypt_symm_with_asym(rsa_pk, aes_sk):
    """ Encrypts the AES-GCM key used to encrypt the
    file directly with an RSA-OAEP asymmetric key

    :param rsa_sk: an RSA public key object
    :param aes_sk: a AES secret key object
    :param rtype: a string
    """
    raise NotImplementedError()

def decrypt_symm_with_asym(rsa_sk, ciphertext):
    """ Decrypts the AES-GCM key used to encrypt the
    file directly with an RSA-OAEP asymmetric key

    :param rsa_sk: an RSA public key object
    :param aes_sk: a AES secret key object
    :param rtype: a string
    """
    raise NotImplementedError()

def encrypt_file(output_filename, input_filename, input_rsa_key):
    """Encrypt file `input_filename` under given `input_rsa_key` public key.

    :param output_filename: result is written to this file
    :param input_filename: this file is read and encrypted
    :param input_rsa_key: this file is read and used to encrypt symmetric key
    :param password: the password is used to generate an encryption key

    """

    # AEAD key generation
    raise NotImplementedError()

    # Load PKE keys
    raise NotImplementedError()

    # Public-key encrypt (aka encapsulate) the symmetric key
    raise NotImplementedError()

    # Prepare an authenticated encryption scheme engine (note, GCM depends on having pycryptodome)
    raise NotImplementedError()

    with open(input_filename, "rb") as input_filehandle:
        with open(output_filename, "wb") as output_filehandle:

            # Load and encrypt plaintext file
            raise NotImplementedError()

            # Concatenate the encapsulated aead key, the nonce, and the ciphertext and tag pair
            raise NotImplementedError()

            # Public-key sign the ciphertext
            raise NotImplementedError()

            # Write the output signature || concatenated_ciphertext
            raise NotImplementedError()


def decrypt_file(output_filename, input_filename, input_rsa_key):
    """Decrypt file `input_filename` under given `input_rsa_key` public key.

    :param output_filename: result is written to this file
    :param input_filename: this file is read and decrypted
    :param input_rsa_key: this file is read and used to decrypt symmetric key

    """
    # Load and encrypt plaintext file
    raise NotImplementedError()

    with open(input_filename, "rb") as input_filehandle:
        with open(output_filename, "wb") as output_filehandle:
            # Load ciphertext file
            raise NotImplementedError()

            # Verify signature
            raise NotImplementedError()

            # Parse AEAD ciphertext components
            raise NotImplementedError()

            # recover AEAD key, and prepare crypto engine
            raise NotImplementedError()

            # decrypt and verify integrity of plaintext
            raise NotImplementedError()

            # Write plaintext to file
            raise NotImplementedError()

def parse_commandline():
    """Parse command line arguments and check for consistency.

    :returns: parameters
    :rtype: argparse.Namespace

    """
    parser = argparse.ArgumentParser(description='Encrypt all the files.')
    parser.add_argument('--encrypt',  '-e',
                        action='store_true', help="encrypt!")
    parser.add_argument('--decrypt',  '-d',
                        action='store_true', help="decrypt!")
    parser.add_argument('--output',   '-o', type=str,
                        help="output filename")
    parser.add_argument('input', nargs=1, help='the input filename')
    parser.add_argument('--asymkey',   '-a', type=str,
                        help="asymmetric key")
    args = parser.parse_args()

    if not (args.encrypt or args.decrypt):
        raise ValueError("Either encrypt with -e or decrypt with -d")

    return args

def main():
    """Run the encryption/decryption program.

    Example usage:
        $ echo "foobar" > deadbeef
        $ python iy3660-lab-06-solution.py --encrypt --output deadbeef.c --asymkey rsakey.pem deadbeef
        $ python iy3660-lab-06-solution.py --decrypt --output deadbeef.p --asymkey rsakey.pem deadbeef.c
    """
    args = parse_commandline()
    if args.encrypt:
        # if rsa key file does not exist, generate a new RSA keypair
        if not os.path.exists(args.asymkey):
            public_key_generation(args.asymkey)
        encrypt_file(args.output, args.input[0], args.asymkey)
    else:
        decrypt_file(args.output, args.input[0], args.asymkey)

if __name__ == '__main__':
    main()
