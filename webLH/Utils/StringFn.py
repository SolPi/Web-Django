from Crypto.Hash import SHA256
import hashlib, binascii


def cryptoSHA256(strNoCrypto):
    hash = SHA256.new()
    hash.update(strNoCrypto)
    return binascii.hexlify(hash.digest())
