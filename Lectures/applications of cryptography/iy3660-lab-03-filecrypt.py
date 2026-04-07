#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# We're using AES-128
block_size = 16
key_size = 16


class PaddingError(Exception):
    """
   We raise a ``PaddingError`` if padding is wrong.
   """
    pass

class LengthError(Exception):
    """
   We raise a ``LengthError`` if the padding byte is greater than the block-size.
   """
    pass

def add_padding(message):
    """Pad message to multples of `block_size`.

    If the message already has a length which is a multiple of `block_size`
    we add `block_size` bytes of padding to avoid ambiguity.

    :param message: byte string
    :returns: padded message
    :rtype: byte string

    :note: this function returns a byte string. This is because PyCryptoDome's internal
    functions are written to expect a C-style string, rather than the Python str class. 

    ::
    >>> add_padding("Hello IY3660".encode()).hex()
    '48656c6c6f2049593336363003030303'
    """

    # Compute the length of the padding.
    padding_length = block_size - (len(message) % block_size)

    # Actually redundant (can you see why?)
    if padding_length == 0:
        padding_length = block_size

    # chr(i) converts `i` to its unicode representation.
    # For the sake of this tutorial, you can view this as a byte.
    padding = [chr(padding_length - 1) for _ in range(padding_length)]
    # This invocation turns the padding list into an encoded string
    # and concatentates it to the encoded message. 
    return message + ''.join(padding).encode()

def remove_padding(encoded):
    """Remove padding allegedly added by `add_padding`.

    :param encoded: a byte string with some padding
    :returns: the message without padding
    :rtype: byte string.

    : note: similarly to add_padding, this function returns a byte string. This is because
    PyCryptoDome's internal functions are written to expect a C-style string, rather than the Python
    str class.
    
    ::

    >>> remove_padding(bytes.fromhex('48656c6c6f2049593336363003030303')).decode("utf-8")
    'Hello IY3660'
    """

    encoded_length = len(encoded)
    padding_byte = encoded[encoded_length - 1]
    padding_length = padding_byte + 1

    if padding_length > block_size:
        raise LengthError()

    for i in range(padding_length):
        if encoded[encoded_length - i - 1] != padding_byte:
            raise PaddingError()  # Uh-oh!

    plaintext_length = encoded_length - padding_length
    return encoded[:plaintext_length]

def password_to_key(password):
    """Turn password into key for block cipher.

    :param password: a string
    :returns: a string of length `key_size`
    :rtype:  a string

    """
    hash = SHA256.new()
    raise NotImplementedError # You need to fill this in. 

def encrypt_file(output_filename, input_filename, password):
    """Encrypt file `input_filename` under given `password`.

    :param output_filename: result is written to this file
    :param input_filename: this file is read and encrypted
    :param password: the password is used to generate an encryption key

    """
    key = password_to_key(password)
    raise NotImplementedError

    with open(input_filename, "rb") as input_filehandle:
        with open(output_filename, "wb") as output_filehandle:
            plaintext = input_filehandle.read()

            raise NotImplementedError

            output_filehandle.write(ciphertext)

def decrypt_file(output_filename, input_filename, password):
    """Decrypt file `input_filename` under given `password`.

    :param output_filename: result is written to this file
    :param input_filename: this file is read and decrypted
    :param password: the password is used to generate an encryption key

    """
    key = password_to_key(password)
    raise NotImplementedError

    with open(input_filename, "rb") as input_filehandle:
        with open(output_filename, "wb") as output_filehandle:
            ciphertext = input_filehandle.read()

            raise NotImplementedError

            output_filehandle.write(plaintext)

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
    parser.add_argument('--password', '-p', type=str,
                        help="password", required=True)
    parser.add_argument('--output',   '-o', type=str,
                        help="output filename")
    parser.add_argument('input', nargs=1, help='the input filename')

    args = parser.parse_args()

    if not (args.encrypt or args.decrypt):
        raise ValueError("Either encrypt with -e or decrypt with -d")

    return args

def main():
    """Run the encryption/decryption program.
    """
    args = parse_commandline()
    if args.encrypt:
        encrypt_file(args.output, args.input[0], args.password)
    else:
        decrypt_file(args.output, args.input[0], args.password)

if __name__ == '__main__':
    import doctest    
    doctest.testmod()
    main()
