import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import HMAC

block_size = 16 # AES uses 16 byte block sizes.
key_size = 16 # Here we're using good ole AES-128

# Key derivation function.
def kdf(msk):
    """
    Produce MAC and encryption keys from a singular master
    key.
    :param msk ("master secret key"): a string which acts as a master secret.
    :returns a mac key and an encryption key for AES-128.
    :rtype a tuple of two keys.

    ::
    
    >>> out = kdf("CRYPTO")
    >>> out[0].hex()
    '487857bcc3181258953065f5d4c55606'
    >>> out[1].hex()
    '1f639a8dc4e5987d655dca7754252ddf'
    """
    

    # Create a new key derivation object. In Python, this is done via an
    # object (can you see why?)
    kdf = SHA256.new()
    # We encode the msk as a series of bytes. This is so we can use it
    # in the key derivation function as some input state.
    kdf.update(str.encode(msk))

    # Output our random keying material.
    key_material = kdf.digest()

    # We'll take the first key_size bytes as our mac_key, and the second
    # as the enc_key. This is actually typical in practice.
    mac_key = key_material[:key_size] # 0,..., key_size - 1
    enc_key = key_material[key_size:] # key_size,..., len(key_material) - 1
    return mac_key, enc_key


# We treat each type of padding error as an exception that can be raised.
class PaddingError(Exception):
# This is raised if the padding is wrong.
    pass

class LengthError(Exception):
# This is raised if the padding length is too long. 
    pass


# These functions add and remove padding to a message.
# Note that we use the "simplified TLS padding" introduced in class:
# 1. We compute b = padding_length - (len(message) % block_size). This is the
# value of our padding byte.
# 2. We append b copies of b-1 to the end of the message. Note that if b == 0, then
# then we add block_size copies of 0x0f to the end of the message: this means our padding
# is a full empty block. This is for determinism, with the implication that the last
# byte of the message is always a byte of padding. 

def add_padding(message):
    """
    Pads message to a multiple of "block_size" using the simplified TLS padding
    scheme. If the message has a length that is already a multiple of "block_size"
    then we add "block_size" many padding bytes to avoid ambiguity.
    :param message: the message to pad.
    :returns a padded message.

    ::
    >>> add_padding("Hello IY3660!").encode("utf-8").hex()
    '48656c6c6f2049593336363021020202'
    """

    # Compute the length of the padding.
    padding_length = block_size - (len(message) % block_size)
    # If the message was already a multiple of block_size in length, round up.
    if padding_length == 0:
        padding_length = block_size

    # chr(i) converts `i` to its unicode character representation.
    # For the sake of this tutorial, you can view this as a byte.
    padding = [chr(padding_length-1) for _ in range(padding_length)]
    # Pad the message.
    # Note that the "if" here is just for testing purposes.
    if isinstance(message, bytes):
        return message + ''.join(padding).encode("utf-8")
    elif isinstance(message, str):
        return message + ''.join(padding)
    else:
        # We only accept bytes or strings. 
        assert(False)
    

def remove_padding(encoded):
    """
    Remove the padding allegedly added by "add_padding". This function
    removes the bytes added by the simplified TLS padding scheme.

    ::
    >>> remove_padding(bytes.fromhex('48656c6c6f2049593336363021020202').decode("utf-8"))
    'Hello IY3660!'
    
    """

    encoded_length = len(encoded)
    # We know the last byte is _always_ a byte of padding.
    padding_byte = encoded[encoded_length - 1]
    # ord(i) converts `i` from a unicode character to a byte.

    # If encoded is already a byte string, then we don't need to do the
    # conversion. Otherwise, if encoded is a string, then we need to do
    # a conversion to a byte. Thankfully, ord(i) converts `i` into a byte.

    # Note that whatever the value of `i` is, we added `i+1` bytes
    # of padding to the message. Thus, the length of the padding is
    # padding_byte + 1.
    
    if isinstance(encoded, bytes):
        padding_length = padding_byte + 1
    elif isinstance(encoded, str):
        padding_length = ord(padding_byte) + 1
    else:
        assert(False)


    # If we've added too much padding, break.
    if padding_length > block_size:
        raise LengthError()

    # Strip off the padding
    for i in range(padding_length):
        if encoded[encoded_length - i - 1] != padding_byte:
            raise PaddingError() # Uh-oh!

    plaintext_length = encoded_length - padding_length
    return encoded[:plaintext_length]


def add_mac(message, key):
    """
    add_mac. This function adds a MAC to the "message" under the key "key".
    :param message: a string.
    :param key: a string of length "key_size"
    :returns a message with a tag prepended.

    :rtype a byte list.

    ::
    >>> mac_key = kdf("SuperSecretPassword")[0]
    >>> add_mac("CRYPTO", mac_key).hex()
    '36ed7318655af6b1ae7161cc364726da96452dbd935733c9ca63c063e83a827a43525950544f'
    """

    # As for key derivation, HMACs are handled as objects.
    h = HMAC.new(key, digestmod=SHA256)
    h.update(message.encode("utf-8"))
    # Produce the tag.
    tau = h.digest()
    # Note: for the sake of this lab we are going to assume that this is true.
    # This is to make implementation slightly easier. This is not necessarily true
    # in practice, but it is for all major symmetric schemes (e.g AES-128 and SHA-256).
    assert(len(tau) % block_size == 0)
    return tau + message.encode("utf-8")

# If the mac checking fails, we raise a MACFailure.
class MACFailure(Exception):
    pass

def check_and_remove_mac(message, key):
    """
    Check MAC tag and remove it if it is valid, otherwise raise
    "MacFailure" error.

    The first "SHA256.digest_size" bytes are intepreted as the
    MAC tag.

    :param message: a list of bytes.
    :param key: a string of length "key_size".
    :returns a message without the MAC tag.

    ::
    >>> mac_key = kdf("SuperSecretPassword")[0]
    >>> macd = add_mac("CRYPTO", mac_key)
    >>> check_and_remove_mac(macd, mac_key) == b'CRYPTO'
    True

    >>> kd = kdf("SuperSecretPassword")
    >>> mac_key = kd[0]
    >>> f_key = kd[1]
    >>> macd = add_mac("CRYPTO", mac_key)
    >>> check_and_remove_mac(macd, f_key)
    Traceback (most recent call last):
        ...
    MACFailure
    """

    # This function is essentially the opposite of add_mac.

    # KDFs etc are still objects.
    h = HMAC.new(key, digestmod=SHA256)

    # Recall that the first SHA256.digest_size bytes are the tag.
    tau_ = message[:SHA256.digest_size]
    message = message[SHA256.digest_size:]

    # Produce the MAC. This is the same as what add_mac did.
    h.update(message)
    tau = h.digest()
    if tau != tau_:
        raise MACFailure()

    return message


def encrypt(data, key, iv = None):
    """ encrypt "data" under key "key" using AES-128 in CBC mode with random IVs.
    :param data: a string to be encrypted. Must be a multiple of "block_size"
    in length.
    :param key: a string of length "key_size"
    :param iv: the IV to use. This is only used during testing to ensure deterministic output.
    This does not form part of the lab: it is just here to facilitate testing of this function.
    Don't use it!
    :returns a ciphertext with a random IV prepended.

    ::

    >>> aes_key = kdf("SuperSecretPassword")[1]
    >>> iv = bytes.fromhex("b412c0e6deed7d80fad1c63528b7e921")
    >>> encrypt(add_padding("Hello IY3660!"), aes_key, iv).hex()
    'b412c0e6deed7d80fad1c63528b7e921f7bd491012dd04e4687463b725ec449b'
    
    """

    if iv is None:
        # Firstly we create a random IV using the operating system's randomness.
        # Again, this will be the case for the lab in general: this is just
        # here to facilitate testing.
        iv = os.urandom(block_size)

    crypto_engine = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    assert(len(data) % block_size == 0)

    # For testing purposes, we allow the user to pass bytes in here.
    # Convert them if needed.
    if isinstance(data, str):
        data = data.encode("utf-8")
    
    ciphertext = crypto_engine.encrypt(data)
    return iv + ciphertext

def decrypt(ciphertext, key):
    """
    decrypt "ciphertext" under key "key" using AES-128 in CBC mode with random IVs.
    The first "block_size" bytes of the ciphertext are interpreted as the IV.
    :param data: a string to use for encryption. Must have a length that is a multiple of
    "block_size".
    :param key: a string of length "key_size"
    :returns a plaintext. 

    ::

    >>> aes_key = kdf("SuperSecretPassword")[1]
    >>> iv = bytes.fromhex("b412c0e6deed7d80fad1c63528b7e921")
    >>> ct = encrypt(add_padding("Hello IY3660!"), aes_key, iv)
    >>> remove_padding(decrypt(ct, aes_key).decode("utf-8"))
    'Hello IY3660!'
    
    """
    
    assert(len(ciphertext) % block_size == 0)
    iv = ciphertext[:block_size]
    ciphertext = ciphertext[block_size:]
    crypto_engine = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    return crypto_engine.decrypt(ciphertext)


# Finally, we'll put everything together into something called Authenticated encryption.
# We'll cover this more in class soon.

def mee_encrypt(plaintext, msk, iv = None):
    """
    Perform TLS-style authenticated encryption.
    :param plaintext: a string.
    :param msk: the master secret key, used to derive key material.
    :returns a ciphertext.

    ::
    >>> iv = bytes.fromhex("ff7ade839049080976f93a3c37d6602c")
    >>> mee_encrypt("Hello IY3660!", "SuperSecretPassword", iv).hex()
    'ff7ade839049080976f93a3c37d6602c796210b7916288f0c681b9ea60c727d0bc5ba40adb75b23032347c4fd5f8d939a605f63e9c56cd6bed7d57a42a25818e'
    """
    mac_key, enc_key = kdf(msk)
    authenticated = add_mac(plaintext, mac_key)
    encoded = add_padding(authenticated)
    return encrypt(encoded, enc_key, iv)


def mee_decrypt(ciphertext, msk):
    """
    Perform TLS-style authenticated decryption.
    :param ciphertext: a string.
    :param msk: a master secret key, used to derive key material.
    :returns a plaintext.

    ::
    
    >>> iv = bytes.fromhex("ff7ade839049080976f93a3c37d6602c")
    >>> ct = mee_encrypt("Hello IY3660!", "SuperSecretPassword", iv)
    >>> mee_decrypt(ct, "SuperSecretPassword").decode("utf-8")
    'Hello IY3660!'

    
    """
    mac_key, enc_key = kdf(msk)
    encoded = decrypt(ciphertext, enc_key)
    authenticated = remove_padding(encoded)
    plaintext = check_and_remove_mac(authenticated, mac_key)
    return plaintext

def decryption_error(ciphertext):
    """
    This function is your entry point to this lab. We attempt to decrypt our
    given ciphertext with the following key.
    """
    msk = "SuperSecretPassword"
    mee_decrypt(ciphertext, msk)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
