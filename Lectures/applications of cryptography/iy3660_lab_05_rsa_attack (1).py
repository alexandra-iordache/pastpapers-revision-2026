from iy3660_lab_05_rsa_attack_auxiliary import get_public_key, get_target_ciphertext, encryption_oracle, decryption_oracle

"""
The aim of this exercise is to successfully use a decryption 
oracle attack to break naive RSA. Auxiliary functions are provided
as an interface to the RSA implementation and the secret values.

The goal is to print, in hex format, the decryption of the 
ciphertext returned by get_target_ciphertext(). You will know 
when this is correct by the form of this hex value.

iy3660_lab_05_rsa_attack_auxiliary provides you with
four functions. These are sufficient to execute the
attack on RSA; they use your RSA implementation, but the details are abstracted so you can focus on the attack itself.

get_public_key() takes no arguments, and returns (e, N), the
RSA public key. e is the public RSA exponent, and N is the
RSA modulus.

get_target_ciphertext() returns an integer representing the
target ciphertext. For your convenience, this has already been converted from its hex values.

encryption_oracle(m), when provided with an integer which represents a message, returns an integer which represents the RSA ciphertext  under the public key returned by get_public_key. This is provided for your convenience; it would be possible to use your RSA encryption implementation directly using the public key.

decryption_oracle, when provided with an integer which represents 
a ciphertext, returns its decryption under the unknown RSA  
private key which corresponds to the public key returned by 
get_public_key(), UNLESS that ciphertext is the target one 
returned by get_target_ciphertext().

You may also find yourself needing randbelow, from the secrets module, or functions from the SymPy module. You should look up the documentation of these modules to figure out what these do. They should be imported in the normal way.


"""

def main():
    # Put your implementation of the attack here.
    raise NotImplementedError("Implement the attack!")

if __name__ == "__main__":
    main()
