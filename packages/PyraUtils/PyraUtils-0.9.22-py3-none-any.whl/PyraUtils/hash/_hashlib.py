# -*- coding: utf-8 -*-

import hashlib
from enum import Enum

'''
区别：
1. hashlib 中的md5 是没有key的，最多是加salt； 而 hmac 是必须加key和指定具体的算法
2. 使用hmac算法比标准hash算法更安全，因为针对相同的password，不同的key会产生不同的hash。
'''

class Algorithms(Enum):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()
    blake2b = hashlib.blake2b()
    shake_256 = hashlib.shake_256()

class HashlibUtil:
    def __init__(self) -> None:
        pass

    def sign_01(self, digestmod:str, data:bytes):
        """
        跟 sign_02 的区别是可以额外支持OS本身所支持的所有算法，但是速度不如sign_02快。

        digestmod: 允许访问hashlib列出的哈希算法以及你的 OpenSSL 库可能提供的任何其他算法。 
                    常用的算法 - 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
                                'blake2b', 'blake2s',
                                'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
                                'shake_128', 'shake_256'
        PS： 同名的构造器要比 new()， 更快所以应当优先使用
    
        data： 数据
        """
        if not isinstance(digestmod, str):
            raise TypeError("Algorithm name must be a string")

        h = hashlib.new(digestmod)
        h.update(data)
        return h.digest()

    def sign_02(self, digestmod, data):
        """
        跟 sign_01 的区别是速度比sign_01快，应该优先被使用。

        algorithms: 算法名
        data： 数据
        """
        """
        跟 sign_01 的区别是速度比sign_01快，应该优先被使用。

        algorithms: 算法名
        data： 数据
        """
        hash_obj = Algorithms[digestmod.lower()].value
        hash_obj.update(data)
        return hash_obj.hexdigest().encode('utf-8')

    def sign_derivation(self, hash_name, password:bytes, salt:bytes, iterations:int=100000, dklen=None):
        """
        hash_name: 字符串, hash_name 是要求用于 HMAC 的哈希摘要算法的名称，例如 'sha1' 或 'sha256'。
        password 和 salt 会以字节串缓冲区的形式被解析.应当将 password 限制在合理长度 (例如 1024)。 salt 应当为适当来源例如 os.urandom() 的大约 16 个或更多的字节串数据。
        iterations 数值应当基于哈希算法和算力来选择。 在 2013 年时，建议至少为 100,000 次 SHA-256 迭代。
        dklen 为派生密钥的长度。 如果 dklen 为 None 则会使用哈希算法 hash_name 的摘要大小，例如 SHA-512 为 64。
        """
        if not isinstance(password, bytes) or not isinstance(salt, bytes):
            raise TypeError("Password and salt must be bytes")

        if len(password) > 1024:
            raise ValueError("Password length should be limited to reasonable size")

        dk = hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen)
        return dk.hex()

    def sign_blake2b(self, data: bytes = b'', digest_size: int = 64, key: bytes = b'', salt: bytes = b'',
                    person: bytes = b'', fanout: int = 1, depth: int = 1, leaf_size: int = 0,
                    node_offset: int = 0, node_depth: int = 0, inner_size: int = 0,
                    last_node: bool = False, usedforsecurity: bool = True):
        '''
        data: 要哈希的初始数据块，它必须为 bytes-like object。 它只能作为位置参数传入。
        digest_size: 以字节数表示的输出摘要大小。
        key: 用于密钥哈希的密钥（对于 BLAKE2b 最长 64 字节，对于 BLAKE2s 最长 32 字节）。
        salt: 用于随机哈希的盐值（对于 BLAKE2b 最长 16 字节，对于 BLAKE2s 最长 8 字节）。
        person: 个性化字符串（对于 BLAKE2b 最长 16 字节，对于 BLAKE2s 最长 8 字节）。
        '''
        if not isinstance(data, bytes) or not isinstance(key, bytes) or not isinstance(salt, bytes) or not isinstance(person, bytes):
            raise TypeError("data, key, salt and person must be bytes")

        h = hashlib.blake2b(digest_size=digest_size, key=key, salt=salt,person=person,
                            fanout=fanout, depth=depth, leaf_size=leaf_size, node_offset=node_offset,
                            node_depth=node_depth, inner_size=inner_size,
                            last_node=last_node, usedforsecurity=usedforsecurity)
        h.update(data)
        return h.hexdigest().encode('utf-8')

    # def verify_blake2b(self, sig, data=b'') -> bool:
    #     good_sig = self.sign_blake2b(data)
    #     return hmac.compare_digest(good_sig, sig)
