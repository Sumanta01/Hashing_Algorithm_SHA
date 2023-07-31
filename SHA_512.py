# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:59:35 2023

@author: KIIT
"""

import hashlib


str="Sumanta swain"
hashedval=hashlib.sha512(str.encode())
print(hashedval)
print(hashedval.hexdigest())