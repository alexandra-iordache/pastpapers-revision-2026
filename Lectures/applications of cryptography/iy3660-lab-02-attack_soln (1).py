#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is your ciphertext. We'll use it throughout. 
ciphertext = b'\xffz\xde\x83\x90I\x08\tv\xf9:<7\xd6`,' \
             b'\xce\xa1\xbd\xdd\xda9jGI\x9fM\xe3\xc1\x07' \
             b'2\xde\xef\x183\xd5@M\xe0\x84vu\xdb\x1a9' \
             b'\xe6\n\x86\xf1\xf86\xf8\xc2\xba\xd4\xdb' \
             b'\x82\x84\x8b\xadU\xa4\xcf\x81'

def padding_oracle(ciphertext):
    """
    Use ``padding_oracle`` to create a padding oracle.

    :param ciphertext: a string

    :returns: ``True`` if the padding is correct, ``False`` otherwise

    :rtype: a boolean. 
    """

    from iy3660_lab_02_target import decryption_error
    from iy3660_lab_02_target import MACFailure
    from iy3660_lab_02_target import PaddingError
    from iy3660_lab_02_target import LengthError

    try:
        decryption_error(ciphertext)
    except MACFailure:
        return True
    except LengthError:
        return False
    except PaddingError:
        return False
    return True

def xor_value_at_pos(string, pos, value):
    """
    XOR value ``value`` to the byte at position ``pos`` in ``string``.

    ..  note::

        We write ``a.__xor__(b)`` instead of the simpler ``a ^ b``
        because ``a^b`` means exponentiation in Sage not XOR.

    :param string: a string
    :param pos: a byte position
    :param value: an integer `0 ≤ value < 256`

    :returns: the result of the XOR operation

    :rtype: a string
    """
    T = list(string)  # turn the bytes into a list
    t = T[pos]   # turn the byte at position ``pos`` into an integer
    t = t.__xor__(value) # xor with ``value``
    T[pos] = t # set new value
    return bytes(T) # return bytes

def attack_mee_simple(ciphertext):
    """
    Recover one byte of plaintext from ``ciphertext``

    :param ciphtertext: a string

    :returns: one byte of plaintext

    :rtype: a string

    """

    from iy3660_lab_02_target import block_size

    # first, we want to find the actual length of the padding

    # we do this by changing each bit of the second-last ciphertext block.
    # Because of the way CBC decryption works, this will change the corresponding
    # byte after decryption of the last block. If that bit belonged to the
    # plaintext, we will get a MAC check failure, if it belonged to padding,
    # we will get a padding error. This way, we can distinguish the cases

    padding_len = None
    for i in range(1, block_size):
        if not padding_oracle(xor_value_at_pos(ciphertext, len(ciphertext) - 2 * block_size + i, 1)):
            padding_len = block_size - i
            break

    print(padding_len)

    # now that we know the length of the padding, we can try to get the last byte
    # of the plaintext

    # we try every possible value for the last byte

    for last_byte in range(256):

        # and check whether the guess was correct. In particular, if we guessed
        # correctly, the decryption will produce a correct padding, and we will
        # get a MAC check failure. If we guessed wrongly, the padding will be wrong

        new_ciphertext = bytearray(ciphertext)
        for i in range(len(ciphertext) - block_size - padding_len, len(ciphertext) - block_size):
            new_ciphertext[i] ^= (padding_len - 1) ^ padding_len
        new_ciphertext[-block_size - padding_len - 1] ^= padding_len ^ last_byte
        
        if padding_oracle(new_ciphertext):
            return chr(last_byte)

out = attack_mee_simple(ciphertext)
print(out)
