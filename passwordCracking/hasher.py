#! /usr/bin/env python3
import hashlib

hashvalue=input("*Enter a String to hash")
hashobj1=hashlib.md5()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

hashobj1=hashlib.sha1()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

hashobj1=hashlib.sha224()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

hashobj1=hashlib.sha256()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

hashobj1=hashlib.sha512()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())