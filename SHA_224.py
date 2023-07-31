# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:00:20 2023

@author: KIIT
"""

import hashlib

str="Sumanta swain"
hashedval=hashlib.sha224(str.encode())
print(hashedval)
print(hashedval.hexdigest())