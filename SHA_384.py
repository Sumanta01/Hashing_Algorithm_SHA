# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:01:18 2023

@author: KIIT
"""
import hashlib

str="Sumanta swain"
hashedval=hashlib.sha384(str.encode())
print(hashedval)
print(hashedval.hexdigest())