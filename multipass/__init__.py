# -*- coding: utf-8 -*-
import datetime
import json
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
from Crypto.Random import get_random_bytes
from base64 import urlsafe_b64encode


class Multipass:
    def __init__(self, secret):
        key = SHA256.new(secret.encode('utf-8')).digest()
        self.encryptionKey = key[0:16]
        self.signatureKey = key[16:32]

    def generateToken(self, customerDataHash):
        customerDataHash['created_at'] = datetime.datetime.utcnow().isoformat()
        cipherText = self.encrypt(json.dumps(customerDataHash))
        return urlsafe_b64encode(cipherText + self.sign(cipherText))

    def generateURL(self, customerDataHash, url):
        token = self.generateToken(customerDataHash).decode('utf-8')
        return '{0}/account/login/multipass/{1}'.format(url, token)

    def encrypt(self, plainText):
        plainText = self.pad(plainText)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.encryptionKey, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(plainText)

    def sign(self, secret):
        return HMAC.new(self.signatureKey, secret, SHA256).digest()

    def pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
