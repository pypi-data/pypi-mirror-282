# -*- coding: utf-8 -*-
# -------------------------------

# @IDE：PyCharm
# @Python：3.1x
# @Project：DP

# -------------------------------

# @fileName：_pad.py
# @createTime：2024/7/3 9:50
# @author：Primice

# -------------------------------
from Cryptodome.Util.Padding import pad, unpad


def Pkcs7(_data: bytes, _decrypt=False):
    if _decrypt:
        return unpad(_data, 16, style='pkcs7')
    return pad(_data, 16, style='pkcs7')

def NoPadding(_data: bytes, _decrypt=False):
    # _data = _data.decode()
    if _decrypt:
        return _data.rstrip('\0')
    return _data + (16 - len(_data) % 16) * b'\0'
