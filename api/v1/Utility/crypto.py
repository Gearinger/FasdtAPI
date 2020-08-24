"""
ECB没有偏移量
"""
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex, a2b_hex
from Crypto.PublicKey import RSA


def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text, key):
    '''加密函数'''
    key = key.encode('utf8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    crypto = AES.new(key, mode)

    cipher_text = crypto.encrypt(text)
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text, key):
    '''解密后，去掉补足的空格用strip() 去掉'''
    key = key.encode('utf8')
    mode = AES.MODE_ECB
    crypto = AES.new(key, mode)
    plain_text = crypto.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


class RsaKey():
    def __init__(self,private_pem, public_pem):
        self.private_pem = private_pem
        self.public_pem = public_pem


def get_rsa_keys():
    '''获取rsa密钥对'''
    random_generator = Random.new().read
    rsa = RSA.generate(1024, random_generator)
    # master的秘钥对的生成
    private_pem = rsa.exportKey()
    public_pem = rsa.publickey().exportKey()
    return RsaKey(private_pem, public_pem)


if __name__ == '__main__':
    e = encrypt("hello world", '1111111111111111')  # 加密
    d = decrypt(e, '1111111111111111')  # 解密
    print("加密:", e)
    print("解密:", d)
    get_rsa_keys()
