from iy3660_lab_05_rsa import dec, enc

"""
Do not modify this file. You do not need to read this file to complete the
exercise. Do not read decryption_oracle() in particular.

"""

def hex_to_integer(lst):
  """
  Auxiliary function for converting hex'd integers into actual integers.
  """

  hx = "".join(lst)
  return int(hx, 16)

def get_public_key():
  """
  Function which returns the RSA public key.
  """
  e = [
    "438dfe55ab5ebbd567198169d9be643c",
    "3798250d071dc04b1019f1c69a6a98c8",
    "ebb3b717dd57709649ba11910988b994",
    "f34f29e2e3496c30013d42c8dba81ae7",
    "7c8a569153b3102308db75715f80971d",
    "6c3dfd542cd6ec7d81102abcba28beeb",
    "125dc6c10552b4d227a1985498a5edc9",
    "87b9d0f97dd2e2f1afe4a584d46641c6",
    "7380e50817cf190f934b0da61b07de31",
    "36e78eb2918255f77905d9326017654b",
    "3bec3acb454ec6bb505d6fdf028ba06c",
    "b9cb4145abe4f9d98c577a36157d2c70",
    "0f415e07f3ea93664efe3582cd490aba",
    "2eab2f7ebb7ec29efdaab6e1c476890a",
    "3f72d5710df411caf7c1027d3ee4159e",
    "743f1d69a28c7f512a35098bde86729d",
  ]
  N = [
    "6e84a7c72731a3c942d21be811547c87",
    "2962cd69bd66bc2e148132ba76abc00c",
    "15000cf7eb66fd3dd91b324771722369",
    "51abd19a7651d0a45ff8881d3b9d9dd1",
    "6bafe6d7849e4ad1675ecbb224ca7b25",
    "ab619e5e09662f229d3cc1e120015c69",
    "dfc069ed0bd9c0b0d85aad1e858f618f",
    "7d1898f33f5936639e7d3473691a9376",
    "1bcbadbbb7cde7e234b6ae50eb72f510",
    "e42dfc1981020ac752aadf718578be15",
    "ea50ba6b38f8305614813b051b79c9d5",
    "ccae7b1989c21f6bd3153b09929dadb8",
    "5ac60e27bc2fc79c2e82acf53a8dfc26",
    "fa210444b79383e44dc1030a65cda602",
    "16b50c9094d3a81246a72db9d7d63c63",
    "b003db93637f0aaba9fefd43b3cff23f",
  ]
  return (hex_to_integer(e), hex_to_integer(N))

def get_target_ciphertext():
  """
  Function which returns the target ciphertext.
  """
  c_star = [
    "24f4257a2c25b66f67f71a61945caaf9",
    "5c1490337e1d0c3665c2b6fdcc13a94e",
    "5705d1f8c36ea8b4c2e55b3af0bebc13",
    "423792fc57e0ddb53c20ce54393d698b",
    "153b03deb7a10371c6e1eac3c02e6f14",
    "9ff92db7450d3f9496e73a9656a3b7d8",
    "b41f72b5b7ed3ddc1bd3cea5d53a96fe",
    "2dc38265752efbf8ea7ed3e699c8a709",
    "5471aab2e214b297be6e41ccc82ab85c",
    "4374a0afbc080057473d0c1e201693b5",
    "b66f889efaeb698f558189213e189e84",
    "161ddfb4d156f07bca44ea0cb6460875",
    "cdce35270105e3d705665303d4a6f7db",
    "6d50121a8d50909991b4eff0d9dca170",
    "380008c5246e81ea7df50c05c0579204",
    "f59c596cbc74f137bf89747b1e015636",
  ]
  return hex_to_integer(c_star)

def encryption_oracle(m):
    """
    Encryption oracle. Provided for convenience.
    """
    pk = get_public_key()
    
    return enc(pk, m)


### WARNING : DO NOT READ BELOW ###

# Do not modify or read this function - treat it as a black box.
def decryption_oracle(c):
    """
    Decryption oracle.
    """
    
    c_star = get_target_ciphertext()

    if c == c_star:
        raise ValueError("That's cheating!")

    d = [
        "43cd48748e1f69867c13bd9c58795946",
        "47a6f69909141a268a13332ce5ff01ff",
        "a917301a84b7980e671aad1f7b51316b",
        "a1b3d966a1fa03dceeabd6906fcfc085",
        "cd41b5dfb15da488e1675bb2900a0903",
        "2a18fd9182b4371434407eb77c1e3767",
        "5d32e3aafc55d2f8c4a9485090513ab2",
        "7a41d38432877646205fec97023b556d",
        "8e6ba0369f36e246b74a2fdbc60f1f80",
        "a6b02f9589ede1ac26bc4987c54e949e",
        "b06b9c53ecd13e620acfc98446669d38",
        "36269f1ff3a0c42423edcae06c0f4d5b",
        "264fb037693748a9399b5a3ba6f1f2f3",
        "c632b12594d01486de4f81ba43edff2d",
        "42828ba3137ed36dc5f913a7f1bca01e",
        "7768176f1063b274527694628394a6a5",
    ]

    sk = hex_to_integer(d)

    pk = get_public_key()
    
    return dec(pk, sk, c)

### WARNING : DO NOT READ ABOVE ###

if __name__ == "__main__":
  pass