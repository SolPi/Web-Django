import hashlib, binascii
from Crypto.Hash import SHA256


def cryptoSHA256(strNoCrypto):
    hash = SHA256.new()
    hash.update(strNoCrypto)
    return binascii.hexlify(hash.digest())
